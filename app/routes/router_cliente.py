from typing import List


from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.vendas import Venda
from schemas.venda_schema import VendaSchema

from models.cliente import Cliente
from schemas.cliente_schema import ClienteSchama
from core.deps import get_session

router = APIRouter()

@router.post('/', response_model=ClienteSchama, status_code=status.HTTP_201_CREATED)
async def post_client(cliente: ClienteSchama, db: AsyncSession = Depends(get_session)):
    async with db as session:
        novo_cliente = Cliente(
            nome = cliente.nome,
            contato = cliente.contato,
            endereco = cliente.endereco,
        )
        session.add(novo_cliente)
        await session.commit()
        return novo_cliente

@router.get('/{id}')
async def get_client_by_id(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Cliente).filter(Cliente.id == id)
        resultado = await session.execute(query)
        cliente = resultado.unique().scalar_one_or_none()
        if cliente:
            return cliente
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado !")

@router.get('/', status_code=status.HTTP_200_OK)
async def get_client(name: str = Query(default=None, description="Para buscar todos os clientes com o nome escrito", title="Nome"), db: AsyncSession = Depends(get_session)):
    async with db as session:
        if not name:
            query = select(Cliente)
        else:
            query = select(Cliente).filter(Cliente.nome.like(f'%{name}%'))
        resultado = await session.execute(query)
        clientes : List[Cliente] = resultado.scalars().unique().all()
        for cliente in clientes:
            del cliente.vendas
        return clientes


@router.post('/compra/{id}', response_model=List[VendaSchema])
async def post_cliente_compra(id: int, compras: List[VendaSchema], db: AsyncSession = Depends(get_session)):

    async with db as session:
        novas_compras = []
        query = select(Cliente).filter(Cliente.id == id)
        resultado = await session.execute(query)
        cliente: Cliente = resultado.unique().scalar_one_or_none()
        if cliente:
            for compra in compras:
                nova_compra = await salvar_venda(criar_venda(compra=compra), session)
                novas_compras.append(nova_compra)
            cliente.vendas.extend(novas_compras)
            await session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado !")   
        return compras


async def salvar_venda(compra: Venda, session: AsyncSession):
    session.add(compra)
    await session.commit()
    return compra


def criar_venda(compra: VendaSchema):
    return Venda(
                titulo=compra.titulo,
                descricao=compra.descricao,
                valor=compra.valor,
                data_prevista_pagamento=compra.data_prevista_pagamento)