import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta


db = SQLAlchemy()

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # make sure to change the key
        SECRET_KEY='APP_SECRET_KEY',
        SQLALCHEMY_DATABASE_URI='postgresql://%s:%s@%s:5432/%s' % (
            os.environ['POSTGRES_USER'],
            os.environ['POSTGRES_PASSWORD'],
            'postgres',
            os.environ['POSTGRES_DB']
        ),
        DEBUG=False,
        CELERY_BROKER_URL='redis://redis:6379',
        CELERY_RESULT_BACKEND='redis://redis:6379',
        CELERY_IMPORTS = "service.jobs",
        CELERYBEAT_SCHEDULE = {
            'job1': {
                'task': 'job1',
                'schedule': timedelta(seconds=30),
            },
            'job2': {
                'task': 'job2',
                'schedule': timedelta(seconds=60),
            }
        }
    )

    db.init_app(app)

    from controllers import auth, index, home, jobs
    app.register_blueprint(auth.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(jobs.bp)

    return app

app = create_app()
celery = make_celery(app)
csrf = CSRFProtect(app)