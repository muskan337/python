# FUNCTION
# def calculate_sum(a, b): #function definition, function parameters are a and b
#    return a+b

# # calculate_sum(argument1, argument2) argument are the reall valuess passed to the fenction defintion
# sum = calculate_sum(5, 21) #func call
# print(sum)
# sum = calculate_sum(5, 29) #func call
# print(sum)
# sum = calculate_sum(5, 25) #func call
# print(sum)


# def print_hello():
#    print("hello world")

# output = print_hello()
# print(output) #none, bc jo function return me kuch return nhi karta, uska output none hota h

# def avg(a, b, c):
#  average = (a+ b+ c)/3
#  print(average)
#  return average
 
# avg(5, 10, 15)
# print("apna college")  
# print("apna college", end="$") #sep= " "
# print("muskan jain") #end = "\n"

# built-in functions - print(), len(), type(), range()
# user defined functions- 

    #   DEFAULT FUNCTIONS:
# def cal_prod(a, b=1): #it can never be (a=1, b) , (non-deffault, default)--> alwayss
#    print(a*b)
#    return a*b

# cal_prod(2)


# cities = ["hodal", "palwal", "pune", "mumbai", "chennai"]

# # def leng_th(list):
# #     print(len(list))

# # leng_th(cities)


# def line(list):
#     for item in list:
#         print(item, "," , end=" ")

# line(cities)        

 #                     RECURSSION 
# recurssion a func which repeats itself 
# def show(n):
#     if(n== 0):
#        return
#     print(n)
#     show(n-1)

# show(5)    

# def fac(n):
#     if (n == 0 or n== 1):
#         return 1
#     else:
#         return n * fac(n-1)

# print(fac(4))

# def sum(n):
#     if(n == 0):
#         return 0
#     return n + sum(n-1)

# print(sum(6))

def List(list, idx):
     if(idx == len(list)):
          return
     print(list[idx])
     print(idx)
     List(list, idx+1)

Name = ["mmuskan", "pragya", "riddu"]

List(Name, 0)