import json
from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger

def load_json(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[JSON] Lecture : {path.name}")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        logger.info(f"[JSON] {len(data)} enregistrements")
        for item in data:
            yield item
    else:
        yield data

def load_ndjson(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[NDJSON] Lecture : {path.name}")
    count = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)
                count += 1
    logger.info(f"[NDJSON] {count} lignes lues")