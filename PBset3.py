def CurrencyConversion():
    CvList = ["US Dollar","Chinese Yuan","European Euro","Turkish Lira"]
    CvFactors = {"US Dollar": 1.00,
                 "Chinese Yuan": 7.28,
                 "European Euro": 1.01,
                 "Turkish Lira": 18.60,
                 }
    print("What currency do you currently HAVE?\n1. US Dollar\n2. Chinese Yuan\n3. European Euro\n4. Turkish Lira")
    From = input("Please enter a number: ") 

    print("How much do you have?")
    value = input("Please enter the value: ")

    print("What currency do you want to convert TO?\n1. US Dollar\n2. Chinese Yuan\n3. European Euro\n4. Turkish Lira")
    To = input("Please enter a number: ")

    value = float(value) / CvFactors.get(CvList[int(From)-1]) * CvFactors.get(CvList[int(To)-1])
    print("You have " + str(value) + " " + CvList[int(To)-1])

def GroceryList(List):
    total = 0.0
    purchasedStuff = ""
    GlPrices = {"Apple" : 1.50,
                "Orange" : 1.00,
                "Banana" : 1.00,
                "Bagel" :1.25,
                "Milk" : 2.75,
                "Eggs" : 3.25,
                "Cake" : 8.00,
                "Pasta" : 3.50,
                "Donuts" : 5.00,
                "Cup Noodles" : 1.25,}
    for x in range(len(List)):
        total += GlPrices.get(List[x])
        purchasedStuff += List[x] +" "
    print(purchasedStuff)
    print("Your total is: " + str(total) + " dollars")
    
     
def main():
    #CurrencyConversion()
    GroceryList(["Apple","Banana", "Cup Noodles", "Donuts"])
    


if __name__ == "__main__":
    main()
