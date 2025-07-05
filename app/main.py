from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import routes
from app.db import supabase


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(routes.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/supabase")
async def test_supabase():
    response = supabase.table("locations").select("*").execute()
    
    print(response)
    return {"data": response.data}
