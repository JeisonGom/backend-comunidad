from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from comunidad.database import Base

class CommunityDB(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)