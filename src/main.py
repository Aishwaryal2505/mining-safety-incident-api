from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from src.database import get_db, engine, Base
from src import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mining Safety Incident Tracker")


@app.post("/incidents", response_model=schemas.IncidentResponse)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    new_incident = models.Incident(**incident.model_dump())
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident


@app.get("/incidents", response_model=List[schemas.IncidentResponse])
def list_incidents(
    site: Optional[str] = None,
    severity: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.Incident)
    if site:
        query = query.filter(models.Incident.site == site)
    if severity:
        query = query.filter(models.Incident.severity == severity)
    return query.all()


@app.get("/incidents/{incident_id}", response_model=schemas.IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident


@app.put("/incidents/{incident_id}", response_model=schemas.IncidentResponse)
def update_incident(incident_id: int, update: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    incident.status = update.status
    db.commit()
    db.refresh(incident)
    return incident


@app.delete("/incidents/{incident_id}")
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    db.delete(incident)
    db.commit()
    return {"message": f"Incident {incident_id} deleted"}