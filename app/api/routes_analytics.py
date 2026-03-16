from fastapi import APIRouter, Depends, Query

from datetime import datetime
from app.database.session import db_dependency
from app.services import analytics_service
from app.services.auth_service import get_current_user

router = APIRouter(tags=["Analytics"], dependencies=[Depends(get_current_user)])

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

@router.get("/analytics/revenue-by-period")
def get_revenue_by_period(
    db: db_dependency,
    start_date: datetime = Query(example="2026-01-01T00:00:00"),
    end_date: datetime = Query(example="2026-03-01T00:00:00")
):
    return analytics_service.get_revenue_by_period(db, start_date, end_date)

@router.get("/analytics/trend")
def get_trend(
    db: db_dependency,
    months: int = Query(default=3, example=3)
):
    return analytics_service.get_trend(db, months)