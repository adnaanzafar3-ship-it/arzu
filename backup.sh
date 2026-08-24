#!/bin/sh
set -eu
mkdir -p backups
docker compose -f docker-compose.production.yml exec -T postgres pg_dump -U padhaanewala padhaanewala | gzip > backups/padhaanewala-$(date +%Y%m%d-%H%M%S).sql.gz
find backups -type f -mtime +14 -delete
