"""                                            DAY 3 Of Learning Python 
"""


                                        #LISTs IN PYTHON 
"""
List created by [], and we can store elements of different types (like integer, float, string, etc.)
In list we can change the value but in string we can not change the values. means list are mutable.
"""
student= ["AMIT TOMAR", 99.43, "DELHI"]
print(student)
                      
marks= [23,45,38,90,92,00]
print(marks)
print(marks[0])

marks[0]= 21
print(marks)

""" LIST Slicing
SYNTAX : list_name[starting_index : end_index]
"""
print(marks[2 : 4])

                                    #LIST Methods

list= [2,5,1,3]

list.append(4) #it adds one element at the end
print(list)

list.sort() #arrange in assending order
print(list)

list.sort(reverse=True) #arrange in desending order
print(list)

list.reverse() #reverse list
print(list)

list.insert(5,21) #insert element at index 
print(list)

list.remove(5)
print(list)



                                        #TUPLES IN PYTHON

"""
Tuple created by (), and tuple are immuatable means unchangable. Slicing in tuple similar like list, but some different methods are given
below:
"""

                                        #Tuple Methods

tup= (9,1,7,)

print(tup.index(7))
print(tup.count(9))

#DAY 3 COMPLETED








