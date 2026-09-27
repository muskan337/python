lang = {

}

l1 = input("Enter your language:\n")
n1 = input("Enter your name:\n")
lang.update({l1:n1})

l2 = input("Enter your language:\n")
n2 = input("Enter your name:\n")
lang.update({l2:n2})

l3 = input("Enter your language:\n")
n3 = input("Enter your name:\n")
lang.update({l3:n3})

l4 = input("Enter your language:\n")
n4 = input("Enter your name:\n")
lang.update({l4:n4})


print(lang)

#if two names(keys) are same then no issue , it will be written twice
#if two lang(values) are same, then only one will be written