#elctric bill
# 0 to 100 units – free of cost.
# For 0 to 500 units – first 100 units free, for next 101 to 200 units Rs.2.25 per unit, for next 201 to 400 units Rs.4.5 per unit, for balance Rs.6 per unit.
# For above 500 units – first 100 units free, for next 101 to 400 units Rs.4.5 per unit, for next 401 to 500 units Rs.6 per unit, for next 501 to 600 units Rs.8 per unit, for next 601 to 800 units Rs.9 per unit, for next 801 to 1000 units Rs.10 per unit,for balance Rs.11 per unit.
# [3:30 PM] Get the current month reading as an input from the user.
# [3:30 PM] Write a function to calculate the current_consumption_cost
# [3:30 PM] Arg of the function is consumption_units

def bill_amount(consumption_units):
    amount=0
    temp_amount=0
    temp_unit=0
    unit_101_to_200= 2.25
    unit_201_to_400=  4.5
    unit_balance=6

    
    units_101_to_400 =4.5
    units_401_to_500_units=6
    units_501_to_600= 8 
    unit_601_to_800=9 
    unit_801_to_1000=10 
    unit_for_balance=11

    if consumption_units <= 100 :
        return "the bill amount is {} rupees".format(amount)

    elif consumption_units > 100 and consumption_units  <= 500:

        if consumption_units <=200 :
            temp_unit=consumption_units-100 
            amount=temp_unit*unit_101_to_200
            return "the bill amount is {} rupees".format(amount)
        elif consumption_units <=400:
            temp_unit=consumption_units-200
            amount=(temp_unit*unit_201_to_400)+(100*unit_101_to_200)
            return "the bill amount is {} rupees".format(amount)
        else:
            temp_unit=consumption_units-400
            amount=(temp_unit*unit_balance)+(200*unit_201_to_400)+(100*unit_101_to_200)
            return "the bill amount is {} rupees".format(amount)

    elif consumption_units > 500 :

        if consumption_units <=400 :
            temp_unit=consumption_units-100 
            amount=temp_unit*units_101_to_400
            return "the bill amount is {} rupees".format(amount)
        elif consumption_units <=500:
            temp_unit=consumption_units-400
            amount=(temp_unit*units_401_to_500_units)+(400*units_101_to_400)
            return "the bill amount is {} rupees".format(amount)
        elif consumption_units <=600:
            temp_unit=consumption_units-500
            amount=(temp_unit*units_501_to_600)+(100*units_401_to_500_units)+(400*units_101_to_400)
            return "the bill amount is {} rupees".format(amount)
        elif consumption_units <=800:
            temp_unit=consumption_units-600
            amount=(temp_unit*unit_601_to_800)+(100*units_501_to_600)+(100*units_401_to_500_units)+(400*units_101_to_400)
            return "the bill amount is {} rupees".format(amount)
        elif consumption_units <=1000:
            temp_unit=consumption_units-800
            amount=(temp_unit*unit_801_to_1000)+(200*unit_601_to_800)+(100*units_501_to_600)+(100*units_401_to_500_units)+(400*units_101_to_400)
            return "the bill amount is {} rupees".format(amount)
        else:
            temp_unit=consumption_units-1000
            amount=(temp_unit*unit_for_balance)+(200*unit_801_to_1000)+(200*unit_601_to_800)+(100*units_501_to_600)+(100*units_401_to_500_units)+(400*units_101_to_400)
            return "the bill amount is {} rupees".format(amount)


consumption_unit=eval(input("enter the consumption units : "))
print(bill_amount(consumption_unit))
