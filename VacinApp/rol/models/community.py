from sqlalchemy import Column, Integer, String, ForeignKey
from comunidad.database import Base

class CommunityDB(Base):
    __tablename__ = "communities"
    __table_args__ = {"extend_existing": True} 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=False)