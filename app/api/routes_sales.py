from fastapi import APIRouter, UploadFile, File
from datetime import datetime
from app.database.session import db_dependency
from app.models.sale import Sale
from app.schemas.sale_schema import SaleCreate, SaleResponse
from app.services import sales_service

router = APIRouter()

@router.post('/sales', response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: db_dependency):
    db_sale = Sale(product_id=sale.product_id, quantity=sale.quantity, date=datetime.now())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.get('/sales', response_model=list[SaleResponse])
def get_sales(db: db_dependency):
    return db.query(Sale).all()

@router.post("/sales/upload")
def upload_sales(db: db_dependency, file: UploadFile = File(...)):
    return sales_service.process_csv(file.file, db)