def IsMultiple(num,mtp):
	if num % mtp == 0:
		return str(mtp) + " is a multiple of " + str(num)
	else:
		return str(mtp) + " is not a multiple of " + str(num)
	
def main():
	print(IsMultiple(5,2))
	print(IsMultiple(42,7))
	


if __name__ == "__main__":
	main()
