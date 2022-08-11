def grade(phone):
    if phone.marked or phone.battery_condition < 30:        # options: True or False
        phone.grade = 'F'
        return
    elif phone.f_cracked or phone.r_cracked:                                     # option: None, small, large
        if phone.f_cracked == 'small' or phone.r_cracked == 'small':
            phone.grade = 'D'
            return
        elif phone.f_cracked == 'large' or phone.r_cracked == 'large':
            phone.grade = 'F'
            return
    elif phone.missing_parts or phone.lcd_discolored:       # options: True or False
        phone.grade = 'D'
        return
    elif phone.dent_condition != 'None':
        if phone.dent_condition == 'Small':
            phone.grade = 'C'
        else:
            phone.grade = 'D'
            return
    elif phone.scratch_condition or phone.spotting:
        if phone.scratch_condition == 'light' or phone.spotting == 'None':
            phone.grade = 'A'
        elif phone.scratch_condition == 'medium' or phone.spotting == 'small':
            phone.grade = 'B'
            return
        else:
            if phone.battery_condition >= 79:
                phone.grade = 'C+'
                return
            else:
                phone.grade = 'C'
                return

    if phone.battery_condition >= 0:
        if phone.battery_condition > 79:
            phone.grade = 'A'
        elif phone.battery_condition > 74:
            phone.grade = 'B'
        elif phone.battery_condition > 66:
            phone.grade = 'C'
        else:
            phone.grade = 'D'



