"""SQLite database helpers and simple CRUD helpers for categories/products.

This module provides:
- get_db() / close_db() helpers
- init_db() that executes the SQL in webapp/database/schema.sql
- click CLI command registration via init_app(app)
- convenience CRUD functions used by route handlers
"""
from pathlib import Path
import sqlite3
from flask import current_app, g
import click
import os


def get_db():
    """Return a sqlite3.Connection object attached to the Flask `g` object.

    Uses the path from current_app.config['DATABASE'].
    """
    if 'db' not in g:
        db_path = current_app.config['DATABASE']
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    """Initialize the database using the bundled schema.sql file.

    The schema.sql is expected at: webapp/database/schema.sql (relative to
    the package root). This function creates the parent directory for the
    database file if it does not exist.
    """
    schema_path = Path(__file__).resolve().parents[2] / 'database' / 'schema.sql'
    db_path = Path(current_app.config['DATABASE'])
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(str(db_path)) as conn:
        with open(schema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())


@click.command('init-db')
def init_db_command():
    """CLI command: initialize the database from the schema file."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """Register teardown and CLI with the Flask application."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# --- Basic CRUD helpers for categories and products ---

def count_categories():
    db = get_db()
    row = db.execute('SELECT COUNT(*) AS c FROM categories').fetchone()
    return row['c'] if row else 0


def count_products():
    db = get_db()
    row = db.execute('SELECT COUNT(*) AS c FROM products').fetchone()
    return row['c'] if row else 0


def get_categories():
    db = get_db()
    return db.execute('SELECT id, name, description FROM categories ORDER BY name').fetchall()


def get_category(category_id):
    db = get_db()
    return db.execute('SELECT id, name, description FROM categories WHERE id = ?', (category_id,)).fetchone()


def create_category(name, description):
    db = get_db()
    cur = db.execute('INSERT INTO categories (name, description) VALUES (?, ?)', (name, description))
    db.commit()
    return cur.lastrowid


def update_category(category_id, name, description):
    db = get_db()
    db.execute('UPDATE categories SET name = ?, description = ? WHERE id = ?', (name, description, category_id))
    db.commit()


def delete_category(category_id):
    db = get_db()
    db.execute('DELETE FROM categories WHERE id = ?', (category_id,))
    db.commit()


def get_products():
    db = get_db()
    return db.execute(
        'SELECT p.id, p.title, p.author, p.image, p.price, p.stock, p.category_id, c.name as category_name '
        'FROM products p JOIN categories c ON p.category_id = c.id ORDER BY p.title'
    ).fetchall()


def get_product(product_id):
    db = get_db()
    return db.execute(
        'SELECT p.id, p.title, p.author, p.image, p.price, p.stock, p.category_id, c.name as category_name '
        'FROM products p JOIN categories c ON p.category_id = c.id WHERE p.id = ?', (product_id,)
    ).fetchone()


def create_product(category_id, title, author, price, stock, image=None):
    db = get_db()
    cur = db.execute(
        'INSERT INTO products (category_id, title, author, image, price, stock) VALUES (?, ?, ?, ?, ?, ?)',
        (category_id, title, author, image, price, stock)
    )
    db.commit()
    return cur.lastrowid


def update_product(product_id, category_id, title, author, price, stock, image=None):
    db = get_db()
    if image is None:
        # keep existing image
        db.execute(
            'UPDATE products SET category_id = ?, title = ?, author = ?, price = ?, stock = ? WHERE id = ?',
            (category_id, title, author, price, stock, product_id)
        )
    else:
        # remove old image file if present and different
        try:
            old = db.execute('SELECT image FROM products WHERE id = ?', (product_id,)).fetchone()
            if old and old['image'] and old['image'] != image:
                upload_folder = current_app.config.get('UPLOAD_FOLDER')
                if upload_folder:
                    old_path = Path(upload_folder) / old['image']
                    if old_path.exists():
                        try:
                            os.remove(old_path)
                        except Exception:
                            # ignore errors on delete
                            pass
        except Exception:
            pass
        db.execute(
            'UPDATE products SET category_id = ?, title = ?, author = ?, image = ?, price = ?, stock = ? WHERE id = ?',
            (category_id, title, author, image, price, stock, product_id)
        )
    db.commit()


def delete_product(product_id):
    db = get_db()
    # delete image file if exists
    try:
        row = db.execute('SELECT image FROM products WHERE id = ?', (product_id,)).fetchone()
        if row and row['image']:
            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            if upload_folder:
                image_path = Path(upload_folder) / row['image']
                if image_path.exists():
                    try:
                        os.remove(image_path)
                    except Exception:
                        pass
    except Exception:
        pass
    db.execute('DELETE FROM products WHERE id = ?', (product_id,))
    db.commit()
