from flask import Blueprint, render_template
from ..models import db as models

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """Home dashboard showing counts of records."""
    categories_count = models.count_categories()
    products_count = models.count_products()
    return render_template('home.html', categories_count=categories_count, products_count=products_count)
