from fastapi import APIRouter
from .home import router as home_router
from .simple_table import router as simple_table_router
# from .student import router as student_router
# from .teacher import router as teacher_router

router = APIRouter()

router.include_router(home_router, tags=["Home"])
router.include_router(simple_table_router, tags=["Simple Table"])
# router.include_router(student_router, prefix="/students", tags=["Students"])
# router.include_router(teacher_router, prefix="/teachers", tags=["Teachers"])
