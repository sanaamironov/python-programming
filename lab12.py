                                                                                                                             
# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE                                                                                                                            
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE                                                                                                                                     


# flight() recursively calculates the path of a hailstone                                                                                                                          
# Input:   the height of the hailstone                                                                                                                                             
# Output:  a recursive call, which at the end returns the number of "steps"                                                                                                        
#          taken for the hailstone to reach a height of 1                                                                                                                          
def flight(height):
	#### base case(s)                                                                                                                                                              
	# print out an "invalid" message and return 0 
	if height <= 0:
		print("invalid height of ", height)
		return 0

	# stops when it reachs height of 1 (the ground)                                                                                                                                
	if height == 1:
		print("height of", height)
		return 0
	#### recursive case(s)                                                                                                                                                         
	# if the current height is even, divide it by 2 
	elif height % 2 == 0:
		print("height of", height)
		return (1 + flight(height // 2))

	else:
		# if the current height is odd, multiply it by 3, then add 1                                                                                                                   
		print("height of", height)
		return (1 + flight(height * 3 + 1)) 
   
 
def main():

	print("Welcome to the Hailstone Simulator!")
	startHeight = int(input("Please enter a height for the hailstone to start at: "))
		
	# initial recursive call goes here                                                                                                                                             
	steps = flight(startHeight)
	print("\nIt took", steps, "steps to hit the ground.")

	print("Thank you for using the Hailstone Simulator!\n")

main()