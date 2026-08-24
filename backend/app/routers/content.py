from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Course, Scholarship, Exam, MockTest, Question
from ..schemas import CourseIn
from ..security import admin_user

router = APIRouter(prefix="/api/v1", tags=["Content"])

def slugify(s):
    return "-".join("".join(c.lower() if c.isalnum() else " " for c in s).split())

@router.get("/courses")
def courses(db: Session = Depends(get_db)):
    return db.query(Course).order_by(Course.name).all()

@router.get("/courses/{slug}")
def course(slug: str, db: Session = Depends(get_db)):
    item = db.query(Course).filter(Course.slug == slug).first()
    if not item: raise HTTPException(404, "Course not found")
    return item

@router.post("/courses", dependencies=[Depends(admin_user)])
def create_course(data: CourseIn, db: Session = Depends(get_db)):
    item = Course(**data.model_dump(), slug=slugify(data.name))
    db.add(item); db.commit(); db.refresh(item)
    return item

@router.get("/scholarships")
def scholarships(db: Session = Depends(get_db)):
    return db.query(Scholarship).order_by(Scholarship.name).all()

@router.get("/exams")
def exams(db: Session = Depends(get_db)):
    return db.query(Exam).order_by(Exam.name).all()

@router.get("/mock-tests")
def mock_tests(db: Session = Depends(get_db)):
    return db.query(MockTest).order_by(MockTest.title).all()

@router.get("/mock-tests/{test_id}")
def mock_test(test_id: int, db: Session = Depends(get_db)):
    test = db.get(MockTest, test_id)
    if not test: raise HTTPException(404, "Test not found")
    qs = db.query(Question).filter(Question.test_id == test_id).all()
    return {"test": test, "questions": qs}
