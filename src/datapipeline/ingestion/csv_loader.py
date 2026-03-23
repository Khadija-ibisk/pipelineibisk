import csv
from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger

def load_csv(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[CSV] Lecture : {path.name}")
    count = 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            count += 1
            yield dict(row)
    logger.info(f"[CSV] {count} lignes lues")