from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth, colleges, content, enquiries, ai, admin, otp, student
from .config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Padhaanewala API", version="1.0.0", description="Education platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(colleges.router)
app.include_router(content.router)
app.include_router(enquiries.router)
app.include_router(ai.router)
app.include_router(admin.router)
app.include_router(otp.router)
app.include_router(student.router)

@app.get("/")
def root():
    return {"name":"Padhaanewala API","status":"running","docs":"/docs"}

@app.get("/health")
def health():
    return {"status":"ok"}
