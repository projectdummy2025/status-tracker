from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from fastapi import HTTPException

router = APIRouter()

@router.post("/", response_model=schemas.StatusResponse)
def create_status(
    payload: schemas.StatusCreate,
    db: Session = Depends(get_db)
):
    new_status = models.Status(
        title=payload.title,
        status=payload.status
    )

    db.add(new_status)
    db.commit()
    db.refresh(new_status)

    return new_status

@router.get("/{status_id}", response_model=schemas.StatusResponse)
def get_status(
    status_id: int,
    db: Session = Depends(get_db)
):
    status = db.query(models.Status).filter(models.Status.id == status_id).first()
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status