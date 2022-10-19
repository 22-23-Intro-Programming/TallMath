def Palindrome(sentence):
	RevSentence = ""
	for i in range(len(sentence)):
		RevSentence += sentence[len(sentence) - 1 - i]
	if RevSentence == sentence:
		return "Fantastic! " + sentence + " is a palindrome!"
	else:
		return "Unfortunately, " +sentence + " is not a palindrome!"
def main():
	stc = input("Please enter a potential palindrome: \n")
	print(Palindrome(stc))


if __name__ == "__main__":
	main()
