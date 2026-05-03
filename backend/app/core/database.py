from  sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
from sqlalchemy.orm import sessionmaker , DeclarativeBase
from dotenv import load_dotenv
import  os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = DATABASE_URL.replace("postgresql://","postgresql+asyncpg")

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionlocal = sessionmaker(
        engine,
        class= AsyncSession,
        expire_on_commit=False
    )
class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionlocal() as session:
        try:
            yield session
            await session.commit()
        except Exception :
            await session.rollback()
            raise
        finally:
            await session.close
            
