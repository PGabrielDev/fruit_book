from datetime import datetime
from typing import Optional, List
from colorama import Fore
from core.configs import settings
from models.vendas import Venda
from sqlalchemy import Column, Integer, String, Table, ForeignKey
import sqlalchemy.orm as orm


vendas_clientes = Table(
    'tb_venda_cliente',
    settings.DB_BASE_MODEL.metadata,
    Column('id_cliente', Integer, ForeignKey('tb_cliente.id')),
    Column('id_venda', Integer, ForeignKey('tb_venda.id'))
)


class Cliente(settings.DB_BASE_MODEL):
    __tablename__ :str = 'tb_cliente'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String, nullable=False)
    contato: str = Column(String(50), unique=True)
    endereco: str = Column(String(100))
    vendas:   Optional[List[Venda]] = orm.relationship('Venda', secondary=vendas_clientes,  lazy='joined')
