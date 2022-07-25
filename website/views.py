# file to manage views
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from api_calls import get_device_info

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template('index.html', user=current_user)


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        imei = request.form.get('imei')
        data = get_device_info(imei)
        print(data['BatteryHealthPercentage'])
        if data:
            return render_template('cosmetics.html', user=current_user, data=data)
    return render_template('dashboard.html', user=current_user)


@views.route('/cosmetics', methods=['GET', 'POST'])
@login_required
def cosmetics():
    if request.method == 'POST':
        imei = request.form.get('imei')
        battery = request.form.get('battery')
        print(imei, battery)

    return render_template('cosmetics.html', user=current_user)