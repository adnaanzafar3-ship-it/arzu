
# Environments

Development: localhost, local database.
Staging: staging.padhaanewala.in + staging PostgreSQL.
Production: padhaanewala.in + api.padhaanewala.in + production PostgreSQL.

Never use production secrets in Git.
Never test experimental changes directly on production.
Use Git branches such as main, develop and feature/*.
Run API/frontend/E2E tests before promotion.
