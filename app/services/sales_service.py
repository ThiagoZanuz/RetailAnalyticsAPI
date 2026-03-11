import pandas as pd
from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.models.product import Product
from datetime import datetime

def process_csv(file, db: Session):
    df = pd.read_csv(file)

    results = []
    for _, row in df.iterrows():
        product = db.query(Product).filter(Product.name == row["product"]).first()
        if not product:
            continue

        sale = Sale(
            product_id=product.id,
            quantity=int(row["quantity"]),
            date=datetime.strptime(str(row["date"]), "%Y-%m-%d")
        )
        db.add(sale)
        results.append(sale)

    db.commit()
    return {"sales_imported": len(results)}