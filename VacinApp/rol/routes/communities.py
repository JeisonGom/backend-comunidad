from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from comunidad.database import get_db
from roles.models.community import CommunityDB
from roles.models.user import UserDB

router = APIRouter()

class CommunityJoin(BaseModel):
    user_id: int
    community_code: str | None = None
    community_name: str | None = None

@router.post("/community/join")
def join_community(data: CommunityJoin, db: Session = Depends(get_db)):
    """Permite a un usuario unirse a una comunidad usando código o nombre"""

    # validar que se envíe al menos un método de búsqueda
    if not data.community_code and not data.community_name:
        raise HTTPException(status_code=400, detail="Debes proporcionar un código o nombre de comunidad.")

    # buscar comunidad por código o nombre
    community = None
    if data.community_code:
        community = db.query(CommunityDB).filter(CommunityDB.code == data.community_code).first()
    elif data.community_name:
        community = db.query(CommunityDB).filter(CommunityDB.name.ilike(f"%{data.community_name}%")).first()

    # validar si la comunidad existe
    if not community:
        raise HTTPException(status_code=404, detail="Comunidad no encontrada.")

    # verificar si el usuario existe
    user = db.query(UserDB).filter(UserDB.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    # agregar el usuario a la comunidad
    user.community_id = community.id
    db.commit()
    db.refresh(user)

    return {"message": "Usuario unido a la comunidad", "community": community.name}