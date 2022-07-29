from re import I
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
        cliente = resultado.scalars().unique().first()
        return cliente

@router.get('/', status_code=status.HTTP_200_OK)
async def get_client(name: str = Query(default=None, description="Para buscar todos os clientes com o nome escrito", title="Nome"), db: AsyncSession = Depends(get_session)):
    async with db as session:
        if not name:
            query = select(Cliente)
        else:
            query = select(Cliente).filter(Cliente.nome.like(f'%{name}%'))
        resultado = await session.execute(query)
        clientes : List[Cliente] = resultado.scalars().unique().all()
        return clientes

@router.post('/compra/{id}')
async def post_cliente_compra(id: int, compras: List[VendaSchema], db: AsyncSession = Depends(get_session)):
    async with db as session:
        novas_compras = []
        query = select(Cliente).filter(Cliente.id == id)
        resultado = await session.execute(query)
        cliente: Cliente = resultado.scalars().unique().first()
        if cliente:
            for compra in compras:
                novas_compras.append( Venda(
                titulo=compra.titulo,
                descricao=compra.descricao,
                valor=compra.valor,
                data_prevista_pagamento=compra.data_prevista_pagamento
        ))
            cliente.vendas.extend(novas_compras)
            await session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado !")   
        
        await session.commit()
        return compras




     