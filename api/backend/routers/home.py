from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_home():
    return "<h1>Welcome to scrapewithrian Homepage</h1>"
