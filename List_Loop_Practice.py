def problem1(list):

    for i in range(len(list)-1):
        if list[i] == 7 and list[i] == list[i+1]:
            return True
    return False

def problem2(list):
    total = 0
    for i in range(len(list)-1):
        if list[i] == 0:
            return total
        total += list[i]

    return total

def problem3(list):
    IsBetween = False
    total = 0
    for i in range(len(list)-1):
        if list[i] == 2 and IsBetween == False:
            IsBetween = True
            continue
        elif list[i] == 3 and IsBetween == True:
            IsBetween = False
            continue
        elif IsBetween == True:
            continue
        
        total += list[i]
    return total


def main():
    print("The result for the first problem is " + str(problem1([1,2,3,7,7])))
    #input1 = [1,2,3,7,7]
    #input2 = [1,7,2,7]
    #input3 = [7,8,7]  here are the options for test <3
    
    print("The result for the second problem is " + str(problem2([1,4,0,3,6])))
    #input1 = [1,4,0,3,6]
    #input2 = [1,20,12,8,0,8,10]
    #input3 = [0,3,4,5,6,7,8,9,10]
  
    print("The result for the third problem is " + str(problem3([1,5,6,2,99,3])))
    #input1 = [1,4,4]
    #input2 = [1,5,6,2,99,3]
    #input3 = [1,3,4,2,3,8]   
    
    
    
if __name__ == "__main__":
    main()


