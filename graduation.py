# File:        graduation.py
# Author:      Sanaa
# Date:        nov 7, 2016
# Section:     04
# Description: YOUR DESCRIPTION GOES HERE AND HERE
#              YOUR DESCRIPTION CONTINUED SOME MORE
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 



def main():
	myInputFile = open("roster.txt", "r")
	myInputFile.read() 

    for line in myInputFile:
        # directly assign each token to a variable
        major,gpa,last_name, first_name = line.split()
        # remember to cast to another type if needed
        if ( float(gpa) < 4.0):
   			print(first_name, last_name, "is graduating with a degree in", major)
        
    
		#sanaa close file!!!!
	myInputFile close()

main()	