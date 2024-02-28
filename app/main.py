import fastapi
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from contextlib import asynccontextmanager
import os 

import logging
from app.util.logger import configure_logger

logger:logging = configure_logger("monitor")

@asynccontextmanager
async def lifespan(app:fastapi.FastAPI):

    global database_engine, SessionLocal

    # 데이터베이스 연결 설정
    database_engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database_engine)

    print("FastAPI application is starting up!")

    logger.info('lifespan start')
    logger.info('run env ::: ' + str(os.getenv('ENV', 'no env selected')))

    yield

app = fastapi.FastAPI(lifespan=lifespan)

from app.routes import home, images, nginx

app.include_router(home.router)
app.include_router(images.router)
app.include_router(nginx.router)


