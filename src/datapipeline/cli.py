import concurrent.futures
from pathlib import Path
from src.datapipeline.logging_config import logger
from src.datapipeline.ingestion.detector import detect_and_load
from src.datapipeline.transform.normalize import normalize_order
from src.datapipeline.validation.validators import validate_order
from src.datapipeline.storage.postgres import get_connection, insert_order, insert_error
from src.datapipeline import config

def process_file(filepath: str):
    filename = Path(filepath).name
    source_type = Path(filepath).suffix.lstrip(".")
    logger.info(f"--- Début : {filename} ---")

    conn = get_connection()
    total = valid = rejected = inserted = 0

    try:
        for raw in detect_and_load(filepath):
            total += 1
            normalized = normalize_order(raw, source_type=source_type)
            order, error = validate_order(normalized)

            if order:
                valid += 1
                if insert_order(conn, order):
                    inserted += 1
            else:
                rejected += 1
                insert_error(conn, raw, error, filename)
    finally:
        conn.close()

    logger.info(f"[{filename}] {total} lues | {valid} valides | {rejected} rejetées | {inserted} insérées")
    return {"file": filename, "total": total, "valid": valid, "rejected": rejected, "inserted": inserted}

def run_pipeline(data_dir: str = None):
    data_dir = data_dir or config.DATA_RAW_DIR
    files = [str(p) for p in Path(data_dir).iterdir() if p.is_file()]
    logger.info(f"[PIPELINE] {len(files)} fichier(s) trouvé(s)")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(process_file, f): f for f in files}
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                logger.error(f"[PIPELINE] Erreur : {e}")

    logger.info("--- Pipeline terminé ---")
    return results

if __name__ == "__main__":
    run_pipeline()