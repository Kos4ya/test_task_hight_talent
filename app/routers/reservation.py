from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..schemas.reservation import Reservation, ReservationCreate
from ..services.reservation import get_reservations, create_reservation, delete_reservation
from ..db import get_db

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[Reservation])
def read_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reservations = get_reservations(db, skip=skip, limit=limit)
    return reservations

@router.post("/", response_model=Reservation)
def create_new_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    try:
        return create_reservation(db, reservation=reservation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{reservation_id}")
def remove_reservation(reservation_id: int, db: Session = Depends(get_db)):
    if not delete_reservation(db, reservation_id=reservation_id):
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {"message": "Reservation deleted successfully"}