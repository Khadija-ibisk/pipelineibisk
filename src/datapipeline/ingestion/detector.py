from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger
from src.datapipeline.exceptions import ParsingError

def detect_and_load(filepath: str) -> Generator[dict, None, None]:
    path = Path(filepath)
    suffix = path.suffix.lower()
    logger.info(f"[DETECTOR] {path.name} -> format : {suffix}")

    if suffix == ".csv":
        from src.datapipeline.ingestion.csv_loader import load_csv
        yield from load_csv(filepath)
    elif suffix == ".json":
        from src.datapipeline.ingestion.json_loader import load_json
        yield from load_json(filepath)
    elif suffix == ".ndjson":
        from src.datapipeline.ingestion.json_loader import load_ndjson
        yield from load_ndjson(filepath)
    elif suffix == ".xml":
        from src.datapipeline.ingestion.xml_loader import load_xml
        yield from load_xml(filepath)
    elif suffix in (".xlsx", ".xls"):
        from src.datapipeline.ingestion.excel_loader import load_excel
        yield from load_excel(filepath)
    elif suffix == ".zip":
        from src.datapipeline.ingestion.archive_loader import load_archive
        yield from load_archive(filepath)
    else:
        raise ParsingError(f"Format non supporte : {suffix}")