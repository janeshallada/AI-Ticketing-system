from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter(prefix="/employees")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_employee(name: str, email: str, department: str, db: Session = Depends(get_db)):
    emp = models.Employee(name=name, email=email, department=department)
    db.add(emp)
    db.commit()
    return emp

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
