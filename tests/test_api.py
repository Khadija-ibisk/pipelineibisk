from fastapi.testclient import TestClient
from unittest.mock import patch
from src.datapipeline.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health_service_name():
    response = client.get("/health")
    assert response.json()["service"] == "pipelineibisk"

@patch("src.datapipeline.api.main.reports.revenue_by_country",
       return_value=[{"country": "France", "total_revenue": 500.0}])
def test_revenue_by_country(mock_r):
    response = client.get("/metrics/revenue-by-country")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1

@patch("src.datapipeline.api.main.reports.revenue_by_product",
       return_value=[{"product": "Laptop", "total_revenue": 1999.98}])
def test_revenue_by_product(mock_r):
    response = client.get("/metrics/revenue-by-product")
    assert response.status_code == 200
    assert response.json()["count"] == 1

@patch("src.datapipeline.api.main.reports.top_customers",
       return_value=[{"customer_name": "Alice", "total_spent": 999.99}])
def test_top_customers(mock_r):
    response = client.get("/metrics/top-customers")
    assert response.status_code == 200
    assert response.json()["data"][0]["customer_name"] == "Alice"