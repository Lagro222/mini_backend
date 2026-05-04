from  sqlalchemy.engine import create_engine , make_url 
from sqlalchemy.orm import sessionmaker , DeclarativeBase
from dotenv import load_dotenv

import  os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

url = make_url(DATABASE_URL)

engine = create_engine(url)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
