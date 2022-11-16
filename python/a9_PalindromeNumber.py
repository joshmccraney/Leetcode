from reverse import rev

def pal(num):
	isPal = num - rev(num) == 0
	return isPal

# DRIVER CODE
num = 16761
print(pal(num))