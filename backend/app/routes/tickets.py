from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from ai_engine import analyze_ticket

router = APIRouter(prefix="/tickets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_ticket(title: str, description: str, db: Session = Depends(get_db)):
    ai_result = analyze_ticket(description)

    ticket = models.Ticket(
        title=title,
        description=description,
        status="Assigned",
        department=ai_result.get("department")
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {"ticket": ticket, "ai": ai_result}

@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(models.Ticket).all()
