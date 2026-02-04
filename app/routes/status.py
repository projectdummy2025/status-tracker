from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import List
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

@router.get("/", response_model=List[schemas.StatusResponse]) # 👈 Response adalah list
def get_all_statuses(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    statuses = db.query(models.Status).offset(skip).limit(limit).all()
    return statuses

@router.put("/{status_id}", response_model=schemas.StatusResponse)
def update_status(
    status_id: int,
    payload: schemas.StatusCreate,
    db: Session = Depends(get_db)
):
    status_query = db.query(models.Status).filter(models.Status.id == status_id)
    db_status = status_query.first()
    if not db_status:
        raise HTTPException(status_code=404, detail="Status not found")

    update_data = payload.model_dump(exclude_unset=True)
    status_query.update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(db_status)

    return db_status