
from core.configs import Settings
from core.db import engine

async def  create_tables() -> None:
    import models.__all_models
    print("Criando tabelas no banco...")
    async with engine.begin() as conn:
        await conn.run_sync(Settings.DB_BASE_MODEL.metadata.drop_all)
        await conn.run_sync(Settings.DB_BASE_MODEL.metadata.create_all)


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())