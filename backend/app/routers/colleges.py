
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_,asc,desc
from ..database import get_db
from ..models import College
from ..schemas import CollegeIn
from ..security import admin_user

router=APIRouter(prefix="/api/v1/colleges",tags=["Colleges"])

def slugify(s): return "-".join("".join(c.lower() if c.isalnum() else " " for c in s).split())

@router.get("")
def list_colleges(q:str="",state:str="",district:str="",city:str="",college_type:str="",university:str="",
                  min_rating:float=0,hostel:bool|None=None,admission_status:str="",page:int=1,limit:int=24,
                  sort:str="rating",db:Session=Depends(get_db)):
    limit=max(1,min(limit,100)); query=db.query(College)
    if q:
        like=f"%{q}%";query=query.filter(or_(College.name.ilike(like),College.official_name.ilike(like),College.city.ilike(like),College.state.ilike(like),College.district.ilike(like)))
    if state:query=query.filter(College.state.ilike(f"%{state}%"))
    if district:query=query.filter(College.district.ilike(f"%{district}%"))
    if city:query=query.filter(College.city.ilike(f"%{city}%"))
    if college_type:query=query.filter(College.college_type.ilike(f"%{college_type}%"))
    if university:query=query.filter(College.university.ilike(f"%{university}%"))
    if min_rating:query=query.filter(College.rating>=min_rating)
    if hostel is not None:query=query.filter(College.hostel==hostel)
    if admission_status:query=query.filter(College.admission_status.ilike(f"%{admission_status}%"))
    total=query.count()
    order=College.name.asc() if sort=="name" else College.rating.desc()
    items=query.order_by(order).offset((page-1)*limit).limit(limit).all()
    return {"items":items,"total":total,"page":page,"limit":limit}

@router.get("/{college_id}")
def get_college(college_id:int,db:Session=Depends(get_db)):
    x=db.get(College,college_id)
    if not x:raise HTTPException(404,"College not found")
    return x

@router.post("",dependencies=[Depends(admin_user)])
def create_college(data:CollegeIn,db:Session=Depends(get_db)):
    x=College(**data.model_dump(),slug=slugify(data.name));x.college_code=f"COLLEGE{db.query(College).count()+1:06d}"
    db.add(x);db.commit();db.refresh(x);return x

@router.put("/{college_id}",dependencies=[Depends(admin_user)])
def update_college(college_id:int,data:CollegeIn,db:Session=Depends(get_db)):
    x=db.get(College,college_id)
    if not x:raise HTTPException(404,"College not found")
    for k,v in data.model_dump().items():setattr(x,k,v)
    x.slug=slugify(x.name);db.commit();db.refresh(x);return x

@router.delete("/{college_id}",dependencies=[Depends(admin_user)])
def delete_college(college_id:int,db:Session=Depends(get_db)):
    x=db.get(College,college_id)
    if not x:raise HTTPException(404,"College not found")
    db.delete(x);db.commit();return {"message":"Deleted"}
