import tempfile
import json
import os
from src.datapipeline.ingestion.json_loader import load_json

def test_load_json_list():
    data = [{"id": "ORD001", "client": "Alice"}, {"id": "ORD002", "client": "Bob"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        fname = f.name
    rows = list(load_json(fname))
    os.unlink(fname)
    assert len(rows) == 2
    assert rows[0]["client"] == "Alice"

def test_load_json_single_object():
    data = {"id": "ORD001", "client": "Alice"}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        fname = f.name
    rows = list(load_json(fname))
    os.unlink(fname)
    assert len(rows) == 1

def test_load_json_content():
    data = [{"id": "ORD010", "montant": 120.0}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        fname = f.name
    rows = list(load_json(fname))
    os.unlink(fname)
    assert rows[0]["montant"] == 120.0