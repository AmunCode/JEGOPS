# file to manage views
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from api_calls import get_device_info
from phone import Phone

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    return render_template('index.html', user=current_user)


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        IMEI = request.form.get('imei')
        session['current_device'] = get_device_info(IMEI)
        # print(data)
        if session['current_device']:
            # return redirect(url_for('views.cosmetics', user=current_user))
            return redirect(url_for('views.cosmetics', user=current_user, data=session['current_device']))
        else:
            flash(f'IMEI {IMEI} not found!', category='error')

        # Tracer lines

        # testing_data = cosmetic_data.update(data)
        # print(f"cosmetic data: {cosmetic_data}")
        # print(f"full data: {testing_data}")
    return render_template('dashboard.html', user=current_user)


@views.route('/cosmetics', methods=['GET', 'POST'])
@login_required
def cosmetics():
    if request.method == 'POST':
        imei = request.form.get('imei')
        battery = request.form.get('battery')
        scratches = request.form.get('scratches')
        dents = request.form.get('dents')
        lcd_discoloration = request.form.get('lcd-discoloration')
        components_missing = request.form.get('missing-components')
        cracked = request.form.get('cracks')
        markings = request.form.get('markings')
        cosmetic_data = request.form.to_dict()
        # print(data['BatteryHealthPercentage'])
        print(f"scratches: {scratches}, dents {dents}, lcd {lcd_discoloration}, comps {components_missing},"
              f" cracked {cracked}, markings {markings}")
        print(cosmetic_data)
        print(imei, battery)
        session.clear()
        return redirect(url_for('views.dashboard', user=current_user))

    return render_template('cosmetics.html', user=current_user, data=session['current_device'])
