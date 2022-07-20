from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('uName')
        password = request.form.get('password')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        user_name = request.form.get('uName')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(user_name) < 4:
            flash('Email must be great than 5 characters.', category='error')
        elif password != confirm_password:
            flash('Email must be great than 5 characters.', category='error')
        else:
            # all good, add to DB
            flash('Account successfully created!', category='success')

    return render_template('signup.html')



