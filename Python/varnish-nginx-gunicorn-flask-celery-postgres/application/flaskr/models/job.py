from app import db
from sqlalchemy.sql import func


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(50), unique=True, nullable=False)
    dt = db.Column(db.DateTime(timezone=True), default=func.now())