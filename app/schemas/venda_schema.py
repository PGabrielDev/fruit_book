from typing import Optional
from datetime import datetime

from pydantic import BaseModel as SCBaseModel

class VendaSchema(SCBaseModel):
    id: Optional[int]
    titulo: str 
    descricao: str 
    valor: float  
    data_venda: datetime 
    data_pagamento: datetime
    data_prevista_pagamento: datetime 

    class Config:
        orm_mode = True