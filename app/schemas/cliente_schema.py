from typing import Optional, List
from schemas.venda_schema import VendaSchema
from pydantic import BaseModel as SCBaseModel

class ClienteSchama(SCBaseModel):
    id: Optional[int] 
    nome: str 
    contato: str
    endereco: str 
    vendas: Optional[List[VendaSchema]]
