import zipfile
import tempfile
import os
from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger

def load_archive(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[ZIP] Extraction : {path.name}")
    with zipfile.ZipFile(path, "r") as z:
        with tempfile.TemporaryDirectory() as tmpdir:
            z.extractall(tmpdir)
            for filename in z.namelist():
                extracted_path = os.path.join(tmpdir, filename)
                logger.info(f"[ZIP] Fichier extrait : {filename}")
                from src.datapipeline.ingestion.detector import detect_and_load
                yield from detect_and_load(extracted_path)