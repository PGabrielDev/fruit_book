from click import echo
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
                                        autocommit=False,
                                        autoflush=False,
                                        expire_on_commit=False,
                                        echo=True,
                                        class_=AsyncSession, 
                                        bind=engine
                                    )