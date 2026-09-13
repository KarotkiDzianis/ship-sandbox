# Проект: Ship Sandbox E2E Test

> Наследует глобальные правила из `/Users/dzianis/claude/CLAUDE.md`.

## Что это

НЕ клиентский проект. Единственная цель — первый живой сквозной прогон
платформы `platform/ship` (commit → CI → build → deploy → restart →
health → auto-rollback) на реальном VM, прежде чем на Ship переводят
настоящие проекты (TradePulse и др.). Одноразовый расходный материал:
можно удалить/пересоздать в любой момент без потери ценности.

`project.yml`: `approval: automatic` — деплой без Telegram-подтверждения,
намеренно (central registry, `platform/ship/registry/projects.yml`, а не
этот файл — сам проект не может себе такое разрешить). Цель первого
прогона — доказать, что механика деплоя (install/verify/switch/restart/
health/rollback) реально работает на VM с systemd, отдельно от вопроса
работы Telegram-approval (это отдельный, более поздний шаг).

## Приложение

`app/main.py` — тривиальный HTTP-сервер на стандартной библиотеке (без
зависимостей): `/` отдаёт версию (git sha, читается из `VERSION`),
`/healthz` отдаёт 200. `scripts/ship/build` копирует их в `build/`.
`scripts/ship/health` — curl на `/healthz`. Никакой бизнес-логики.

## Systemd

`ship-sandbox.service` (шаблон в `deploy/ship-sandbox.service`) —
отдельный юнит, изолированный от TradePulse и другого бота на этом же
VM. Restart-разрешение раннера ограничено sudoers-правилом ТОЛЬКО на
`systemctl restart ship-sandbox` — никогда не reboot, никогда другие
сервисы.
