from fastapi import FastAPI
from app.api import routes_products, routes_sales, routes_analytics
from app.database.session import Base
from app.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes_products.router)
app.include_router(routes_sales.router)
app.include_router(routes_analytics.router)