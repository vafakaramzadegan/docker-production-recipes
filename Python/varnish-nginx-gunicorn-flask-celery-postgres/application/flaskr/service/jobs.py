from app import celery, db
from models.job import Job


@celery.task(name='job1')
def job1():
    rec = Job(job_name='job1')
    db.session.add(rec)
    db.session.commit()

    return True

@celery.task(name='job2')
def job2():
    rec = Job(job_name='job2')
    db.session.add(rec)
    db.session.commit()

    return True
