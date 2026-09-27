# a = 12
# b = 45
# c = 56
# average = (a+b+c)/3
# print(average)

# def avg():
#     a = int(input("Enter your nukmber:"))
#     b = int(input("Enter your nukmber:"))
#     c = int(input("Enter your nukmber:"))
#     d = int(input("Enter your nukmber:"))

#     average = (a+b+c+d)/4
#     print(average)

# avg()    
# avg()    
# avg()    
# avg()    
# avg()    

# A FUNCTION IS A GROUP OF STATEMENTS USED TO PERFORM SPECIFIC TASKS
# A FUNCTIIIN CAN BE REUSED BBY THE PROGRAMMER IN A GIVEN PROGRAM ANY NUMBER OF TIMES

def func1():
    print("Hello!!!!")

func1()   #function call   

# def goodDay(name, ending ):  #funnc with arguments
#     print("Good Day, " + name)
#     print(ending)

# goodDay("Harry", "Thank You")     

def goodDay(name, ending = "Thank You" ):  #funnc with arguments
    print(f"Good Day,  {name}")
    print(ending)

goodDay("Harry")     #output wiill be thank you
goodDay("Muskan", "THanks")      # output will be thanks