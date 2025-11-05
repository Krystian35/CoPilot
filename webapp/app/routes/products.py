from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
import uuid
from ..models import db as models
import os

bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('/')
def list_products():
    products = models.get_products()
    return render_template('products/list.html', products=products)


@bp.route('/add', methods=('GET', 'POST'))
def add_product():
    categories = models.get_categories()
    if request.method == 'POST':
        try:
            category_id = int(request.form.get('category_id'))
        except (TypeError, ValueError):
            category_id = None
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        price = request.form.get('price', '').strip()
        stock = request.form.get('stock', '').strip()

        errors = []
        if not title:
            errors.append('Title is required.')
        if category_id is None:
            errors.append('Category selection is required.')

        try:
            price_val = float(price) if price else None
        except ValueError:
            errors.append('Price must be a number.')
            price_val = None

        try:
            stock_val = int(stock) if stock else 0
        except ValueError:
            errors.append('Stock must be an integer.')
            stock_val = 0

        # handle uploaded image
        image_file = request.files.get('image')
        image_filename = None
        if image_file and image_file.filename:
            orig = secure_filename(image_file.filename)
            filename = f"{uuid.uuid4().hex}_{orig}"
            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            if upload_folder:
                os.makedirs(upload_folder, exist_ok=True)
                dest = os.path.join(upload_folder, filename)
                image_file.save(dest)
                image_filename = filename

        if errors:
            for e in errors:
                flash(e, 'danger')
        else:
            new_id = models.create_product(category_id, title, author or None, price_val, stock_val, image=image_filename)
            product = models.get_product(new_id)
            return render_template('products/confirm.html', action='added', product=product)

    return render_template('products/form.html', product=None, categories=categories)


@bp.route('/<int:product_id>/edit', methods=('GET', 'POST'))
def edit_product(product_id):
    product = models.get_product(product_id)
    if product is None:
        flash('Product not found.', 'warning')
        return redirect(url_for('products.list_products'))

    categories = models.get_categories()
    if request.method == 'POST':
        try:
            category_id = int(request.form.get('category_id'))
        except (TypeError, ValueError):
            category_id = None
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        price = request.form.get('price', '').strip()
        stock = request.form.get('stock', '').strip()

        errors = []
        if not title:
            errors.append('Title is required.')
        if category_id is None:
            errors.append('Category selection is required.')

        try:
            price_val = float(price) if price else None
        except ValueError:
            errors.append('Price must be a number.')
            price_val = None

        try:
            stock_val = int(stock) if stock else 0
        except ValueError:
            errors.append('Stock must be an integer.')
            stock_val = 0

        # handle uploaded image
        image_file = request.files.get('image')
        image_filename = None
        if image_file and image_file.filename:
            orig = secure_filename(image_file.filename)
            filename = f"{uuid.uuid4().hex}_{orig}"
            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            if upload_folder:
                os.makedirs(upload_folder, exist_ok=True)
                dest = os.path.join(upload_folder, filename)
                image_file.save(dest)
                image_filename = filename

        if errors:
            for e in errors:
                flash(e, 'danger')
        else:
            # if no new image uploaded, pass image=None to keep existing
            models.update_product(product_id, category_id, title, author or None, price_val, stock_val, image=image_filename)
            updated = models.get_product(product_id)
            return render_template('products/confirm.html', action='edited', product=updated)

    return render_template('products/form.html', product=product, categories=categories)


@bp.route('/<int:product_id>/delete', methods=('GET', 'POST'))
def delete_product(product_id):
    product = models.get_product(product_id)
    if product is None:
        flash('Product not found.', 'warning')
        return redirect(url_for('products.list_products'))

    if request.method == 'POST':
        models.delete_product(product_id)
        return render_template('products/confirm.html', action='deleted', product=product)

    return render_template('products/confirm.html', action='confirm_delete', product=product)
