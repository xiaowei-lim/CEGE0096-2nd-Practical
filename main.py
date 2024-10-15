def main():
	# Task 1: User Input/System Output
	# Retrieve input from user
	input_easting = input('Please input your current location EASTING: ')
	input_northing = input('Please input your current location NORTHING: ')

	# Converts user input to integer, else prompt for correct input.
	# Checks if within bounding box
	try:
	    user_easting = int(input_easting)
	    user_northing = int(input_northing)
	    if user_easting < 430000 or user_easting > 465000:
	        print('Easting coordinates are out of bounds.')
	    elif user_northing < 80000 or user_northing > 95000:
	        print('Northing coordinates are out of bounds.')
	    else:
	        print(f'Thank you! Your current coordinates ({user_easting}, {user_northing}) are within bounds.')
	except:
	    print('Please key in integers only.')

    # Task 2: Triplet Orientation
    def triplet_orientation(p, q, r):
	    # Splits up x and y coords into inputs
	    xp = p[0]
	    yp = p[1]
	    xq = q[0]
	    yq = q[1]
	    xr = r[0]
	    yr = r[1]
	    # Equation for orientation
	    val = (yq-yp)*(xr-xq) - (xq-xp)*(yr-yq)
	    if val > 0:
	        return 'Clockwise turn'
	    elif val < 0:
	        return 'Counterclockwise turn'
	    else:
	        return 'Colinear'


if __name__ == '__main__':
	main()