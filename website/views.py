# file to manage views
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template('index.html', user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@views.route('/cosmetics', methods=['GET', 'POST'])
@login_required
def cosmetics():
    if request.method == 'POST':
        imei = request.form.get('imei')
        battery = request.form.get('battery')
        print(imei, battery)

    return render_template('cosmetics.html', user=current_user)