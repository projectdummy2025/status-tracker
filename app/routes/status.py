from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

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
