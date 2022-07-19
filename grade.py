def grade(phone):
    if phone.marked or phone.battery_condition < 30:        # options: True or False
        phone.grade = 'F'
        return
    elif phone.missing_parts or phone.lcd_discolored:       # options: True or False
        phone.grade = 'D'
        return
    elif phone.dent_condition:                              # options: None, shallow, deep
        if phone.dent_condition == 'shallow':
            phone.grade = 'C'
        else:
            phone.grade = 'D'
            return
    elif phone.cracked:                                     # option: None, small, large
        if phone.cracked == 'small':
            phone.grade = 'D'
        else:
            phone.grade = 'F'
        return
    elif phone.scratch_condition:
        if phone.scratch_condition == 'negligible':
            phone.grade = 'A'
        elif phone.scratch_condition == 'small':
            phone.grade = 'B'
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


