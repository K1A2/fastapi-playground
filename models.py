from sqlalchemy import Column, String, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, DATE, DATETIME, TINYINT
from sqlalchemy.orm import relationship
from datetime import datetime
from database.mariadb_session import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(String(64), primary_key=True, nullable=False)
    email = Column(String(255), nullable=False)
    provider = Column(String(40), nullable=False)
    username = Column(String(40), nullable=False)
    is_superuser = Column(TINYINT(1), default=False, nullable=False)
