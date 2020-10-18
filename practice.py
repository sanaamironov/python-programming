def add2n(n):
	if n == 1:
		return 1
	 
	return n + add2n(n-1)  

def mult(n):
	if n == 1:
		return 1
	return n * mult(n-1) 

def listsum(l,start):
	if l == []:
		return start
	x = l[0]
	rest = l[1:]    
	return x + listsum(rest,start)

def listprod(l, start):
	if l == []:
		return start	
	x = l[0]
	rest = l[1:]	
	return x * listprod(rest,start)

			   

def main():
	print(add2n(3))
	print (mult(4))
	print(listsum([1,2,3],10))
	print(listprod([1,2,3,4],0))


main()    

