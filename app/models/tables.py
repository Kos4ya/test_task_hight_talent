from base import Base

from sqlalchemy import Column, String, Integer


class Table(Base):
    __tablename__ = 'tables'
    name = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
