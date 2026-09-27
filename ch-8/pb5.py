def rem(l, word):
    n = [ ]
    for item in l:
       if not(item == word):
           n.append(item.strip(word))
    return n   


l = ["Harry", "muskan", 1, 5, 6, 7, 8, "an"]

print(rem(l, "an"))