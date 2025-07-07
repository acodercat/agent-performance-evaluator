def map_service_get_directions(start, end, avoid=None):
	"""
	Retrieve directions from a starting location to an ending location, including options for route preferences.    
	Parameters:
	start: Starting location for the route.
	end: Ending location for the route.
	avoid: Route features to avoid. Default is none if not specified.

	"""
	pass

def geometry_area_triangle(base, height, unit=None):
	"""
	Calculate the area of a triangle.    
	Parameters:
	base: The length of the base of the triangle.
	height: The height of the triangle from the base.
	unit: The measurement unit for the area. Defaults to square meters.

	"""
	pass

def science_history_get_invention(invention_name, want_year):
	"""
	Retrieve the inventor and year of invention based on the invention's name.    
	Parameters:
	invention_name: The name of the invention.
	want_year: Return the year of invention if set to true.

	"""
	pass

tools = [map_service_get_directions, geometry_area_triangle, science_history_get_invention]
