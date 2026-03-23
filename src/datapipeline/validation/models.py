from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date, datetime

class Order(BaseModel):
    order_id: str
    customer_name: str
    country: Optional[str] = None
    product: Optional[str] = None
    quantity: int
    price: float
    order_date: Optional[date] = None
    source_type: str = "unknown"
    ingestion_timestamp: datetime = datetime.now()

    @field_validator("order_id")
    def order_id_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("order_id est obligatoire")
        return v

    @field_validator("customer_name")
    def customer_name_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("customer_name ne peut pas être vide")
        return v

    @field_validator("quantity")
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError("quantity doit être > 0")
        return v

    @field_validator("price")
    def price_non_negative(cls, v):
        if v < 0:
            raise ValueError("price doit être >= 0")
        return v