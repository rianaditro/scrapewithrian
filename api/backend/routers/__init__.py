from fastapi import APIRouter
from api.backend.routers.home import router as home_router
from api.backend.routers.simple_table import router as simple_table_router
from api.backend.routers.products import router as products_router

router = APIRouter()

router.include_router(home_router, tags=["Home"])
router.include_router(simple_table_router, tags=["Simple Table"])
router.include_router(products_router, tags=["Products"])
