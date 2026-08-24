
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name:str; email:Optional[EmailStr]=None; password:Optional[str]=None; mobile:Optional[str]=None
class UserLogin(BaseModel): email:EmailStr; password:str
class Token(BaseModel): access_token:str; token_type:str="bearer"; role:str

class CollegeIn(BaseModel):
    name:str; official_name:Optional[str]=None; college_type:Optional[str]="Private"; university:Optional[str]=None
    state:Optional[str]=None; district:Optional[str]=None; city:Optional[str]=None; address:Optional[str]=None; pincode:Optional[str]=None
    website:Optional[str]=None; phone:Optional[str]=None; email:Optional[EmailStr]=None; established_year:Optional[int]=None
    accreditation:Optional[str]=None; recognition:Optional[str]=None; hostel:bool=False; facilities:Optional[str]=None
    rating:float=0; description:Optional[str]=None; verified:bool=False; verification_status:str="Unverified"
    data_source:Optional[str]=None; source_url:Optional[str]=None; admission_status:str="Unknown"

class CourseIn(BaseModel):
    name:str; degree:Optional[str]=None; duration:Optional[str]=None; eligibility:Optional[str]=None; entrance_exam:Optional[str]=None
    admission_procedure:Optional[str]=None; fees:Optional[str]=None; career:Optional[str]=None; description:Optional[str]=None
    seo_title:Optional[str]=None; meta_description:Optional[str]=None

class EnquiryIn(BaseModel):
    name:str; mobile:str; email:Optional[EmailStr]=None; course:Optional[str]=None; preferred_college:Optional[str]=None
    state:Optional[str]=None; city:Optional[str]=None; qualification:Optional[str]=None; message:Optional[str]=None
    source:str="website"; utm_source:Optional[str]=None; utm_medium:Optional[str]=None; utm_campaign:Optional[str]=None; utm_content:Optional[str]=None

class PredictorIn(BaseModel):
    course:str; entrance_exam:Optional[str]=None; score:Optional[float]=None; rank:Optional[int]=None; category:Optional[str]=None
    state:Optional[str]=None; city:Optional[str]=None; budget:Optional[float]=None; government:Optional[bool]=None
    hostel:Optional[bool]=None; preferences:Optional[str]=None

class AssistantIn(BaseModel): question:str
class ReviewIn(BaseModel): college_id:int; name:str; course:Optional[str]=None; year:Optional[str]=None; rating:int; review:str; image_url:Optional[str]=None
