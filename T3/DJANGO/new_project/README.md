# Django Learning Project

This folder is now a small, clean Django project for learning.

## Start the project

From this `new_project` folder:

```powershell
cd D:\GitHub\sem-4-python\T3\DJANGO\new_project
..\venv\Scripts\python.exe manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Important files

- `manage.py` runs Django commands.
- `config/settings.py` contains project settings.
- `config/urls.py` connects URLs to apps.
- `pages/urls.py` lists page URLs.
- `pages/views.py` contains Python functions that return pages.
- `templates/` contains HTML.
- `static/` contains CSS and images.

## What changed

- This clean learning project lives in `DJANGO\new_project`.
- The copied projects live in `DJANGO\old_projects`.
- The shared virtual environment stays in `DJANGO\venv`.

## Useful commands

```powershell
..\venv\Scripts\python.exe manage.py check
..\venv\Scripts\python.exe manage.py test
..\venv\Scripts\python.exe manage.py runserver
```
