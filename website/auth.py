from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('uName')
        password = request.form.get('password')
        user = User.query.filter_by(user_name=user_name).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard', user=current_user))
                # send to first page of grading process
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exist. please register.', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('logout.html', user=current_user)


@auth.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        user_name = request.form.get('uName')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        admin_checkbox = request.form.get('is_admin')

        if admin_checkbox:
            is_admin = True
        else:
            is_admin = False

        user = User.query.filter_by(user_name=user_name).first()
        if user:
            flash('user already exists!', category='error')
        elif len(user_name) < 5:
            flash('Username must be great than 4 characters.', category='error')
        elif len(password) < 7:
            flash('password is too short, must be at least 7 characters.', category='error')
        elif password != confirm_password:
            flash('passwords do not match!', category='error')
        else:
            # all good, add to DB
            new_user = User(user_name=user_name, password=generate_password_hash(password, method='sha512'), is_admin=is_admin)
            db.session.add(new_user)
            db.session.commit()
            flash('Account successfully created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)



