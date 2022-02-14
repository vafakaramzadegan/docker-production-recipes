from flask import Blueprint, render_template
from .auth import login_required
from app import db
from models.job import Job


bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template(
        'home/dashboard.html',
        title='Dashboard',
        num_of_jobs=db.session.query(Job).count()
    )