import tempfile
import os
from src.datapipeline.ingestion.csv_loader import load_csv

def test_load_csv_basic():
    content = "order_id,customer_name\nORD001,Alice\nORD002,Bob\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write(content)
        fname = f.name
    rows = list(load_csv(fname))
    os.unlink(fname)
    assert len(rows) == 2
    assert rows[0]["order_id"] == "ORD001"

def test_load_csv_empty():
    content = "order_id,customer_name\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write(content)
        fname = f.name
    rows = list(load_csv(fname))
    os.unlink(fname)
    assert rows == []

def test_load_csv_multiple_columns():
    content = "order_id,customer_name,country,price\nORD001,Alice,France,99.9\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write(content)
        fname = f.name
    rows = list(load_csv(fname))
    os.unlink(fname)
    assert rows[0]["country"] == "France"
    assert rows[0]["price"] == "99.9"