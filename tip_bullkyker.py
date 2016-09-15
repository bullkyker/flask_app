# Calculate suggested tip for 15%, 18%, 20%
# Written by Robert Quinn 
# 17 Aug 2016
import math
#name = input("What is the customer name? ")
# ensure that a number has been entered
# while True:
	# try:
		# amount = float(input("What is the amount of the bill? $"))
		# break
	# except ValueError:
		# print("You need to enter a valid numeric amount")
#print("Hello %s your sub-total amount is $%.2f" % (name, amount))
#print("Hello %s your sub-total amount is $%.2f" % (name, amount))
#Calulations
def num(s):
    try:
        return float(s)
    except ValueError:
        return 1.00
Tips = []
def suggest_tip(amount):
	#amount = num(amount)
	#fl_amount = 85.5
	fl_amount = float(amount)
	fifteen = float(fl_amount * 0.15) 
	eighteen = float(fl_amount * 0.18) 
	twenty = float(fl_amount * 0.2) 
	Tips.append({
		    "bill_amount": str(fl_amount), 
		     "tip_amount": str("%.2f" % round(fifteen,2)),
			"percent": " for fifteen percent",
			"total": str("%.2f" %(round(fifteen,2) + fl_amount))
		})
	Tips.append({
		    "bill_amount": str(fl_amount), 
		     "tip_amount": str("%.2f" % round(eighteen,2)),
			"percent": " for eighteen percent",
			"total": str("%.2f" %(round(eighteen,2) + fl_amount))
		})
	Tips.append({
		    "bill_amount": str(fl_amount), 
		     "tip_amount": str("%.2f" % round(twenty,2)),
			"percent": " for twenty percent",
			"total": str("%.2f" %(round(twenty,2) + fl_amount))
		})
	return Tips
# mytip = suggest_tip(42.50)
# print(mytip[0])
	#return("The suggested tips for $%.2f are: 15 percent $%.2f, 18 percent $%.2f, 20 percent $%.2f" % (amount, fifteen, eighteen, twenty))
#print("The totals would be: \n\t 15 percent $%.2f, \n\t 18 percent $%.2f, \n\t 20 percent $%.2f" % (fifteen + amount, eighteen + amount, twenty + amount))
