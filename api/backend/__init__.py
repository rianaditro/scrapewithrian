from fastapi import FastAPI
from api.backend.routers import home

app = FastAPI()

# Register routers
app.include_router(home.router)
