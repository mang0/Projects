#Decimal to binary
def toBinary():
	rinput = int(input("Enter your decimal number here: " ))
	print (bin(rinput))
#Binary to Decimal
def fromBinary():
	rinput = (input("Enter your binary number here: "))
	print (int(rinput,2))
#Main
def calc():
	print ("Enter 'B2D' to convert binary to decimal.")
	print ("Enter 'D2B' to convert decimal to binary.")
	rinput = input("Your choice: ")
	if rinput == 'b2d':
		fromBinary()
	if rinput == 'd2b':
		toBinary()
	else:
		print ("Woops! What was that?")
		calc()
#begin
calc()