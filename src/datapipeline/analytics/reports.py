from src.datapipeline.storage.postgres import get_connection
from src.datapipeline.logging_config import logger

def revenue_by_country() -> list[dict]:
    sql = """
        SELECT country, SUM(quantity * price) AS total_revenue
        FROM orders GROUP BY country ORDER BY total_revenue DESC;
    """
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    conn.close()
    return [{"country": r[0], "total_revenue": float(r[1])} for r in rows]

def revenue_by_product() -> list[dict]:
    sql = """
        SELECT product, SUM(quantity * price) AS total_revenue
        FROM orders GROUP BY product ORDER BY total_revenue DESC;
    """
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    conn.close()
    return [{"product": r[0], "total_revenue": float(r[1])} for r in rows]

def top_customers(limit: int = 10) -> list[dict]:
    sql = """
        SELECT customer_name, SUM(quantity * price) AS total_spent
        FROM orders GROUP BY customer_name ORDER BY total_spent DESC LIMIT %s;
    """
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(sql, (limit,))
        rows = cur.fetchall()
    conn.close()
    return [{"customer_name": r[0], "total_spent": float(r[1])} for r in rows]

def revenue_over_time() -> list[dict]:
    sql = """
        SELECT DATE_TRUNC('month', order_date) AS month,
               SUM(quantity * price) AS total_revenue
        FROM orders WHERE order_date IS NOT NULL
        GROUP BY month ORDER BY month;
    """
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    conn.close()
    return [{"month": str(r[0])[:7], "total_revenue": float(r[1])} for r in rows]