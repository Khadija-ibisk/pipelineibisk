from datetime import datetime
from typing import Optional

def normalize_order(raw: dict, source_type: str) -> dict:
    order_id = (
        raw.get("order_id") or raw.get("id") or raw.get("order_number") or ""
    ).strip()

    customer_name = (
        raw.get("customer_name") or raw.get("client") or raw.get("customer") or ""
    ).strip()

    country = (
        raw.get("country") or raw.get("pays") or raw.get("nation") or ""
    ).strip()

    product = (
        raw.get("product") or raw.get("article") or raw.get("item") or ""
    ).strip()

    try:
        quantity = int(float(raw.get("quantity") or raw.get("qte") or 0))
    except (ValueError, TypeError):
        quantity = 0

    try:
        price = float(raw.get("price") or raw.get("montant") or raw.get("amount") or 0)
    except (ValueError, TypeError):
        price = 0.0

    order_date = None
    raw_date = raw.get("order_date") or raw.get("date") or raw.get("date_commande")
    if raw_date:
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
            try:
                order_date = datetime.strptime(str(raw_date), fmt).date()
                break
            except ValueError:
                continue

    return {
        "order_id": order_id,
        "customer_name": customer_name,
        "country": country,
        "product": product,
        "quantity": quantity,
        "price": price,
        "order_date": order_date,
        "source_type": source_type,
        "ingestion_timestamp": datetime.now(),
    }