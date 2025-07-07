def circle_properties_get(radius, get_area=None, get_circumference=None):
	"""
	Retrieve the dimensions, such as area and circumference, of a circle if radius is given.    
	Parameters:
	radius: The length of radius of the circle.
	get_area: A flag to determine whether to calculate the area of circle. Default is true.
	get_circumference: A flag to determine whether to calculate the circumference of circle. Default is true.

	"""
	pass

def triangle_properties_get(side1, side2, side3, get_area=None, get_perimeter=None, get_angles=None):
	"""
	Retrieve the dimensions, such as area and perimeter, of a triangle if lengths of three sides are given.    
	Parameters:
	side1: The length of first side of the triangle.
	side2: The length of second side of the triangle.
	side3: The length of third side of the triangle.
	get_area: A flag to determine whether to calculate the area of triangle. Default is true.
	get_perimeter: A flag to determine whether to calculate the perimeter of triangle. Default is true.
	get_angles: A flag to determine whether to calculate the internal angles of triangle. Default is true.

	"""
	pass

tools = [circle_properties_get, triangle_properties_get]
