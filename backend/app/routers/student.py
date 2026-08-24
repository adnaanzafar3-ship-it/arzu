
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User,College,SavedCollege,Review
from ..security import current_user
from ..schemas import ReviewIn

router=APIRouter(prefix="/api/v1/student",tags=["Student"])

@router.get("/saved")
def saved(user=Depends(current_user),db:Session=Depends(get_db)):
    return [db.get(College,x.college_id) for x in db.query(SavedCollege).filter(SavedCollege.user_id==user.id).all()]

@router.post("/saved/{college_id}")
def save(college_id:int,user=Depends(current_user),db:Session=Depends(get_db)):
    if not db.get(College,college_id): raise HTTPException(404,"College not found")
    if not db.query(SavedCollege).filter_by(user_id=user.id,college_id=college_id).first():
        db.add(SavedCollege(user_id=user.id,college_id=college_id));db.commit()
    return {"saved":True}

@router.delete("/saved/{college_id}")
def unsave(college_id:int,user=Depends(current_user),db:Session=Depends(get_db)):
    x=db.query(SavedCollege).filter_by(user_id=user.id,college_id=college_id).first()
    if x: db.delete(x);db.commit()
    return {"saved":False}

@router.get("/compare")
def compare(ids:str,user=Depends(current_user),db:Session=Depends(get_db)):
    values=[]
    for raw in ids.split(",")[:6]:
        try: c=db.get(College,int(raw))
        except: c=None
        if c: values.append(c)
    return values

@router.post("/reviews")
def review(data:ReviewIn,user=Depends(current_user),db:Session=Depends(get_db)):
    x=Review(**data.model_dump(),status="Pending");db.add(x);db.commit();db.refresh(x)
    return {"message":"Review submitted for moderation","id":x.id}
