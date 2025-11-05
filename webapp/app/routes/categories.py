from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import db as models

bp = Blueprint('categories', __name__, url_prefix='/categories')


@bp.route('/')
def list_categories():
    categories = models.get_categories()
    return render_template('categories/list.html', categories=categories)


@bp.route('/add', methods=('GET', 'POST'))
def add_category():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        if not name:
            flash('Name is required.', 'danger')
        else:
            new_id = models.create_category(name, description)
            category = models.get_category(new_id)
            return render_template('categories/confirm.html', action='added', category=category)
    return render_template('categories/form.html', category=None)


@bp.route('/<int:category_id>/edit', methods=('GET', 'POST'))
def edit_category(category_id):
    category = models.get_category(category_id)
    if category is None:
        flash('Category not found.', 'warning')
        return redirect(url_for('categories.list_categories'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        if not name:
            flash('Name is required.', 'danger')
        else:
            models.update_category(category_id, name, description)
            updated = models.get_category(category_id)
            return render_template('categories/confirm.html', action='edited', category=updated)

    return render_template('categories/form.html', category=category)


@bp.route('/<int:category_id>/delete', methods=('GET', 'POST'))
def delete_category(category_id):
    category = models.get_category(category_id)
    if category is None:
        flash('Category not found.', 'warning')
        return redirect(url_for('categories.list_categories'))

    if request.method == 'POST':
        models.delete_category(category_id)
        return render_template('categories/confirm.html', action='deleted', category=category)

    return render_template('categories/confirm.html', action='confirm_delete', category=category)
