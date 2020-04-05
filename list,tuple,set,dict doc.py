


#List 

Properties of list:
> list can be writes in square brackets[]
> Ordering and indexing is possible
> list is mutable, we can change/update the list
> Duplicates are possible in list
example
list1 = [1,2,3,"devil",4.56]


#Methods in List

#append() 
  Adds an element at the end of the list
list1 = [1,2,3,4,5]
list1.append("devil")
print(list1)
Output - [1,2,3,4,5,"devil"

#insert() 
Adds an element at the partricalar position
list1 = [1,7,9,4,5]
list1.insert(1,7)
print(list1)
output = [1,7,9,4,5]

#Remove()
Removes the item with the specified value
list1 = [1,2,3,4,5]
list1.remove(3)
print(list1)
output = [1,2,4,5]
#pop()
Removes the element at the specified position
list1 = [1,2,3,4,5]
list1.pop(2)
print(list1)
output = [1,2,4,5]

#clear()
 Removes all the elements from the list
list1 =  [1,2,3,4,5]
list1.clear()
print(list1)
output = []


#copy() 
returns a copy of the specified list.
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list2)
Output = [1,2,3,4,5]

 
#count() 
Returns the number of elements with the specified value
list1 = [1,2,3,4,5]
list1.count(2)
print(list1)
output = 1

#extend() 
adds the specified list elements (or any iterable) to the end of the current list.
list1 = [1,2,3,4,5]
list2 = [7,8,9]
list1.extend(list2)
print(list1)
Output = [1,2,3,4,5,7,8,9]

#index() 
returns the position at the first occurrence of the specified value.
list1 = [1,2,3,4,5,6]
list2 = list1.index(3)
print(list2)
output = 2



#reverse() 
Reverses the order of the list
list1 = [1,2,3,4,5]
list1.reverse()
print(list1)
output = [5,4,3,2,1]

#Sort() 
'Sorts the list from smallest to largest
list1 = [5,3,4,1,2]
list1.sort()
print(list1)
output = [1,2,3,4,5]

                #Tuple

Properties 
> tuples writes   in round brackets()
> Ordering and indexing is possible
> tuples immutable, we cannot change/update the tuple
> Duplicates are possible in tuple
example
 tuple1 = (1,2,3,"devil")


#Methods 

#count() 
Returns the number of times a specified value occurs in a tuple
tuple1 = (1,2,3,4,4,5,6,8)
tuple1.count(4)
print(tuple1)
output = 2

#index() 
identifed the tuple for a specified value and returns the position of where it was found
tuple1 = (1,2,3,4,5)
tuple2 = tuple1.index(3)
print(tuple2)
output = 2


#Set : 

Properties 
> sets writes  in curly brackets{}
> Ordering and indexing is not possible
> sets  mutable, we can change/update the set
> Duplicates are not possible in set
example
set1 = {9,8,devil,7,6}



#Methods 

#add() 
Adds an element to the set
set1 = {1,2,3,4,5}
set1.add(6)
print(set1)
output = {1,2,3,4,5,6}

         
#discard() 
 Remove the specified item
set1 = {1,2,3,4,5,6}
set1.remove(4)
print(set1)
output = {1, 2, 3, 5, 6}
          
#clear() 
Removes all the elements from the set
set1 = {1,2,3,4,5,6}
set1.clear()
print(set1)
output = {}

#copy() 
Returns a copy of the set
set1 = {1,2,3,4,5,6}
seb2 = set1.copy()
print(set2)
output = {1,2,3,4,5,6}

#differnce() 
Returns a set containing the difference between two or more sets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = set1.difference(set2)
print(set3)
output = {1,2,3}

#difference_update() 
Removes the items in this set that are also included in another, specified set
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set1.difference_update(set2)
print(set1)
output = {1,2,3}

#discard() 
 Remove the specified item
set1 = {1,2,3,4,5,6}
set1.remove(4)
print(set1)
output = {1, 2, 3, 5, 6}

#intersection() -
Returns a set, that is the intersection of two other sets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = set1.intersection(set2)
print(set3)
output = {4,5,6}

#intersection_update() 
Removes the items in this set that are not present in other, specified set(s)
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set1.intersection_update(set2)
print(set1)
output = {4,5,6}

#isdisjoint() -
Returns whether two sets have a intersection or not
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3= set1.isdisjoint(set2)
print(set3)
Output = True
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set3 = set1.isdisjoint(set2)
print(set3)
output = False

#issubset()
Returns whether another set contains this set or not
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,5,4,8,10}
set3 = set2.issubset(set1)
print(set3)
output = True

#issuperset() 
Returns whether this set contains another set or not
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,5,4,8,10}
set3= set1.issuperset(set2)
print(set3)
output = True

#pop() 
Removes an element from the set
set1 = {1,2,3,4,5,6,7,8,9,10}
set1.pop()
print(set1)
output = {2,3,4,5,6,7,8,9,10}

#remove() 
Removes the specified element
set1 - {1,2,3,4,5,6}
set1.remove(3)
print(set1)
output = {1,2,4,5,6}

#symmetric_difference() 
Returns a set with the symmetric differences of two sets
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set3 = set1.symmetric_difference(set2)
print(set3)
output = {1,2,3,4,5,7,8,9,10}

#symmetric_difference_update() 
 the symmetric differences from this set and another
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set1.symmetric_difference_update(set2)
print(set1)
output = {1,2,3,4,5,7,8,9,10}

#union() 
Return a set containing the union of sets
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set3 = set1.union(set2)
print(set3)
output = {1,2,3,4,5,6,7,8,9,10}

#update()
Update the set with the union of this set and others
set1 = {1,2,3,4,5,6}
set2 = {6,7,8,9,10}
set1.update(set2)
print(set1)
output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#Dictionaries:

Properties of dictioanies:
> dict is a key value pair enclosed in curly brackets{:}
> Ordering and indexing is not possible
> dict mutable, we can change/update the dictionaries
> Duplicate keys are not possible but duplicate values are possible
example
dic1 = {"1":"comando","2":"gathak","3":"nsg"}

                    #dict 
#update() 
Updates the dictionary with the specified key-value pairs
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic1.update({"roopesh":"para tooper"})
print(dic1)
output = {"1":"comando","2":"gathak","3":"nsg","roopesh":"para tooper"}


#clear() 
Removes all the elements from the dictionary
dic1 = {}
dic1.clear("1":"comando","2":"gathak","3":"nsg")
print(dic1)
output = {}

#copy()
Returns a copy of the dictionary
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic2 = dic1.copy()
print(dic2)
output = {"1":"comando","2":"gathak","3":"nsg"}

#fromkeys() 
Returns a dictionary with the specified keys and value
key = {"1","2","3")
value = "para comando"
dic1 = dict.fromkeys(key,value)
print(dic1)
output = {"1":"para comando","2":"para comando","3":"para comando"}
# get() 
Returns the value of the specified key
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic2 = dic1.get("1")
print(dic2)
output= "comado"

#items() 
Returns a list containing a tuple for each key value pair
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic2 = dic1.items()
print(dic2)
output = dict_items([("1","comando"),("2","gathak"),("3","nsg")])

#keys() 
Returns a list containing the dictionary's keys
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic2 = dic1.keys()
print(dic2)
output = dict_keys([1,2,3])

#values() 
Returns a list of all the values in the dictionary
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic2 = dic1.values()
print(dic2)
output = dict_values(["comando","gathak","nsg"])

#pop() 
Removes the element with the specified key
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic1.pop("1")
print(dic1)
output = {"2":"gathak","3":"nsg"}

#popitem() 
Removes the last inserted key-value pair
dic1 = {"1":"comando","2":"gathak"
dic1.popitem()
print(dic1)
output = {"1":"comando","2":"gathak"}



#update() 
Updates the dictionary with the specified key-value pairs
dic1 = {"1":"comando","2":"gathak","3":"nsg"}
dic1.update({"roopesh":"para tooper"})
print(dic1)
output = {"1":"comando","2":"gathak","3":"nsg","roopesh":"para tooper"}




