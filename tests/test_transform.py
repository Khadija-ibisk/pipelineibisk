from src.datapipeline.transform.normalize import normalize_order

def test_normalize_csv_format():
    raw = {
        "order_id": "ORD001",
        "customer_name": "Alice",
        "country": "France",
        "product": "Laptop",
        "quantity": "1",
        "price": "999.99",
        "order_date": "2024-01-15"
    }
    result = normalize_order(raw, source_type="csv")
    assert result["order_id"] == "ORD001"
    assert result["quantity"] == 1
    assert result["price"] == 999.99
    assert result["source_type"] == "csv"

def test_normalize_json_different_keys():
    raw = {
        "id": "ORD010",
        "client": "Emma",
        "pays": "UK",
        "article": "Headphones",
        "qte": "2",
        "montant": "120.0"
    }
    result = normalize_order(raw, source_type="json")
    assert result["order_id"] == "ORD010"
    assert result["customer_name"] == "Emma"
    assert result["country"] == "UK"
    assert result["quantity"] == 2

def test_normalize_invalid_date():
    raw = {
        "order_id": "ORD001",
        "customer_name": "Alice",
        "quantity": "1",
        "price": "10.0",
        "order_date": "pas-une-date"
    }
    result = normalize_order(raw, source_type="csv")
    assert result["order_date"] is None

def test_normalize_missing_fields():
    raw = {
        "order_id": "ORD099",
        "customer_name": "Test"
    }
    result = normalize_order(raw, source_type="csv")
    assert result["quantity"] == 0
    assert result["price"] == 0.0