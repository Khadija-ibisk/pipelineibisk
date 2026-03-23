from pydantic import ValidationError as PydanticValidationError
from src.datapipeline.validation.models import Order
from src.datapipeline.logging_config import logger
from typing import Optional

def validate_order(data: dict) -> tuple[Optional[Order], Optional[str]]:
    try:
        order = Order(**data)
        return order, None
    except PydanticValidationError as e:
        error_msg = str(e)
        logger.warning(f"[VALIDATION] Rejeté — {data.get('order_id','?')} : {error_msg}")
        return None, error_msg