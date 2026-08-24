from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    DATABASE_URL:str="sqlite:///./padhaanewala.db"
    JWT_SECRET:str="change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES:int=1440
    FRONTEND_URL:str="http://localhost:3000"
    OPENAI_API_KEY:str=""
    OPENAI_MODEL:str="gpt-5.4"
    OTP_PROVIDER_URL:str=""
    OTP_PROVIDER_API_KEY:str=""
    OTP_SENDER_ID:str="PADHAAN"
    WHATSAPP_NUMBER:str=""
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
settings=Settings()
