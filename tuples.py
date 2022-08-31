# animals = ("Dog", "Cats", "Cows")

#animals = "Dogs", "Cats", "Cows"

#print(type(animals))


# Accessing tuple elements using indexing
#tuple_with_ints = (1, 2, 3)
#print(tuple_with_ints[0]) # 1
#print(tuple_with_ints[1]) # 2
#print(tuple_with_ints[2]) # 3

# IndexError: list index out of range
#print(tuple_with_ints[3])

# Accessing nested tuples
#tuple_with_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#print(tuple_with_tuples[0][0]) # 1
#print(tuple_with_tuples[1][1]) # 5
#print(tuple_with_tuples[2][2]) # 9

from re import I


my_tuple = (("python", "C++", "C#"), (1,5,8), "Frode")

#for item in my_tuple:
    #if isinstance(item, tuple) or isinstance(item, list):
        #for x in item:
           # print(x)
   # else:
       # print(item)

#Dictionaries
my_dict = {}

my_dict = {1: "Apple", 2: "Banana", "Likes": ["Music", "Soccer"] }


print(my_dict["Likes"][1])