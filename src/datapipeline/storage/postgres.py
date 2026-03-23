import psycopg2
from src.datapipeline import config
from src.datapipeline.logging_config import logger
from src.datapipeline.exceptions import DatabaseError

def get_connection():
    try:
        conn = psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
        )
        return conn
    except Exception as e:
        logger.error(f"[DB] Échec connexion : {e}")
        raise DatabaseError(str(e))

def insert_order(conn, order) -> bool:
    sql = """
        INSERT INTO orders
        (order_id, customer_name, country, product, quantity, price, order_date, source_type, ingestion_timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING;
    """
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (
                order.order_id, order.customer_name, order.country,
                order.product, order.quantity, order.price,
                order.order_date, order.source_type, order.ingestion_timestamp
            ))
        conn.commit()
        logger.info(f"[DB] Inséré : {order.order_id}")
        return True
    except Exception as e:
        conn.rollback()
        logger.error(f"[DB] Erreur insertion {order.order_id} : {e}")
        return False

def insert_error(conn, raw_data: str, error_msg: str, source_file: str):
    sql = """
        INSERT INTO ingestion_errors (raw_data, error_message, source_file)
        VALUES (%s, %s, %s);
    """
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (str(raw_data)[:500], error_msg, source_file))
        conn.commit()
    except Exception as e:
        logger.error(f"[DB] Erreur log erreur : {e}")