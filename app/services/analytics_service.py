import pandas as pd
from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.models.product import Product

def get_revenue(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return {'total_revenue': 0}
    
    df = pd.DataFrame([{'product_id': s.product_id, 'quantity': s.quantity, 'date': s.date} for s in sales])
    products = db.query(Product).all()
    df_products = pd.DataFrame([{'id': p.id, 'price': p.price} for p in products])

    df = df.merge(df_products, left_on='product_id', right_on='id')
    df['revenue'] = df['quantity'] * df['price']

    return {'total_revenue': df['revenue'].sum()}

def get_top_products(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return []

    products = db.query(Product).all()

    df = pd.DataFrame([{
        "product_id": s.product_id,
        "quantity": s.quantity
    } for s in sales])

    df_products = pd.DataFrame([{
        "id": p.id,
        "name": p.name
    } for p in products])

    df = df.merge(df_products, left_on="product_id", right_on="id")
    top = df.groupby("name")["quantity"].sum().reset_index()
    top = top.sort_values("quantity", ascending=False)

    return top.to_dict(orient="records")

def get_daily_sales(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return []

    df = pd.DataFrame([{
        "date": s.date,
        "quantity": s.quantity
    } for s in sales])

    df["date"] = pd.to_datetime(df["date"]).dt.date
    daily = df.groupby("date")["quantity"].sum().reset_index()

    return daily.to_dict(orient="records")

def get_average_ticket(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return {"average_ticket": 0}

    products = db.query(Product).all()

    df = pd.DataFrame([{
        "product_id": s.product_id,
        "quantity": s.quantity
    } for s in sales])

    df_products = pd.DataFrame([{
        "id": p.id,
        "price": p.price
    } for p in products])

    df = df.merge(df_products, left_on="product_id", right_on="id")
    df["revenue"] = df["quantity"] * df["price"]

    return {"average_ticket": df["revenue"].mean()}