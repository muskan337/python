n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))
n4 = int(input("Enter the number 4: "))

if(n1>n2 and n1>n3 and n1> n4):
    print("Greatest no. is n1: ", n1)
    
elif(n2>n1 and n2>n3 and n2> n4):
    print("Greatest no. is n2: ", n2)
if(n3>n2 and n3>n1 and n3> n4):
    print("Greatest no. is n3: ", n3)
if(n4>n2 and n4>n3 and n4> n2):
    print("Greatest no. is n4: ", n4)
