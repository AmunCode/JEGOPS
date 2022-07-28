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
        try:
            battery = int(request.form.get('battery'))
        except ValueError:
            session['current_device']['BatteryHealthPercentage'] = '0'

        device_cosmetics['scratches'] = request.form.get('scratches')
        device_cosmetics['dents'] = request.form.get('dents')

        if request.form.get('lcd-discoloration') == 'True':
            device_cosmetics['lcd_discoloration'] = True
        else:
            device_cosmetics['lcd_discoloration'] = False

        if request.form.get('missing-components') == 'True':
            device_cosmetics['components_missing'] = True
        else:
            device_cosmetics['components_missing'] = False

        if request.form.get('cracks') == 'True':
            device_cosmetics['cracked'] = True
        else:
            device_cosmetics['cracked'] = False

        if request.form.get('markings') == 'True':
            device_cosmetics['markings'] = True
        else:
            device_cosmetics['markings'] = False
        # device_cosmetics['cosmetic_data'] = request.form.to_dict()
        # print(data['BatteryHealthPercentage'])

        print(device_cosmetics)
        print(device_cosmetics['lcd_discoloration'])
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

        print(type(test_phone.lcd_discolored))

        grade(test_phone)
        print(test_phone.grade)

        session.clear()
        return redirect(url_for('views.dashboard', user=current_user))

    return render_template('cosmetics.html', user=current_user, data=session['current_device'])
