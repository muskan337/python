a = int(input("Enter your age: "))

#if statement-1
if(a % 2 == 0):
    print("age is even")
    #end of if statement-1


#if statement-2
if(a>=18):
    print("your are above the age of consent")
    print("good for u")

elif(a<0):
    print("You are entering an invalid age")

elif(a == 0):
    print("a is not a valid age")

else:
    print("You are below the age of consent")

print("end of program")
#end of if statement-2

print("end of program")
#both if statements will run independently

#elif and else can't be alone