from fastapi import APIRouter
from app.database.session import db_dependency
from app.services import analytics_service

router = APIRouter()

@router.get("/analytics/revenue")
def get_revenue(db: db_dependency):
    return analytics_service.get_revenue(db)

@router.get("/analytics/top-products")
def get_top_products(db: db_dependency):
    return analytics_service.get_top_products(db)

@router.get("/analytics/daily-sales")
def get_daily_sales(db: db_dependency):
    return analytics_service.get_daily_sales(db)

@router.get("/analytics/average-ticket")
def get_average_ticket(db: db_dependency):
    return analytics_service.get_average_ticket(db)