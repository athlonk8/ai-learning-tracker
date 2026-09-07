# AI Learning Tracker

Minimal Django project for **DataTalksClub AI Dev Tools Zoomcamp 2026 Homework 1**.

Workflow: [spec.md](spec.md) → [backlog.md](backlog.md) → instructions in [AGENTS.md](AGENTS.md) → Task 1 implementation and verification.

Only Task 1 is implemented: Django scaffolding, the Course model, SQLite migration, and model tests. Course management pages, progress forms, learning notes, and the dashboard are planned, not implemented.

## Setup and commands

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/). If needed, install uv with `python -m pip install --user uv` and ensure your Python user Scripts/bin directory is on PATH.

From the project directory:

On the current homework machine, uv was installed in the parent workspace's `.tools` directory because user-site installation failed. In PowerShell, run these session settings first (the local cache also avoids a Windows cross-drive cache error):

```powershell
$env:Path = "$(Resolve-Path ..\.tools\uv\bin);$env:Path"
$env:UV_CACHE_DIR = Join-Path (Resolve-Path ..).Path '.tools\uv-cache'
```

These settings are unnecessary on another machine with a working uv installation.

```sh
uv sync --locked
uv run python manage.py migrate
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/ to see Django's development welcome page. Stop the server with Ctrl+C. Settings are for local development only.

Run tests and checks:

```sh
uv run python manage.py test
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
```

Tests use Django's isolated test database. Local data lives in ignored `db.sqlite3`; dependencies are pinned in `uv.lock`.

Course has a required title, status (`not_started`, `in_progress`, `completed`), and completion percentage from 0 to 100. Defaults are `not_started` and 0. Model validation uses `full_clean()`; as in standard Django, `save()` does not call it automatically. Database constraints additionally protect status and percentage bounds.
