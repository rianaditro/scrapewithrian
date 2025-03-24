from sqlmodel import Field, SQLModel

class Product(SQLModel, table=True):
    sku: str = Field(default=None, primary_key=True)
    product_name: str
    category: str
    description: str
    price: str
    color: str