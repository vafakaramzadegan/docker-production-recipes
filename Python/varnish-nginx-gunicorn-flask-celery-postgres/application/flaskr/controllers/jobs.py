from flask import Blueprint, render_template
from .auth import login_required
from models.job import Job
from sqlalchemy import desc


bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@bp.route('/list', methods=['GET'])
@login_required
def list_jobs():
    jobs = Job.query.order_by(desc(Job.id)).all()
    return render_template(
        'jobs/list.html',
        title='Dashboard',
        jobs=jobs,
        num_of_jobs=len(jobs)
    )