from fastapi import FastAPI, HTTPException
from src.datapipeline.analytics import reports
from src.datapipeline.logging_config import logger

app = FastAPI(
    title="PipelineIbisk API",
    description="API de consultation des métriques data",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "pipelineibisk"}

@app.get("/metrics/revenue-by-country")
def get_revenue_by_country():
    try:
        data = reports.revenue_by_country()
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        logger.error(f"[API] {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics/revenue-by-product")
def get_revenue_by_product():
    try:
        data = reports.revenue_by_product()
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics/top-customers")
def get_top_customers(limit: int = 10):
    try:
        data = reports.top_customers(limit=limit)
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics/revenue-over-time")
def get_revenue_over_time():
    try:
        data = reports.revenue_over_time()
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))