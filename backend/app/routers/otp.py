from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..config import settings
import secrets,time,httpx

router=APIRouter(prefix="/api/v1/otp",tags=["OTP"])
_store={}
class OTPRequest(BaseModel): mobile:str
class OTPVerify(BaseModel): mobile:str; otp:str

@router.post("/send")
async def send_otp(data:OTPRequest):
    if not settings.OTP_PROVIDER_URL or not settings.OTP_PROVIDER_API_KEY:
        raise HTTPException(503,"OTP provider is not configured")
    otp=f"{secrets.randbelow(1000000):06d}"
    _store[data.mobile]={"otp":otp,"expires":time.time()+300}
    payload={"mobile":data.mobile,"otp":otp,"sender_id":settings.OTP_SENDER_ID}
    headers={"Authorization":f"Bearer {settings.OTP_PROVIDER_API_KEY}"}
    async with httpx.AsyncClient(timeout=15) as client:
        r=await client.post(settings.OTP_PROVIDER_URL,json=payload,headers=headers)
    if r.status_code>=400: raise HTTPException(502,"OTP provider request failed")
    return {"message":"OTP sent"}

@router.post("/verify")
def verify_otp(data:OTPVerify):
    item=_store.get(data.mobile)
    if not item or item["expires"]<time.time() or not secrets.compare_digest(item["otp"],data.otp):
        raise HTTPException(400,"Invalid or expired OTP")
    _store.pop(data.mobile,None)
    return {"verified":True}
