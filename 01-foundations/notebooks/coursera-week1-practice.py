#Exercise 1 : Create house price dataset
house_sizes = [1200,1500,1800,2000]	#sq feet
house_prices = [300000, 375000, 400000, 500000] #rupees

#Exercise 2 : create simple cost function
def compute_cost(x,y, w=0.5,b=1000):
	"""
	Compute Cost Function
	predication = w*x+b
	cost = (1/m)*sum(predication-y)^2)
	"""
	m = len(x)
	predications = [w*xi+b for xi in x]
	cost = sum((pred-yi)**2 for pred, yi in zip(predications, y))/m
	return cost
cost = compute_cost(house_sizes, house_prices)
print(f"Cost with w=0.5, b=1000: {cost}")