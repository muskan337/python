#Funtions to perform operations on  or manipulate strings

name = "muskan jain"

print(len(name)) #6
print(name.endswith("kan")) #true, tells whether the string "name" ends with kan or not, if yes return true else false

print(name.startswith("mus"))

print(name.capitalize()) #muskan->Muskan

str(123)
"HELLO".lower()
"hello".upper()
"hello world".capitalize() #capitalise the first character of the string

print(name.count("a"))  #count the number of occurences of any character

print(name.find("muskan"))   #finds a word and returns the idx of first occurence of the word

print(name.replace("muskan", "jain"))  #jain jain

"hello world".title() #capitalize the first character of each word in a string

" hello ".strip() #removes trailing or leading whitespace

" muskan ".lstrip() #removes leading whitespace

" muskan ".rstrip() #removes trailing whitespace 
