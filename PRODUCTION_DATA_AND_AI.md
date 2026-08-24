# Production data, OTP and AI

1. Do not use the demo colleges as real production data.
2. Import verified college records from authoritative sources and retain source URL, verification status and last verified date.
3. For medical/AYUSH, prioritize official regulator/counselling sources such as NMC, NCH, NCISM, AACCC and relevant state counselling authorities.
4. Natural-language college search follows:
User -> FastAPI -> database candidate retrieval -> OpenAI ranking/explanation -> response.
5. AI is not allowed to invent college facts. Current information must be verified.
6. OpenAI API keys remain backend-only.
7. OTP requires a real transactional SMS provider account and its current API contract. The adapter is intentionally provider-neutral; configure and test it before launch.
8. Before accepting real student data, add PostgreSQL backups, HTTPS, rate limiting, admin 2FA, monitoring, secure file storage and legal/privacy review.
