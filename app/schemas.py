from pydantic import BaseModel

class StatusCreate(BaseModel):
    title: str
    status: str

class StatusResponse(StatusCreate):
    id: int

    class Config:
        from_attributes = True
