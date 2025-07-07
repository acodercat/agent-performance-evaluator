def corporate_finance_product_price(company, product):
	"""
	Fetch the current selling price of the product.    
	Parameters:
	company: The company that sells the product.
	product: The product whose price we want to fetch.

	"""
	pass

def corporate_finance_revenue_forecast(company, product, sales_units_increase_percentage=None):
	"""
	Estimate the revenue of a company by multiplying the sales units of the product with its selling price.    
	Parameters:
	company: The company that you want to calculate the revenue for.
	product: The product sold by the company.
	sales_units_increase_percentage: Percentage increase in the sales units. This value is optional and defaults to zero if not provided.

	"""
	pass

tools = [corporate_finance_product_price, corporate_finance_revenue_forecast]
