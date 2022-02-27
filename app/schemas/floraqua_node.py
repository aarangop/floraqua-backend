import uuid
from pydantic import BaseModel, Field


class FloraquaNode(BaseModel):
    id: uuid.UUID
    name: str
    plant_name: str
    target_moisture: int = Field(gt=0, le=100)
