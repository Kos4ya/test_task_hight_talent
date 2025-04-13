from sqlalchemy.orm import Session

from ..models.tables import Table
from ..schemas.table import TableCreate


def get_table(db: Session, table_id: int):
    return db.query(Table).filter(Table.id == table_id).first()


def get_tables(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Table).offset(skip).limit(limit).all()


def create_table(db: Session, table: TableCreate):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_id: int):
    db_table = db.query(Table).filter(Table.id == table_id).first()
    if db_table:
        db.delete(db_table)
        db.commit()
        return True
    return False
