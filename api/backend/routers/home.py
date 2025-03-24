from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_home():
    return {
        "page_title": "Home",
        "page_description": "Collection of all entry points",
        "page_content": {
            "entry_points": [
                {
                    "name": "Simple Table",
                    "path": "/table"
                },
            ]
        }
    }
