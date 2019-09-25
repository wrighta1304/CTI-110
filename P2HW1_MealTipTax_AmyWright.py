# Meal Tip and Tax Calculator
# September 24, 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Amy Wright
#
meal = float(input('How much did your meal cost?'))
total_cost = meal + (meal * .06) + (meal * .15)

print('Your total meal cost is:$ %.2f' % total_cost)
