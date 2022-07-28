from datetime import datetime
from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime,DECIMAL


class Venda(settings.DB_BASE_MODEL):
    __tablename__ = 'tb_venda'

    id: int =  Column(Integer, primary_key=True, autoincrement=True)
    titulo: str =  Column(String(100), nullable=False)
    descricao: str =  Column(String)
    valor: float =  Column(DECIMAL(8,2),nullable=False)
    data_venda: datetime = Column(DateTime, default=datetime.now)
    data_pagamento: datetime = Column(DateTime)
    