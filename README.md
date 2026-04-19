# MoneyBuddy Backend

A sales tracking API for small online vendors built with FastAPI and Supabase.
Log sales by platform and get a breakdown of where your orders are coming from.

## The Problem
Small vendors selling on Instagram, Telegram, Snapchat, TikTok, etc., have no visibility 
into which platforms are driving their revenue. This API powers a tool that 
fixes that.

## Stack
- FastAPI
- Supabase (PostgreSQL)
- Python

## Endpoints
- `GET /health` — check server status
- `POST /sales` — log a sale (platform, amount, product_category)
- `GET /analytics` — get total sales and breakdown by platform

## Running Locally
```bash
pip install fastapi uvicorn supabase python-dotenv
uvicorn main:app --reload
```
