from sqlalchemy import Column, Integer, String, ForeignKey
from comunidad.database import Base
from pydantic import BaseModel

#modelo de SQLAlchemy (Base de datos)
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Contraseña hasheada
    role = Column(String, nullable=False)  # "admin" o "vecino"
    community_id = Column(Integer, ForeignKey("communities.id"), nullable=True)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str
    community_id: int | None = None 