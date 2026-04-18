# MoneyBuddy Backend

A sales tracking API for small online vendors built with FastAPI and Supabase.

## The Problem
Small vendors selling on Instagram, Telegram, Snapchat, TikTok, etc., have no visibility 
into which platforms are driving their revenue. This API powers a tool that 
fixes that.

## Stack
- FastAPI
- Supabase (PostgreSQL)
- Python 3
- Deployed on Render

## Endpoints
- `POST /sales` — log a new sale with platform, amount, and product category
- `GET /analytics` — returns total revenue, total orders, and breakdown by platform
- `GET /health` — health check

## Running Locally
```bash
git clone https://github.com/bolanlesadela/moneybuddy_backend
cd moneybuddy_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
