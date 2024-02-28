import fastapi
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
import os 

import logging
from app.util.logger import configure_logger

logger:logging = configure_logger("monitor")


@asynccontextmanager
async def lifespan(app:fastapi.FastAPI):

    global database_engine, SessionLocal

    # # 데이터베이스 연결 설정
    # database_engine = create_engine("sqlite:///:memory:")
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database_engine)

    print("FastAPI application is starting up!")

    logger.info('lifespan start')
    logger.info('run env ::: ' + str(os.getenv('ENV', 'no env selected')))

    yield

app = fastapi.FastAPI(lifespan=lifespan)
from app.routes import home, images, nginx

app.include_router(home.router)
app.include_router(images.router)
app.include_router(nginx.router)


# Define CORS configurations
origins = [
    "http://localhost",  # Allow requests from this origin
    "http://localhost:8000",  # Allow requests from this origin and port
    "https://example.com",  # Allow requests from this specific domain
    "https://*.example.com",  # Allow requests from any subdomain of example.com
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can specify specific HTTP headers
)