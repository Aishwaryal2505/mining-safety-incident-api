from pydantic import BaseModel
from datetime import date
from typing import Optional


class IncidentCreate(BaseModel):
    site: str
    incident_type: str
    severity: str
    description: Optional[str] = None
    date_reported: date


class IncidentUpdate(BaseModel):
    status: str


class IncidentResponse(BaseModel):
    id: int
    site: str
    incident_type: str
    severity: str
    description: Optional[str] = None
    date_reported: date
    status: str

    class Config:
        from_attributes = True