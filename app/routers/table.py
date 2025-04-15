from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..schemas.table import Table, TableCreate
from ..services.table import get_tables, create_table, get_table, delete_table

from ..db import get_db

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[Table])
def read_tables(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tables = get_tables(db, skip=skip, limit=limit)
    return tables

@router.post("/", response_model=Table)
def create_new_table(table: TableCreate, db: Session = Depends(get_db)):
    return create_table(db, table=table)

@router.delete("/{table_id}")
def remove_table(table_id: int, db: Session = Depends(get_db)):
    if not delete_table(db, table_id=table_id):
        raise HTTPException(status_code=404, detail="Table not found")
    return {"message": "Table deleted successfully"}