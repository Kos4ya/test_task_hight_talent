from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from .base_model import Base


class Reservation(Base):
    __tablename__ = "reservations"

    customer_name = Column(String, nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    reservation_time = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, nullable=False)