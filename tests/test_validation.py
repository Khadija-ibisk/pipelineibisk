from src.datapipeline.validation.validators import validate_order

def test_valid_order():
    data = {
        "order_id": "ORD001",
        "customer_name": "Alice",
        "quantity": 1,
        "price": 99.9,
        "source_type": "csv"
    }
    order, error = validate_order(data)
    assert order is not None
    assert error is None

def test_missing_order_id():
    data = {
        "order_id": "",
        "customer_name": "Alice",
        "quantity": 1,
        "price": 10.0,
        "source_type": "csv"
    }
    order, error = validate_order(data)
    assert order is None
    assert error is not None

def test_empty_customer_name():
    data = {
        "order_id": "ORD002",
        "customer_name": "",
        "quantity": 1,
        "price": 10.0,
        "source_type": "csv"
    }
    order, error = validate_order(data)
    assert order is None

def test_negative_quantity():
    data = {
        "order_id": "ORD003",
        "customer_name": "Bob",
        "quantity": -5,
        "price": 10.0,
        "source_type": "json"
    }
    order, error = validate_order(data)
    assert order is None

def test_negative_price():
    data = {
        "order_id": "ORD004",
        "customer_name": "Carol",
        "quantity": 2,
        "price": -1.0,
        "source_type": "csv"
    }
    order, error = validate_order(data)
    assert order is None

def test_valid_order_with_country():
    data = {
        "order_id": "ORD005",
        "customer_name": "David",
        "country": "France",
        "quantity": 3,
        "price": 50.0,
        "source_type": "csv"
    }
    order, error = validate_order(data)
    assert order is not None
    assert order.country == "France"