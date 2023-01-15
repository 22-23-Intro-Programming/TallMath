
def factorial():
	print("########### Factorial Calculator ###########")
	num = int(input("Give me an integer:\n"))
	count = 1
	for i in range(num):
		count *= i+1 #because i starts with 0, and I want it to multiply by 1 at first time
	print("The factorial of " + str(num) + " is " + str(count))
	return count;
    
	
def DoubleIt():
    print("########### Double It ###########")
    Sth = input("Give me a string: ")
    New = ""
    for i in range(len(Sth)):
        New = New + Sth[i] + Sth[i] #literally, concat twice
    print("Your doubled string is " + New)
    return New

def CamelCase():
    print("########### Camel Case ###########")
    MyString = input("please enter a filename:")
    NewString = MyString.split(" ") #generate a list of words
    Result = NewString[0].lower() #the first word is lowered
    
    for i in range(len(NewString)-1):
        Result = Result + NewString[i+1].capitalize() #capitalize() only makes the first letter capitalized
    
    Result = Result.replace("-","/") #
    print("Your filename is " + Result)
    return Result


def PB2main():
    factorial()
    DoubleIt()
    CamelCase()


