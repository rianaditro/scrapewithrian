from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import JSONResponse
from sqlmodel import select, Session

from api.models.products import Product
from api.db.deps import get_db


router = APIRouter()

@router.get("/products", response_model=dict)
async def get_products(
    request: Request,
    page: int = Query(1, ge=1, description="Page number (min: 1)"),
    session: Session = Depends(get_db)
):
    """Fetch paginated products with total count from state."""
    
    page_size = 20  # Fixed number of items per page
    offset = (page - 1) * page_size

    # Get total products count from app state
    total_products = request.app.state.product_count
    total_pages = (total_products + page_size - 1) // page_size

    # Check if page is out of range
    if page > total_pages:
        return JSONResponse(status_code=404, content={"message": "Page not found"})

    # Query paginated products
    statement = select(Product).offset(offset).limit(page_size)
    results = session.exec(statement)
    products = results.all()  

    return {
        "page": page,
        "page_size": page_size,
        "total_products": total_products,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
        "products": products
    }
