from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.vendas import Venda
from schemas.venda_schema import VendaSchema
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=VendaSchema)
async def salvar_fruit_venda(venda: VendaSchema, db: AsyncSession =  Depends(get_session)):
    fruit_venda = Venda(
        titulo=venda.titulo,
        descricao=venda.descricao,
        valor=venda.valor,
        data_prevista_pagamento=venda.data_prevista_pagamento

        )
    db.add(fruit_venda)
    await db.commit()
    return fruit_venda

@router.get('/', response_model=List[VendaSchema])
async def get_vendas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Venda)
        resultado =  await session.execute(query)
        vendas = resultado.scalars().all()
        return vendas

@router.get('/{id}', response_model=VendaSchema)
async def get_venda(id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = session(Venda).filter(Venda.id == id)
        resultado = await session.execute(query)
        venda = resultado.scalar_one_or_none()

        if venda:
            return venda
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venda nao encontrada !")