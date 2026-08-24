from .database import Base, engine, SessionLocal
from .models import *
from .security import hash_password

Base.metadata.create_all(bind=engine)
db = SessionLocal()

if not db.query(User).filter(User.email=="admin@padhaanewala.in").first():
    db.add(User(name="Padhaanewala Admin", email="admin@padhaanewala.in", password_hash=hash_password("ChangeMe123!"), role="admin"))
if not db.query(User).filter(User.email=="student@padhaanewala.in").first():
    db.add(User(name="Demo Student", email="student@padhaanewala.in", password_hash=hash_password("Student123!"), role="student"))

courses = [
    ("BHMS","BHMS","5.5 years","10+2 with PCB; verify current rules","NEET"),
    ("BAMS","BAMS","5.5 years","10+2 with PCB; verify current rules","NEET"),
    ("B.Sc Nursing","B.Sc Nursing","4 years","10+2; check institution/state rules","Varies"),
    ("B.Pharm","B.Pharm","4 years","10+2 with required subjects","Varies"),
    ("D.Pharm","D.Pharm","2 years","10+2 with required subjects","Varies"),
    ("BCA","BCA","3-4 years","10+2; institution-specific requirements","Varies"),
    ("MBA","MBA","2 years","Bachelor degree; entrance rules vary","CAT/CMAT/State exams"),
]
for name,degree,duration,elig,exam in courses:
    if not db.query(Course).filter(Course.name==name).first():
        slug="-".join(name.lower().replace("&","and").split())
        db.add(Course(name=name, slug=slug, degree=degree, duration=duration, eligibility=elig, entrance_exam=exam))

colleges = [
    ("Padhaanewala Demo College, Bengaluru","Private","Karnataka","Bengaluru","Bengaluru"),
    ("Padhaanewala Demo College, Bihar","Private","Bihar","Araria","Araria"),
    ("Padhaanewala Government College Demo","Government","Karnataka","Mangaluru","Mangaluru"),
    ("Padhaanewala Health Sciences Demo","Private","Karnataka","Mysuru","Mysuru"),
]
for idx,(name,typ,state,district,city) in enumerate(colleges,1):
    if not db.query(College).filter(College.name==name).first():
        db.add(College(college_code=f"COLLEGE{idx:06d}",name=name,slug="-".join(name.lower().split()),college_type=typ,state=state,district=district,city=city,hostel=True,rating=4.2,description="Demo record. Replace with verified institutional data.",verified=False))

if not db.query(Scholarship).first():
    db.add(Scholarship(name="Demo Merit Scholarship",provider="Padhaanewala Demo",kind="Private",eligibility="Merit-based; verify terms",state="All India",course="All",amount="Up to ₹25,000",deadline="Check current notice",application_url="https://padhaanewala.in"))

if not db.query(Exam).first():
    db.add(Exam(name="NEET-UG Demo Record",conducting_authority="NTA",eligibility="Check official notification",application_deadline="Check official notice",exam_date="Check official notice",official_website="https://neet.nta.nic.in"))

if not db.query(MockTest).first():
    test=MockTest(title="NEET Biology Starter Test",subject="Biology",difficulty="Easy",duration_minutes=15,description="Demo test")
    db.add(test); db.flush()
    db.add_all([
        Question(test_id=test.id,question="Which organelle is known as the powerhouse of the cell?",option_a="Nucleus",option_b="Mitochondria",option_c="Ribosome",option_d="Golgi body",answer="B",explanation="Mitochondria are the main sites of ATP production."),
        Question(test_id=test.id,question="DNA stands for?",option_a="Deoxyribonucleic acid",option_b="Ribonucleic acid",option_c="Amino acid",option_d="Nucleic enzyme",answer="A",explanation="DNA is deoxyribonucleic acid."),
    ])

db.commit()
db.close()
print("Seed complete.")
