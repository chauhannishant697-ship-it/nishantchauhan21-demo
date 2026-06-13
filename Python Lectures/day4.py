"""
This is DAY 4 of Learning Python
"""
 
                                    #DICTIONARY
"""
We can create dictionary by { "key" : "value" },
1.They are also mutable means changable.
2.They are unordered.
3.We can not create duplicate keys
"""

info= {"name" : "nishant" , "sub": "jaVA", "age": 21, 
"Class" : "B.Sc 3rd Year", 
"Marks" : 89
}

print(type(info))
print(info)

#We can also print our values like this:
print(info["age"])
print(info["name"])
print(info["Marks"])

#We can change or add new values in dictionary:

info["name"] = "Nikki"
info["surname"] = "Chauhan"

print(info)

                                                 #Nested Dictionary
"""
It means mini dictonary in the  Dictionary.
"""              
Student= { 
    "name": "Nishant", 
    "age": 25,
    "sub": 
{
    "Phy": 98, "Bio": 95, "Chem": 97
},
    "Address": "Bahadurgarh"

}
 
print(Student)

                                                #Dictionary Methods

Student= { 
    "name": "Nishant", 
    "age": 25,
    "sub": 
{
    "Phy": 98, "Bio": 95, "Chem": 97
},
    "Address": "Bahadurgarh"

}                                   

#1.
print(Student.values()) #it returns all values in dictionary.

#2.
print(Student.keys()) #it returns all keys in dictionary.
 
#3.
print(Student.items()) #it returns all (key & value) in a form of tuple.

#4.
print(Student.get("age")) #return key according to value. Here if we write any wrong key so we can not get error,we get None value and after this remaning codes run properly.

#5. 
Student.update({"friend" : "RAJ"}) #It can add (key and value) in dictionary.
print(Student)


#To create empty dictionary we can write like this:
empty_dict = {}
print(empty_dict)   




                                        # SET IN PYTHON
"""Set is created by { } and set are Immutable AND they are unordered and they do not allow Duplicate values.
"""                                        
myset= {1,2,2,5,5,"Nishant", "Nishant"}
print(myset)
print(len(myset)) #it returns the length of set

#To create empty set we can write like this:
empty_set = set()

print(empty_set)

                                      #SET Methods
myset= {1,2,2,5,5,"Nishant", "Nishant"}

#1.
myset.add("RAJ") #it adds one element in set.
print(myset)

#2.
myset.remove(2) #it removes the element from set.
print(myset)

#3.
myset.pop() #it removes the random element from set.
print(myset)

#4.
myset.clear() #it clears the set.

#5. 
set1= {1,3,5}
set2= {1,4,5,6,6,2}
print(set1.union(set2)) #it returns the union of two sets.

#6.
print(set1.intersection(set2)) #it returns the intersection of two sets.


"""
DAY 4 COMPLETED
"""