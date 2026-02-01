from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_status():
    return {"message": "halo status"}
