from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
from pydantic import BaseModel
from datetime import datetime
import os

load_dotenv()

app = FastAPI()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class Sale(BaseModel):
    platform: str
    amount: float
    product_category: str

@app.get("/health")
def health():
    return {"status": "moneybuddy is alive!"}

@app.post("/sales")
def log_sale(sale: Sale):
    data = supabase.table("sales").insert({
        "platform": sale.platform,
        "amount": sale.amount,
        "product_category": sale.product_category,
    }).execute()
    return {"message": "Sale logged successfully", "data": data.data}

@app.get("/analytics")
def get_analytics():
    data = supabase.table("sales").select("*").execute()
    sales = data.data

    total_amount = sum(s["amount"] for s in sales)
    total_orders = len(sales)

    breakdown = {}
    for s in sales:
        platform = s["platform"]
        breakdown[platform] = breakdown.get(platform, 0) + s["amount"]

    return {
        "total_amount": total_amount,
        "total_orders": total_orders,
        "breakdown_by_platform": breakdown
    }