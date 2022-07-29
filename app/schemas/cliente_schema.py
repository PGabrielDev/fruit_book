from typing import Optional, List
from models.vendas import Venda
from pydantic import BaseModel as SCBaseModel

class ClienteSchama(SCBaseModel):
    id: Optional[int] 
    nome: str 
    contato: str
    endereco: str 
    vendas: Optional[List[Venda]] 
