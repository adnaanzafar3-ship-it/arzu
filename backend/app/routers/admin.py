from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import User, College, Course, Scholarship, Exam, Enquiry, Review
from ..security import admin_user

router = APIRouter(prefix="/api/v1/admin", tags=["Admin"])

@router.get("/dashboard", dependencies=[Depends(admin_user)])
def dashboard(db: Session = Depends(get_db)):
    return {
        "users": db.query(func.count(User.id)).scalar(),
        "colleges": db.query(func.count(College.id)).scalar(),
        "courses": db.query(func.count(Course.id)).scalar(),
        "scholarships": db.query(func.count(Scholarship.id)).scalar(),
        "exams": db.query(func.count(Exam.id)).scalar(),
        "leads": db.query(func.count(Enquiry.id)).scalar(),
        "reviews": db.query(func.count(Review.id)).scalar(),
    }
