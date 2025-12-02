#Python Mutable Objects: Lists, Dictionaries, and Sets

shopping_list = ["milk ",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

#chain assignment
a = b = c = d = e = f = another_list
print(a)
print("adding cream")
b.append("cream")
print(c)
print(d)
