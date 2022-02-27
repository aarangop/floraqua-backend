from fastapi import FastAPI

from app.db import db
from app.config import get_config


from app.routes.nodes import router as nodes_router

app = FastAPI(title="Floraqua API", prefix="/api")
app.include_router(nodes_router)


@app.on_event("startup")
async def startup():
    config = get_config()
    await db.connect_to_database(path=config.db_path, db_name=config.db_name)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="info")
