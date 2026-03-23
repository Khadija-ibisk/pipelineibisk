import pandas as pd
from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger

def load_excel(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[EXCEL] Lecture : {path.name}")
    df = pd.read_excel(path, engine="openpyxl")
    logger.info(f"[EXCEL] {len(df)} lignes lues")
    for _, row in df.iterrows():
        yield row.to_dict()