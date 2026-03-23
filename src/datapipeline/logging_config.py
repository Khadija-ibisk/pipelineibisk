import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(stream=open(sys.stdout.fileno(), 
                                              mode='w', 
                                              encoding='utf-8', 
                                              closefd=False)),
            logging.FileHandler("pipeline.log", encoding="utf-8"),
        ]
    )
    return logging.getLogger("pipelineibisk")

logger = setup_logging()