from fastapi import APIRouter, Depends
from app.database.session import db_dependency
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.auth_service import get_current_user

router = APIRouter(tags=['Products'],dependencies=[Depends(get_current_user)])

@router.post('/products', response_model=ProductResponse)
def create_product(product: ProductCreate, db: db_dependency):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get('/products', response_model=list[ProductResponse])
def get_products(db: db_dependency):
    return db.query(Product).all()

@router.get('/products/{id}', response_model=ProductResponse)
def get_product(id: int, db: db_dependency):
    return db.query(Product).filter(Product.id == id).first()