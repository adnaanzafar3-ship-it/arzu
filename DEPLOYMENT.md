# Deployment checklist

## Frontend
Deploy `frontend` to a Next.js-compatible host. Set:
`NEXT_PUBLIC_API_URL=https://api.yourdomain.in`

## Backend
Deploy `backend` to a Python/FastAPI host. Set:
`DATABASE_URL` to PostgreSQL and a strong `JWT_SECRET`.
Set `FRONTEND_URL=https://padhaanewala.in`.

## Domain
- padhaanewala.in -> frontend
- api.padhaanewala.in -> backend

## Before accepting real student data
- HTTPS
- PostgreSQL backups and restoration testing
- Strong secrets
- Production CORS
- Rate limiting
- Email/SMS/OTP provider
- Object storage for images
- Admin 2FA
- Monitoring
- Security testing
- Legally reviewed Privacy Policy / Terms / consent
- Replace demo records with verified college/course/scholarship data
