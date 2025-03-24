from fastapi import FastAPI
from api.backend.routers import home
from api.backend.routers import simple_table

app = FastAPI()

# Register routers
app.include_router(home.router)
app.include_router(simple_table.router)
