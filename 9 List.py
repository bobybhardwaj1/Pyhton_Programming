 # list is a class, list is an iterable sequence, list is mutable, list is growable
 # list can store hetrogeneous data, list element is indexed

 # LIST STRUCTURE:-- 

 l=[1,2,3,4,5,6]
 print(l)
 print(l[1])
 print(l[-1])

 # Assesing list element with for loop
 for i in l:
     print(i, end=" ")

 # with while loop
 i=0
 while i<=5:
     print(l[i], end=" ")
     i+=1
  
  
 # For deleting an element from the list  
 del l[0]
 print(l)


 # For edit an element in the list
 l[2]=8
 print(l)

 # for adding an element in the list
 # 1.append() 2.insert()
 l.append(9)
 print(l)
 l.insert(2,7)
 print(l)

 # Built in methods
 # 1 max() for finding the maximum element in list
 # 2 min() for finding the minimum element in list
 # 3 sum() for finding sum of the elements of the list
 # 4 sorted() for sorting the list
 # 5 len() return lengthb of specified iterable

 # example -- 
 print(len(l))

 print(min(l))

 print(max(l))

 print(sum(l))

 print(sorted(l))

 # we can take input like these in list
 l=list(range(5))
 print(l)

 # list concatenation
 l1=[1,2,3,4]
 l2=[4,5,6,7]
 print(l1+l2)

 #  List Repetition
 l=[2,3,4]
 print(l*2)  # out-- [2, 3, 4, 2, 3, 4]


 # List of Lists
 l=[[1,2,3],[4,5,6],7]
 print(l[1][2]) # Access the element of list of lists

# List Object Methods--
""" 
1. list.append(value)
2. list.insert(index,value)
3. list.remove(value)
4. list.pop() remove value from last and return it
5. list.clear()  empty the list
6. list.reverse() reverse the list
7. list.index(value) give the index of the value in the list
8. list.count(value) count the frequency of the value in the list
9. list.sort() sort the list
"""


# List Comprehension
# structure-- [expression for variable in iterable ]
# example--
print([a for a in range(5)])
print([3+4 for a in range(5)])

print([a**2 for a in range(2,10,2)])
