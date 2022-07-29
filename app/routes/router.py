from fastapi import APIRouter
from routes import router_venda
from routes import router_cliente
api_router = APIRouter()
api_router.include_router(router_venda.router, prefix='/vendas', tags=["vendas"])
api_router.include_router(router_cliente.router, prefix='/cliente', tags=["clientes | compras"])