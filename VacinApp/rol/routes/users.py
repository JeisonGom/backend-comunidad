from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from comunidad.database import get_db
from roles.models.user import UserDB
from roles.security import hash_password, verify_password

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # 🔍 Validar el rol antes de procesar el registro
    if user.role not in ["admin", "vecino"]:
        raise HTTPException(status_code=400, detail="Rol inválido. Debe ser 'admin' o 'vecino'.")

    #hashear la contraseña antes de guardarla en la base de datos
    hashed_password = hash_password(user.password)

    new_user = UserDB(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role,
        community_id=getattr(user, "community_id", None)  
)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuario registrado correctamente", "user": user.username}
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    return {"message": "Inicio de sesión exitoso", "user": user.username, "role": user.role}