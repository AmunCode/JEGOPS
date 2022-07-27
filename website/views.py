# file to manage views
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from api_calls import get_device_info
from phone import Phone
from grade import grade

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
        device_cosmetics = {}
        # imei = request.form.get('imei')
        # battery = request.form.get('battery')
        device_cosmetics['scratches'] = request.form.get('scratches')
        device_cosmetics['dents'] = request.form.get('dents')
        device_cosmetics['lcd_discoloration'] = request.form.get('lcd-discoloration')
        device_cosmetics['components_missing'] = request.form.get('missing-components')
        device_cosmetics['cracked'] = request.form.get('cracks')
        device_cosmetics['markings'] = request.form.get('markings')
        # device_cosmetics['cosmetic_data'] = request.form.to_dict()
        # print(data['BatteryHealthPercentage'])

        print(device_cosmetics)
        print(session['current_device'])
        # master_dict = device_cosmetics.update(session['current_device'])
        # merge cosmetic dictionary with functionality report temp stored in
        master_dict = {**device_cosmetics, **session['current_device']}
        print(master_dict)

        # Build a phone object
        test_phone = Phone(imei=session['current_device']['IMEI'],
                           scratches=device_cosmetics['scratches'],
                           dents=device_cosmetics['dents'],
                           lcd_discoloration=bool(device_cosmetics['lcd_discoloration']),
                           missing_parts=bool(device_cosmetics['components_missing']),
                           cracks=(device_cosmetics['cracked']),
                           markings=bool(device_cosmetics['markings']),
                           battery_life=int(session['current_device']['BatteryHealthPercentage'])
                           )

        grade(test_phone)
        print(test_phone.grade)

        session.clear()
        return redirect(url_for('views.dashboard', user=current_user))

    return render_template('cosmetics.html', user=current_user, data=session['current_device'])
