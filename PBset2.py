
def factorial():
	print("*********************************")
	print("Welcome to Factorial Calculator!")
	print("*********************************")
	print("\n")
	num = int(input("Give me an integer:\n"))
	count = 1
	for i in range(num):
		count *= i+1
	print("The factorial of " + str(num) + " is " + str(count))
	return count;
    
	
def DoubleIt():
    print("*********************")
    print("Welcome to Double It!")
    print("*********************")
    Sth = input("Give me a string: ")
    New = ""
    for i in range(len(Sth)):
        New = New + Sth[i] + Sth[i]
    print("Your doubled string is " + New)
    return New

def CamelCase():
    print("**********************")
    print("Welcome to Camel Case!")
    print("**********************")
    MyString = input("please enter a filename:\n")
    NewString = MyString.split(" ")
    Result = NewString[0].lower()
    
    for i in range(len(NewString)-1):
        Result = Result + NewString[i+1].capitalize()
    
    Result = Result.replace("-","/")
    print("Your filename is " + Result)
    return Result


def main():
    factorial()
    DoubleIt()
    CamelCase()

if __name__ == "__main__":
	main()
