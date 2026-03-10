from fastapi import FastAPI
from app.api import routes_products, routes_sales
from app.database.session import Base
from app.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes_products.router)
app.include_router(routes_sales.router)