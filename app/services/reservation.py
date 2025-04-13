from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_, func

from ..models.reservations import Reservation
from ..schemas.reservation import ReservationCreate


def check_table_availability(db: Session, table_id: int, reservation_time: datetime, duration_minutes: int):
    end_time = reservation_time + timedelta(minutes=duration_minutes)

    conflicting_reservations = db.query(Reservation).filter(
        and_(
            Reservation.table_id == table_id,
            Reservation.reservation_time < end_time,
            func.make_interval(0, 0, 0, 0, 0,
                               Reservation.duration_minutes) + Reservation.reservation_time > reservation_time)
    ).count()

    return not conflicting_reservations


def create_reservation(db: Session, reservation: ReservationCreate):
    if not check_table_availability(db, reservation.table_id, reservation.reservation_time,
                                    reservation.duration_minutes):
        raise ValueError("Table is already booked for this time slot")

    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reservation).offset(skip).limit(limit).all()


def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation:
        db.delete(db_reservation)
        db.commit()
        return True
    return False
