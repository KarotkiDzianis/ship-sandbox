---
name: tech-stack
description: Технический стек, архитектура, ключевые паттерны
metadata:
  type: project
---

## Stack

- Frontend: {{FRONTEND}} (Next.js / Astro / plain HTML)
- Backend: {{BACKEND}} (FastAPI / Node / Python)
- Database: {{DATABASE}} (Supabase / PostgreSQL / SQLite)
- Auth: {{AUTH}}
- Hosting: {{HOSTING}}
- AI/LLM: {{AI_PROVIDER}} (claude-sonnet-4-6 для реализации, claude-haiku-4-5 для рутины)

## Структура src/

```
src/
├── web/          ← сайт / лендинг
│   ├── pages/
│   ├── components/
│   └── styles/
├── tools/        ← бизнес-инструменты
│   ├── calculators/
│   ├── forms/
│   └── dashboards/
└── automation/   ← агенты и интеграции
    ├── agents/
    ├── webhooks/
    └── workflows/
```

## Архитектурные решения

| Решение | Выбрали | Отвергли | Причина |
|---------|---------|----------|---------|
| {{DECISION_1}} | {{CHOICE}} | {{ALTERNATIVE}} | {{REASON}} |

## Ключевые паттерны

- {{PATTERN_1}}
- {{PATTERN_2}}

## Видео/аудио (будущее)

- Транскрипция: faster-whisper (локально) или Whisper API
- Генерация видео: fal.ai (Runway, Kling)
- Генерация аудио: ElevenLabs / OpenAI TTS
- Graphify поддерживает видео: запускай с `--whisper-model medium`
