import pandas as pd
from pathlib import Path
from src.datapipeline.storage.postgres import get_connection
from src.datapipeline.logging_config import logger
from src.datapipeline import config

def export_to_parquet(output_dir: str = None, partition_by: str = "country"):
    output_dir = output_dir or config.DATA_EXPORTS_DIR
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM orders;", conn)
    conn.close()

    logger.info(f"[PARQUET] {len(df)} lignes à exporter")

    if partition_by and partition_by in df.columns:
        for value, group in df.groupby(partition_by):
            safe_val = str(value).replace(" ", "_")
            filepath = Path(output_dir) / f"orders_{partition_by}_{safe_val}.parquet"
            group.to_parquet(filepath, index=False)
            logger.info(f"[PARQUET] {filepath.name} ({len(group)} lignes)")
    else:
        filepath = Path(output_dir) / "orders.parquet"
        df.to_parquet(filepath, index=False)

    csv_path = Path(output_dir) / "orders_consolidated.csv"
    df.to_csv(csv_path, index=False)
    logger.info(f"[CSV] Export consolidé : {csv_path}")