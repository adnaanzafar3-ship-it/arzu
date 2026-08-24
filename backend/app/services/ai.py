from openai import OpenAI
from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..config import settings
from ..models import College

def search_colleges_with_ai(question: str, db: Session):
    terms=[x.strip() for x in question.replace(","," ").split() if len(x.strip())>2]
    q=db.query(College)
    if terms:
        clauses=[]
        for t in terms[:8]:
            like=f"%{t}%"
            clauses += [College.name.ilike(like),College.city.ilike(like),College.state.ilike(like)]
        q=q.filter(or_(*clauses))
    candidates=q.order_by(College.rating.desc()).limit(30).all()
    rows=[{"id":c.id,"name":c.name,"city":c.city,"state":c.state,"type":c.college_type,
           "university":c.university,"rating":c.rating,"hostel":c.hostel,"verified":c.verified}
          for c in candidates]
    if not settings.OPENAI_API_KEY:
        return {"answer":"AI is not configured yet. Showing database matches.","query":question,"results":rows}
    client=OpenAI(api_key=settings.OPENAI_API_KEY)
    response=client.responses.create(
        model=settings.OPENAI_MODEL,
        input=f"""You are Padhaanewala's college-search assistant.
User query: {question}
Use the supplied database records as the source of truth for college facts.
Do not invent colleges, fees, recognition, rankings or admissions.
Rank candidates for relevance and explain briefly. If current information is missing, say it needs verification.
Candidates: {rows}""",
        tools=[{"type":"web_search"}],
    )
    return {"answer":response.output_text,"query":question,"results":rows}
