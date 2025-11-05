# Catalog Webapp (Flask + SQLite)

Small demo Flask application providing CRUD for Categories and Products.

Requirements

- Python 3.8+
- See `requirements.txt` (install into a virtualenv)

Quick start (from PowerShell on Windows)

```powershell
Set-Location -Path 'c:\Users\KrystianPilch\Desktop\CoPilot\CoPilot\webapp'
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Initialize the SQLite database from schema.sql
flask --app app init-db

# Run the development server
flask --app app run --debug
```

App structure

- `app/` – Flask package (blueprints, templates, static)
- `database/schema.sql` – SQL schema + sample data

Notes

- The app uses the DB file at `webapp/database/app.db` by default. Initializing
  the DB will create it and populate sample data from `schema.sql`.
