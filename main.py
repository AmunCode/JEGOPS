from website import create_app
from phone import Phone
from grade import grade

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

f_phone = Phone('ftest', markings=True, missing_parts=False)

b_phone = Phone('btest', markings=False, missing_parts=False, lcd_discoloration=False)
b_phone2 = Phone('btest2', markings=False, missing_parts=False, lcd_discoloration=False, scratches='small', dents='shallow', battery_life=44)
b_phone3 = Phone('btest3', markings=False, missing_parts=False, lcd_discoloration=False, scratches='large', battery_life=77)
b_phone4 = Phone('btest4', markings=False, missing_parts=True, lcd_discoloration=False, scratches='large', battery_life=79)
b_phone5 = Phone('btest5', markings=False, missing_parts=False, lcd_discoloration=False, scratches='large', battery_life=90)
b_phone6 = Phone('btest6', markings=False, missing_parts=False, lcd_discoloration=False, scratches='negligible', dents='shallow', battery_life=88)
# d_phone1 = Phone('dtest1', markings=False, missing_parts=True)
# d_phone2 = Phone('dtest2', markings=False, lcd_discoloration=True)
#
#
# c_phone = Phone('ctest', cracks='small')
# c_phone2 = Phone('ctest2', cracks='large')
# c_phone3 = Phone('ctest3', dents='deep')
# c_phone4 = Phone('ctest4', dents='shallow')


# grade(f_phone)
grade(b_phone)
grade(b_phone2)
grade(b_phone3)
grade(b_phone4)
grade(b_phone5)
grade(b_phone6)
# grade(d_phone1)
# grade(d_phone2)
# grade(c_phone)
# grade(c_phone2)
# grade(c_phone3)
# grade(c_phone4)


# print(f_phone.cosmetic_report())
print(b_phone.cosmetic_report())
print(b_phone2.cosmetic_report())
print(b_phone3.cosmetic_report())
print(b_phone4.cosmetic_report())
print(b_phone5.cosmetic_report())
print(b_phone6.cosmetic_report())
# print(d_phone1.cosmetic_report())
# print(d_phone2.cosmetic_report())
# print(c_phone.cosmetic_report())
# print(c_phone2.cosmetic_report())
# print(c_phone3.cosmetic_report())
# print(c_phone4.cosmetic_report())
