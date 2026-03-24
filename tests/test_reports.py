from unittest.mock import patch, MagicMock
from src.datapipeline.analytics import reports

@patch("src.datapipeline.analytics.reports.get_connection")
def test_revenue_by_country_returns_list(mock_conn):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [("France", 1999.98), ("USA", 76.50)]
    mock_conn.return_value.cursor.return_value.__enter__ = lambda s: mock_cursor
    mock_conn.return_value.cursor.return_value.__exit__ = MagicMock(return_value=False)
    result = reports.revenue_by_country()
    assert isinstance(result, list)

@patch("src.datapipeline.analytics.reports.get_connection")
def test_revenue_by_product_returns_list(mock_conn):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [("Laptop", 2999.97)]
    mock_conn.return_value.cursor.return_value.__enter__ = lambda s: mock_cursor
    mock_conn.return_value.cursor.return_value.__exit__ = MagicMock(return_value=False)
    result = reports.revenue_by_product()
    assert isinstance(result, list)