from fastapi import APIRouter
from routes import router_venda

api_router = APIRouter()
api_router.include_router(router_venda.router, prefix='/vendas', tags=["vendas"])