from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.queries import add_locations_to_db
from app.preprocessing.parser import parse_raw_data
from app.routers import routes
from app.db.client import supabase


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

@app.put("/locations")
async def locations():
    locations = parse_raw_data()
    response = add_locations_to_db(locations)
    return response
   