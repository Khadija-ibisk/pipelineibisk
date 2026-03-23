import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Generator
from src.datapipeline.logging_config import logger

def load_xml(filepath: str, record_tag: str = "order") -> Generator[dict, None, None]:
    path = Path(filepath)
    logger.info(f"[XML] Lecture : {path.name}")
    tree = ET.parse(path)
    root = tree.getroot()
    records = root.findall(record_tag)
    logger.info(f"[XML] {len(records)} enregistrements")
    for elem in records:
        yield {child.tag: child.text for child in elem}