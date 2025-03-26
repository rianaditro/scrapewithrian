from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlalchemy import func

from api.db.session import get_session
from api.models.products import Product
from api.backend import routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Convert session generator to session
    session = next(get_session())

    # Count total data
    statement = select(func.count()).select_from(Product)
    product_count = session.exec(statement).one()

    # Store total data in app state
    app.state.product_count = product_count

    session.close()

    yield # yield control back to FastAPI


app = FastAPI(lifespan=lifespan)
router = routers.router

# Register routers
app.include_router(router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)