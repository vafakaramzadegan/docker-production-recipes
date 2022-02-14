from flask import Blueprint, redirect, url_for
from .auth import login_required


bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    return redirect(url_for('home.dashboard'))