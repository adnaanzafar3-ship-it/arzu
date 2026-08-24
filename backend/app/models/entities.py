
from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True); name=Column(String(120),nullable=False)
    email=Column(String(255),unique=True,index=True); password_hash=Column(String(255))
    role=Column(String(30),default="student",nullable=False); mobile=Column(String(30),unique=True)
    otp_verified=Column(Boolean,default=False); created_at=Column(DateTime,default=datetime.utcnow)
    profile=relationship("StudentProfile",back_populates="user",uselist=False,cascade="all, delete-orphan")
    saved=relationship("SavedCollege",back_populates="user",cascade="all, delete-orphan")

class StudentProfile(Base):
    __tablename__="student_profiles"
    id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey("users.id"),unique=True)
    education=Column(String(255)); course_interest=Column(String(255)); preferred_state=Column(String(100))
    preferred_city=Column(String(100)); budget=Column(Numeric(14,2)); category=Column(String(100))
    user=relationship("User",back_populates="profile")

class College(Base):
    __tablename__="colleges"
    id=Column(Integer,primary_key=True); college_code=Column(String(30),unique=True,index=True)
    name=Column(String(255),nullable=False,index=True); official_name=Column(String(255)); slug=Column(String(255),unique=True,index=True)
    college_type=Column(String(50)); university=Column(String(255)); state=Column(String(100),index=True)
    district=Column(String(100),index=True); city=Column(String(100),index=True); address=Column(Text); pincode=Column(String(20))
    website=Column(String(500)); email=Column(String(255)); phone=Column(String(50)); established_year=Column(Integer)
    accreditation=Column(String(255)); recognition=Column(String(500)); hostel=Column(Boolean,default=False); facilities=Column(Text)
    rating=Column(Float,default=0); description=Column(Text); verified=Column(Boolean,default=False)
    verification_status=Column(String(40),default="Unverified"); data_source=Column(String(1000)); source_url=Column(String(1000))
    last_verified_date=Column(DateTime); verified_by=Column(String(255)); admission_status=Column(String(60),default="Unknown")
    courses=relationship("CollegeCourse",back_populates="college",cascade="all, delete-orphan")
    fees=relationship("Fee",back_populates="college",cascade="all, delete-orphan")
    gallery=relationship("Media",back_populates="college",cascade="all, delete-orphan")
    reviews=relationship("Review",back_populates="college",cascade="all, delete-orphan")
    faqs=relationship("FAQ",back_populates="college",cascade="all, delete-orphan")

class University(Base):
    __tablename__="universities"
    id=Column(Integer,primary_key=True); name=Column(String(255),unique=True); state=Column(String(100)); website=Column(String(500))

class Course(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True); name=Column(String(255),nullable=False,index=True); slug=Column(String(255),unique=True,index=True)
    degree=Column(String(100)); duration=Column(String(100)); eligibility=Column(Text); entrance_exam=Column(String(255))
    admission_procedure=Column(Text); fees=Column(String(255)); career=Column(Text); description=Column(Text)
    seo_title=Column(String(255)); meta_description=Column(String(500))
    colleges=relationship("CollegeCourse",back_populates="course",cascade="all, delete-orphan")

class CollegeCourse(Base):
    __tablename__="college_courses"
    id=Column(Integer,primary_key=True); college_id=Column(Integer,ForeignKey("colleges.id")); course_id=Column(Integer,ForeignKey("courses.id"))
    seats=Column(Integer); admission_status=Column(String(50),default="Open")
    college=relationship("College",back_populates="courses"); course=relationship("Course",back_populates="colleges")

class Fee(Base):
    __tablename__="fees"
    id=Column(Integer,primary_key=True); college_id=Column(Integer,ForeignKey("colleges.id")); course_id=Column(Integer,ForeignKey("courses.id"))
    tuition_fee=Column(Numeric(14,2)); hostel_fee=Column(Numeric(14,2)); examination_fee=Column(Numeric(14,2))
    other_charges=Column(Numeric(14,2)); total_approx_fee=Column(Numeric(14,2)); fee_period=Column(String(100)); verified=Column(Boolean,default=False)
    college=relationship("College",back_populates="fees")

class Scholarship(Base):
    __tablename__="scholarships"
    id=Column(Integer,primary_key=True); name=Column(String(255),nullable=False); provider=Column(String(255)); kind=Column(String(50))
    eligibility=Column(Text); state=Column(String(100)); course=Column(String(255)); income_criteria=Column(String(255))
    amount=Column(String(255)); deadline=Column(String(100)); documents=Column(Text); application_url=Column(String(1000))
    status=Column(String(50),default="Open"); source_url=Column(String(1000)); last_verified_date=Column(DateTime)

class Exam(Base):
    __tablename__="exams"
    id=Column(Integer,primary_key=True); name=Column(String(255),nullable=False); conducting_authority=Column(String(255))
    eligibility=Column(Text); application_start=Column(String(100)); application_deadline=Column(String(100)); exam_date=Column(String(100))
    admit_card_date=Column(String(100)); result_date=Column(String(100)); official_website=Column(String(1000)); official_notification=Column(String(1000))
    description=Column(Text); source_url=Column(String(1000)); last_verified_date=Column(DateTime)

class MockTest(Base):
    __tablename__="mock_tests"
    id=Column(Integer,primary_key=True); title=Column(String(255),nullable=False); subject=Column(String(255)); exam=Column(String(255))
    difficulty=Column(String(50)); number_of_questions=Column(Integer,default=0); duration_minutes=Column(Integer,default=30); description=Column(Text)

class Question(Base):
    __tablename__="questions"
    id=Column(Integer,primary_key=True); test_id=Column(Integer,ForeignKey("mock_tests.id")); question=Column(Text,nullable=False)
    option_a=Column(String(500)); option_b=Column(String(500)); option_c=Column(String(500)); option_d=Column(String(500))
    answer=Column(String(1)); explanation=Column(Text); topic=Column(String(255))

class TestAttempt(Base):
    __tablename__="test_attempts"
    id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey("users.id")); test_id=Column(Integer,ForeignKey("mock_tests.id"))
    score=Column(Integer); percentage=Column(Float); correct=Column(Integer); incorrect=Column(Integer); unattempted=Column(Integer)
    time_taken_seconds=Column(Integer); created_at=Column(DateTime,default=datetime.utcnow)

class SavedCollege(Base):
    __tablename__="saved_colleges"
    id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey("users.id")); college_id=Column(Integer,ForeignKey("colleges.id"))
    created_at=Column(DateTime,default=datetime.utcnow); user=relationship("User",back_populates="saved")

class Review(Base):
    __tablename__="reviews"
    id=Column(Integer,primary_key=True); college_id=Column(Integer,ForeignKey("colleges.id")); name=Column(String(120)); course=Column(String(255))
    year=Column(String(20)); rating=Column(Integer); review=Column(Text); status=Column(String(30),default="Pending")
    image_url=Column(String(1000)); created_at=Column(DateTime,default=datetime.utcnow); college=relationship("College",back_populates="reviews")

class FAQ(Base):
    __tablename__="faqs"
    id=Column(Integer,primary_key=True); college_id=Column(Integer,ForeignKey("colleges.id")); question=Column(String(500)); answer=Column(Text)
    status=Column(String(30),default="Published"); college=relationship("College",back_populates="faqs")

class Media(Base):
    __tablename__="media"
    id=Column(Integer,primary_key=True); college_id=Column(Integer,ForeignKey("colleges.id")); url=Column(String(1000)); image_type=Column(String(100))
    alt_text=Column(String(500)); created_at=Column(DateTime,default=datetime.utcnow); college=relationship("College",back_populates="gallery")

class Blog(Base):
    __tablename__="blogs"
    id=Column(Integer,primary_key=True); title=Column(String(500)); slug=Column(String(500),unique=True); content=Column(Text)
    featured_image=Column(String(1000)); category=Column(String(100)); author=Column(String(255)); meta_title=Column(String(255))
    meta_description=Column(String(500)); canonical_url=Column(String(1000)); status=Column(String(30),default="Draft")
    publish_at=Column(DateTime); created_at=Column(DateTime,default=datetime.utcnow)

class Enquiry(Base):
    __tablename__="enquiries"
    id=Column(Integer,primary_key=True); lead_code=Column(String(30),unique=True,index=True); name=Column(String(120),nullable=False)
    mobile=Column(String(30),nullable=False); email=Column(String(255)); course=Column(String(255)); preferred_college=Column(String(255))
    state=Column(String(100)); city=Column(String(100)); qualification=Column(String(255)); message=Column(Text); source=Column(String(100),default="website")
    utm_source=Column(String(255)); utm_medium=Column(String(255)); utm_campaign=Column(String(255)); utm_content=Column(String(255))
    status=Column(String(60),default="New"); assigned_counsellor_id=Column(Integer,ForeignKey("users.id")); follow_up_date=Column(DateTime)
    notes=Column(Text); created_at=Column(DateTime,default=datetime.utcnow)

class LeadNote(Base):
    __tablename__="lead_notes"
    id=Column(Integer,primary_key=True); enquiry_id=Column(Integer,ForeignKey("enquiries.id")); user_id=Column(Integer,ForeignKey("users.id"))
    note=Column(Text); created_at=Column(DateTime,default=datetime.utcnow)

class SEO(Base):
    __tablename__="seo_metadata"
    id=Column(Integer,primary_key=True); path=Column(String(1000),unique=True); title=Column(String(255)); description=Column(String(500))
    canonical=Column(String(1000)); og_image=Column(String(1000)); schema_json=Column(Text)

class AuditLog(Base):
    __tablename__="audit_logs"
    id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey("users.id")); action=Column(String(255)); entity=Column(String(100)); entity_id=Column(String(100))
    details=Column(Text); created_at=Column(DateTime,default=datetime.utcnow)

class Notification(Base):
    __tablename__="notifications"
    id=Column(Integer,primary_key=True); user_id=Column(Integer,ForeignKey("users.id")); title=Column(String(255)); message=Column(Text)
    read=Column(Boolean,default=False); created_at=Column(DateTime,default=datetime.utcnow)

class Setting(Base):
    __tablename__="settings"
    id=Column(Integer,primary_key=True); key=Column(String(255),unique=True); value=Column(Text)
