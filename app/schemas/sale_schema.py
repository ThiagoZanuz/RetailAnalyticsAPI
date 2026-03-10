from pydantic import BaseModel
from datetime import datetime

class SaleCreate(BaseModel):
    product_id: int
    quantity: int

class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    date: datetime
    created_at: datetime

    class Config:
        from_attributes = True