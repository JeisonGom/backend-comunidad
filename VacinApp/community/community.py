from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from comunidad.database import SessionLocal  
from .models import CommunityDB
from pydantic import BaseModel
from datetime import datetime  

router = APIRouter()

# Modelo de validación para recibir datos
class Community(BaseModel):
    name: str
    location: str
    creator_id: int

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/community/create")
def create_community(community: Community, db: Session = Depends(get_db)):
    """Crea una nueva comunidad en la base de datos"""
    new_community = CommunityDB(
        name=community.name,
        location=community.location,
        created_at=datetime.utcnow(),  
        creator_id=community.creator_id
    )
    db.add(new_community)
    db.commit()
    db.refresh(new_community)
    
    return {"message": "Comunidad creada exitosamente", "community": new_community}


