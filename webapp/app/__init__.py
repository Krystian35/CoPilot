"""
Flask application factory and bootstrap.

This module creates the Flask application, configures the SQLite database
location, registers model helpers and attempts to register route blueprints.
"""
from pathlib import Path
from flask import Flask
import logging


def create_app(test_config=None):
    """Create and configure the Flask application.

    - Sets default config values (including DATABASE path)
    - Registers DB helpers from :mod:`app.models.db` via its ``init_app``
      function so CLI commands and teardown handlers are available.
    - Attempts to register blueprints from ``app.routes.*`` if present.

    The package is intended to be run from the `webapp` folder with:

        flask --app app run --debug
    """
    app = Flask(__name__, instance_relative_config=True)

    # sensible defaults; the database file will be created under webapp/database
    base = Path(__file__).resolve().parents[1]  # points to webapp/
    default_db = str(base / 'database' / 'app.db')

    # set upload folder inside the package's static directory so files are
    # served by Flask's `static` endpoint (app.static_folder)
    upload_folder = str(Path(app.root_path) / 'static' / 'images')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=default_db,
        UPLOAD_FOLDER=upload_folder,
    )

    if test_config is not None:
        app.config.update(test_config)

    # register DB helpers (will add CLI command `flask --app app init-db`)
    try:
        from .models import db as models_db

        models_db.init_app(app)
    except Exception as exc:  # pragma: no cover - defensive
        logging.getLogger(__name__).warning("Could not register DB helpers: %s", exc)

    # ensure upload folder exists
    try:
        import os

        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    except Exception:
        logging.getLogger(__name__).info("Could not create upload folder: %s", app.config.get('UPLOAD_FOLDER'))

    # register blueprints if route modules are present
    try:
        from .routes import main

        app.register_blueprint(main.bp)
    except Exception:
        # routes will be added later; keep app importable in the meantime
        logging.getLogger(__name__).info("Main routes not yet available; skipping registration.")

    try:
        from .routes import categories

        app.register_blueprint(categories.bp)
    except Exception:
        logging.getLogger(__name__).info("Categories routes not yet available; skipping registration.")

    try:
        from .routes import products

        app.register_blueprint(products.bp)
    except Exception:
        logging.getLogger(__name__).info("Products routes not yet available; skipping registration.")

    return app
