import random
# Ice cream and toppings
# Ice cream flavor
flavors = ["Vanilla",
        "Chocolate",
        "Strawberry",
        "Durian",
        "Sardine",
        "Banana",
        "Bacon",
		"Rheubarb",
		"Squid",
		"Avacado",
		"Cinnamon",
		"Beer",
		"Coffee",
		"Turkey",
		"Lemon",
		"Tomato",
		"Motor Oil",
		"Whikey"]

# toppings
toppings = ["Peanuts",
          "Caramel",
          "Hot Fudge",
          "Cherries",
          "Whipped Cream",
		  "Hot Sauce",
		  "Pickels",
		  "Frog Eyes",
		  "Slugs",
		  "Dirt",
		  "Fried Chicken",
		  "Spaghetti Sauce",
		  "Jalepenos",
		  "Maple Syrup",
		  "Gravy",
		  "Jelly Beans",
		  "Corn",
		  "Pineapple",
		  "beets", 
		  "French Fries",
		  "pretzels",
		  "a skunk"]
#for num in range(1,50):
def icecream():
	flavor = random.choice(flavors)
	topping1 = random.choice(toppings)
	#Don't want the same thing twice
	good = False
	while not good:	
		topping2 = random.choice(toppings)
		good = topping2 != topping1

	#print("How about some %s ice cream with %s and %s on top?" % (flavor, topping1, topping2))
	return("How about some %s ice cream with %s and %s on top?" % (flavor, topping1, topping2))
#print(icecream())