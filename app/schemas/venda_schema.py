from typing import Optional
from datetime import datetime

from pydantic import BaseModel as SCBaseModel

class VendaSchema(SCBaseModel):
    id: Optional[int]
    titulo: str 
    descricao: str 
    valor: float  
    data_venda: Optional[datetime] 
    data_pagamento: Optional[datetime]
    data_prevista_pagamento: Optional[datetime] 

    class Config:
        orm_mode = True