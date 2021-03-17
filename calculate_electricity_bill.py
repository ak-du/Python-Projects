# Calculating electricity bill

unit = 30
charge = 0

if unit <= 50:
    charge = unit * 0.50

if 50 < unit <= 150:
    charge = charge + (100 * 0.75)

elif 150 < unit <= 250:
    charge = charge + (100 * 1.20)

elif unit > 250:
    charge = charge + ((unit - 250) * 1.50)
additional_surcharge = (charge * 20) / 100
electricity_bill = charge + additional_surcharge
print('Your electricity bill is ', electricity_bill)
