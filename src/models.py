from sqlalchemy import Column, Integer, String, Date
from src.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    site = Column(String, nullable=False)
    incident_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date_reported = Column(Date, nullable=False)
    status = Column(String, default="open")