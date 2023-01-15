def Greeting(): #establish Greeting method
    print("########### Greeting :) ###########")
    name = input("Please enter your name: \n") #get an input
    print("Oh, " + name + ", is it? It is nice to meet you!") #use "+" to concat multiple strings
    print("Have a good day!")

def IsMultiple():
    print("########### IsMultiple ###########")
    num = int(input("Please input the first number"))
    mtp = int(input("Please input the second number"))
    if mtp % num == 0:
        print(str(mtp) + " is a multiple of " + str(num))
    else:
        print(str(mtp) + " is not a multiple of " + str(num))

def Palindrome():
    print("########### Palindrome ########### ")
    sentence = input("Please enter a potential palindrome: \n")
    RevSentence = ""
    for i in range(len(sentence)):
        RevSentence += sentence[len(sentence) - 1 - i]
    if RevSentence == sentence:
        print("Fantastic! " + sentence + " is a palindrome!")
    else:
        print("Unfortunately, " +sentence + " is not a palindrome!")






def PB1main():
    Greeting()
    IsMultiple()
    Palindrome()

