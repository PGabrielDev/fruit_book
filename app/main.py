from  fastapi import FastAPI

from core.configs import settings
from routes.router import api_router

app = FastAPI(title="Fruits API")
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3001, log_level='info', reload=True)