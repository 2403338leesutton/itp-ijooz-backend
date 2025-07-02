from fastapi import APIRouter

router = APIRouter()

@router.get("/api/route")
async def get_route():
    """
    Example endpoint to get a route.
    Replace with actual logic as needed.
    """
    return {"route": "Stop A -> Stop B -> Stop C"}