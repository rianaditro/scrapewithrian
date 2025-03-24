from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.models.products import Product
from api.db.deps import get_db

router = APIRouter()

@router.get("/table")
async def get_products(skip: int = 0, limit: int = 25, session: Session = Depends(get_db)):
    # Query the database using SQLModel's select() method
    statement = select(Product).offset(skip).limit(limit)
    results = session.exec(statement)
    products = results.all()  # Get all rows
    return {"products": products}