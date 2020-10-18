#testswhether myString is a palindrome

def isPalindrome(myString):
 
	tempString = myString
	length = len(tempString)
	half = length/2
	half = int(half)
	
	isPalindrome=True
	for i in range(half+1):
		if myString[i] != myString[length-i-1]:
			isPalindrome = False

#no errors below this line
def main():
	print("Should print: True\nPrints: ",end="")
	isPalindrome("oozyratinasanitaryzoo")
	print("Should print: False\nPrints:", end="")
	isPalindrome("18101181")
main()