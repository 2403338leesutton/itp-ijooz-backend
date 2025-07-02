from fastapi import FastAPI
from app.routers import routes

app = FastAPI()

app.include_router(routes.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}