from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import College
from ..schemas import PredictorIn,AssistantIn
from ..services.ai import search_colleges_with_ai
from ..config import settings
from openai import OpenAI

router=APIRouter(prefix="/api/v1/ai",tags=["AI"])

@router.post("/search")
def ai_search(data:AssistantIn,db:Session=Depends(get_db)):
    return search_colleges_with_ai(data.question,db)

@router.post("/predictor")
def predictor(data:PredictorIn,db:Session=Depends(get_db)):
    q=db.query(College)
    if data.state:q=q.filter(College.state.ilike(f"%{data.state}%"))
    if data.city:q=q.filter(College.city.ilike(f"%{data.city}%"))
    if data.government is not None:q=q.filter(College.college_type.ilike("%Government%" if data.government else "%Private%"))
    if data.hostel is True:q=q.filter(College.hostel==True)
    colleges=q.order_by(College.rating.desc()).limit(20).all()
    return {"disclaimer":"Estimated shortlist based on available data; not an admission guarantee.",
            "results":[{"college":c.name,"location":f"{c.city}, {c.state}","category":"Suitable" if i<7 else "Possible","rating":c.rating,"verified":c.verified} for i,c in enumerate(colleges)]}

@router.post("/assistant")
def assistant(data:AssistantIn):
    if not settings.OPENAI_API_KEY:return {"answer":"AI API is not configured. Add OPENAI_API_KEY to the backend environment.","source":"configuration"}
    client=OpenAI(api_key=settings.OPENAI_API_KEY)
    response=client.responses.create(model=settings.OPENAI_MODEL,input=f"""You are Padhaanewala AI, an education assistant.
Question: {data.question}
Give useful concise guidance. Never claim admission is guaranteed. For changing admission/regulatory facts, tell the user to verify with the relevant official authority.""")
    return {"answer":response.output_text,"source":"OpenAI"}
