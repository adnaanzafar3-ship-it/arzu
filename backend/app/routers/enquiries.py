from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Enquiry
from ..schemas import EnquiryIn
from ..security import admin_user

router = APIRouter(prefix="/api/v1/enquiries", tags=["Enquiries"])

@router.post("")
def create_enquiry(data: EnquiryIn, db: Session = Depends(get_db)):
    item = Enquiry(**data.model_dump())
    item.lead_code = f"LEAD{(db.query(Enquiry).count()+1):06d}"
    db.add(item); db.commit(); db.refresh(item)
    return {"message":"Thank you. Our counsellor will contact you.", "lead_id": item.lead_code}

@router.get("", dependencies=[Depends(admin_user)])
def enquiries(db: Session = Depends(get_db)):
    return db.query(Enquiry).order_by(Enquiry.created_at.desc()).limit(500).all()
