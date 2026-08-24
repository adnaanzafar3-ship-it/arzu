# Padhaanewala Edutech Services — Complete Full-Stack MVP

This repository is a single integrated project for Padhaanewala:
- Next.js + React + TypeScript frontend
- FastAPI backend
- SQLAlchemy database layer
- JWT authentication
- College/course/scholarship/exam/mock-test/enquiry APIs
- Student dashboard
- Admin dashboard
- College comparison
- Basic AI predictor/assistant endpoints
- SEO metadata, sitemap and robots
- Responsive mobile-first UI

## 1. Run backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

The development default uses SQLite so the project starts immediately. For production, set
DATABASE_URL to PostgreSQL in `.env`.

Seed demo data:

```bash
python -m app.seed
```

Demo admin:
- email: admin@padhaanewala.in
- password: ChangeMe123!

Demo student:
- email: student@padhaanewala.in
- password: Student123!

Change these passwords before production.

## 2. Run frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Open http://localhost:3000

## 3. Production database

Set:

DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/padhaanewala

Then run the backend and seed/migrate using your deployment process.

## 4. AI

The demo predictor and assistant work without an external AI key. They use structured database logic and safe templates.
For a real AI provider, implement the provider in `backend/app/services/ai.py` and keep the key only in backend environment variables.

## 5. Important

This is a complete integrated MVP/codebase, not a claim that every production security/compliance requirement has been independently audited.
Before accepting real student data, configure HTTPS, PostgreSQL backups, email/SMS/OTP provider, rate limiting, monitoring, object storage, secrets, 2FA and a security review.
