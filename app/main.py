import fastapi

from contextlib import asynccontextmanager
import os 

import logging
from app.util.logger import configure_logger

logger:logging = configure_logger("monitor")

@asynccontextmanager
async def lifespan(app:fastapi.FastAPI):
    logger.info('lifespan start')
    logger.info('run env ::: ' + str(os.getenv('ENV', 'no env selected')))
    yield

app = fastapi.FastAPI(lifespan=lifespan)

from app.routes import home, images, nginx

app.include_router(home.router)
app.include_router(images.router)
app.include_router(nginx.router)


