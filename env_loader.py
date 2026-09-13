"""
env_loader.py — единая загрузка переменных окружения для проектов.

Правило:
- Локальный .env проекта грузится ВСЕГДА и имеет приоритет.
- Глобальный кошелёк ~/claude/.env подмешивается ТОЛЬКО для НЕ-коммерческих
  проектов (вне projects/commercial/). Коммерческие проекты изолированы и
  используют только свой внутренний .env (защита клиентских данных).

Использование (в config.py / automation-агенте проекта):

    from pathlib import Path
    from env_loader import load_project_env

    info = load_project_env(Path(__file__).resolve().parent)
    # info -> {'commercial': bool, 'local_env': bool, 'global_env': bool, ...}
"""
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # dotenv опционален — если не установлен, тихо пропускаем
    def load_dotenv(*_args, **_kwargs):
        return False

GLOBAL_ENV = Path.home() / "claude" / ".env"


def _is_commercial(project_root: Path) -> bool:
    """Коммерческий = лежит внутри projects/commercial/."""
    return "/projects/commercial/" in (project_root.as_posix() + "/")


def load_project_env(project_root) -> dict:
    """Грузит локальный (+ глобальный для не-коммерческих) .env. Local wins.

    override=False => переменная, загруженная ПЕРВОЙ, побеждает. Поэтому
    локальный .env читаем первым — он переопределяет глобальные дефолты.
    """
    project_root = Path(project_root).resolve()
    local_env = project_root / ".env"
    commercial = _is_commercial(project_root)

    if local_env.exists():
        load_dotenv(local_env, override=False)            # локальный — приоритет

    used_global = False
    if not commercial and GLOBAL_ENV.exists():
        load_dotenv(GLOBAL_ENV, override=False)           # общий кошелёк — добивает недостающее
        used_global = True

    return {
        "project_root": str(project_root),
        "commercial": commercial,
        "local_env": local_env.exists(),
        "global_env": used_global,
    }
