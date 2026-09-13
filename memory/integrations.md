---
name: integrations
description: Внешние API, webhooks, ограничения интеграций
metadata:
  type: project
---

## Внешние сервисы

| Сервис | Назначение | Auth | Rate Limits |
|--------|-----------|------|-------------|
| {{SERVICE_1}} | {{PURPOSE}} | API Key в .env | {{LIMITS}} |

## Webhooks

- {{WEBHOOK_1}}: {{DESCRIPTION}}

## .env переменные (никогда не коммитить)

Два источника (см. [.env.example](../.env.example)):

1. **Локальный `.env`** в корне проекта — приоритет, project-specific секреты.
2. **Глобальный `~/claude/.env`** — общий кошелёк ключей (OpenRouter, Gemini, Perplexity…).

> ⚠️ **Коммерческие проекты** (`projects/commercial/`) читают **только локальный `.env`** —
> глобальный кошелёк игнорируется. Все ключи указывай локально.

Загрузка: `env_loader.load_project_env(Path(__file__).resolve().parent)`

```
# Локально (всегда):
SERVICE_API_KEY=
DATABASE_URL=
```
