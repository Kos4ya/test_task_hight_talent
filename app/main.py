
from fastapi import FastAPI
from .routers import table, reservation
from .db import engine
from .models import base_model


base_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(table.router)
app.include_router(reservation.router)


@app.get("/")
def read_root():
    return {"message": "Restaurant Booking API"}
