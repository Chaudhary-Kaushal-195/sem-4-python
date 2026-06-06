# Django Folder Map

This folder now has two clear areas:

```text
DJANGO/
  new_project/   clean Django project for learning
  old_projects/  copied projects kept for reference
  venv/          shared Python virtual environment
```

## Run the new learning project

```powershell
cd D:\GitHub\sem-4-python\T3\DJANGO\new_project
..\venv\Scripts\python.exe manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Run an old project

Only do this when you specifically want to see the old copied code:

```powershell
cd D:\GitHub\sem-4-python\T3\DJANGO\old_projects\P3
..\..\venv\Scripts\python.exe manage.py runserver
```

Whichever folder's `manage.py` you run, that Django project is the one the browser will show.
