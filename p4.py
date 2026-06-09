#dictionary --> a pair of word <-> meanings
                           #key --> word
                           #value --> meaning
# dictionaries are used to store values in key:value pairs, they are unordered, mutable, don't allow duplicate keys.
#info = {
    # "key": value
#     "name" : "muskan",
#     "learning" : "coding",
#     "age" : 19,
#     "subjects" :  ["python", "C++", "C"],
#     "is_adult" : True,
#     "tupple" : ("na", 1)
# }

# print(type(info))
# print(info["name"])
# print(info["learning"])
# print(info["age"])

# info["name"] = "Muskan" #to edit --> overwrrite
# info["surname"] = "Jain" #to add
# print(info)

# null_dict = {} #empty dictionary
# print(null_dict)
# null_dict["name"] = "msukan"
# print(null_dict)

   #NESTED DICTIONARIEs
# student = {
#       "name" : "dolly",
#       "subjects" : {
#           "phy" : 98,
#           "chem" : 100,
#             "maths" : 100
#       }
#    }

# print(student)
# print(student["subjects"])
# print(student["subjects"]["phy"])

# print(student.keys()) #to print keys of a dictionary, it will return a dict_keys object which is an iterable, we can convert it to a list if we want to access individual keys.
# print(list(student.keys()))
# print(len(list(student.keys()))) #to print total np. of key<-> value papers
# print(student.values())
# print(student.items()) # returns all the key, value pairs in the form of tupple 
# pairs = list(student.items())
# print(pairs[0])
# print(len(student))# total no. of key values
# print(student.get("name"))      # to get value of particular key
# print(student.get("name2"))# no error if key is not present, it will return None
#print(student["name2"])     # will raise a KeyError if key is not present
#print(student["name2"]) #error
# it will raise a KeyError if key is not present, because we are trying to access a key that does not exist in the dictionary. To avoid this error, we can use the get() method which will return None if the key is not present in the dictionary.

#also to avoid this situation, we can do smthng like this :
# print("BEFORE")
# print(student["name2"]) #error      ---> not working
# print("AFTER") 

# student.update({"city": "mumbai"})
# print(student)


# new_dict = {"name": "muskan jain", "city" : "delhi", "age" : 16} 
# student.update(new_dict)

# print(student)
#no duplicate, only overwrite 

                   #            SETS
#collection of unordered items, each element must be unique & immutable but sets are mutable, we can add or remove items from a set but we can't change the value of an item in a set because they are immutable.
# we can store boolean , int, float, str, tuple but we can't store list and dictionary in a set because they are mutable.
         
# col = {1, 2, 3, 4, "hello", "world", "world", 2} #in case of duplicate values set will ignore them and won't show any error 
# print(col)        
# print(type(col))        
# print(len(col)) # it will give total number of items, it will also ignore the counting of duplicate numbers 
#empty set
# set = set()
# set.add(1)
# set.add(2)
# set.add(3)
# set.add("muskan jain")
# set.add((1, 2, 3))
# set.add("apple")
#set.add([1, 2, 3])  --> it will give error saying unhahable type list
#set.remove(1)
#set.remove(6)# it will raise a KeyError because we are trying to remove an element that is not present in the set. To avoid this error, we can use the discard() method which will not raise an error if the element is not present in the set.
# list can be changed so the are unhashable that's why they can't be added in a set
 
# print(type(set))
# print(len(set))

# #set.clear()
# print(set)

# sellu = {"apple", "banana", "orange"}
# print(sellu.pop())

# sellu.pop()
# print(sellu)

# set.union(sellu) #combines both set values & returns new -> return unique values

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4}

# print(set1.union(set2)) #{1, 2, 3, 4}
# print(set1.intersection(set2)) #combines common values & returns new  --> {2, 3, 4} --> counts common vlues only once

# print(set1)
# print(set2)


# dict = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
# }


# set = {"python", "java", "C++", "python", "javascript", "java", "C++", "C"}
# print(len(set))

dict = {}

x = int(input("enter phy : "))
dict.update({"phy" : x})

x = int(input("enter chem : "))
dict.update({"chem" : x})

x = int(input("enter maths : "))
dict.update({"maths" : x})

print(dict)

# values = {9, "9.0", 9.25}
# print(values)
# print(len(values))

values = {
    ("float", 9),
    ("int", 9)
}
print(values) #python considers 9 and 9.0 a same 