import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from models.user import User
from service.captcha import Captcha


bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if session.get('user_id'):
        return redirect(url_for('auth.logout'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        captcha = request.form['captcha']
        error = None

        if not Captcha.verify('login', captcha):
            flash('Invalid value entered for captcha!')
        else:
            user = User.query.filter_by(username=username).first()
            if user is None or not check_password_hash(user.password, password):
                flash('Incorrect username and/or password!')
            else:
                session['user_id'] = user.id
                return redirect(url_for('home.dashboard'))

    return render_template(
        'auth/login.html',
        title='Log in',
        captcha_src=Captcha.generate_captcha('login')
    )

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()