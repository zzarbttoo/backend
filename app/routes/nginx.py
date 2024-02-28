from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/test", description="""nginx router""")
async def nginx_ping():
    return True
