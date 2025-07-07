def hilton_hotel_check_availability(location, check_in_date, check_out_date, no_of_adults, hotel_chain='Hilton'):
	"""
	Check hotel availability for a specific location and time frame.    
	Parameters:
	location: The city where you want to check hotel availability.
	check_in_date: The check-in date in the format YYYY-MM-DD.
	check_out_date: The check-out date in the format YYYY-MM-DD.
	no_of_adults: The number of adults for the hotel booking.
	hotel_chain: The hotel chain where you want to book the hotel.

	"""
	pass

def lawsuits_search(company_name, location, year, case_type=None):
	"""
	Search for lawsuits against a specific company within a specific time and location.    
	Parameters:
	company_name: The name of the company.
	location: The location where the lawsuit was filed.
	year: The year when the lawsuit was filed.
	case_type: The type of the case. Options include: 'civil', 'criminal', 'small_claims', etc. If not specified, default to search for all types.

	"""
	pass

tools = [hilton_hotel_check_availability, lawsuits_search]
