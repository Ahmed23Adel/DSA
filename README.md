Most important data structures, associated with very optimized sorting, and searching algrothims.

# Data structure:</br>
1.**ArrayList** </br>
2.**LinkedList**</br>
3.**stack implemented with array (ArrayStack)**</br>
4.**stack implemented with linkedList (LinkedStack)**</br>
3.**Queue implemented with array (ArrayQueue)**</br>
4.**Queue implemented with linkedList (linkedQueue)**</br>
5.**binary serach tree, implemented by Linked list (LinkedBinarySearchTree)**</br>

# Sorting Algorithms:</br>
1**selection**</br>
2.**insertion**</br>
3.quick sort**</br>
4.**counting sort**</br>

# searching algorithms:</br>
1.**sequential**</br>
2.**binary**</br>


## ArrayList:
 A list represented by array</br>
**advantages**:</br>
1.-Access any element ay any index O(1)</br>
2.inserting/deleting an element at the end of arry is O(1)</br>
3.fixed size array,cannot be changed after intialization, so it doesn't resize at each addition </br>

**disadvantages**:</br>
1. insertion at the first of array will all elements taking O(N)</br>
2. size cannot be changed if needed more space.</br>

# most important algorithms
1-  get_free_space(self): Get count of free spaces in the array.</br>
2-add (self,val): Adding element at the end of the array if not filled</br>
3- remove_at(self, k):  Remove item in array at index k, meaning it will shift elemens to the left</br>
4- remove_all_indicies(self, lst_removable): Given a list of indices, remove all indecied in it.</br>
5- contains(self, searchable): Checking if array containg specific value.</br>
6-index_of(self, searchable): return the index if desired element:</br>
7-replace(self, replaced, to): replace all items in arry with specific value "replaced" to "to"</br>
8-def print_all(self): Printing all items of array</br>
9- to_numpy(self, type=np.int32): return numpy array with size equal size of inserted elements with type equal to type</br>
10- to_serties(self,type=np.int32): Return series compatible with pandas </br>
11 some methods </br>
  1-__add__</br>
  2-__radd__</br>
  3-__sub__</br>
  4-__rsub__</br>
  5-__mul__</br>
  6-__rmul__</br>
  7-__iadd__</br>
  8-__contains__</br>
  9-__iter__</br>
  10-__deepcopy__</br>
  11-__str__</br>
  
it supports sorting algorithms: </br>
  1-sort_selection</br>
  2-sort_insertion</br>
  3-sort_quick</br>
  4-sort_count</br>
  
it supports searching algorithms: </br>
  1-search_sequential</br>
  2-search_binary</br>
  
  
  Example:</br>
  ```
a1=ArrayList(max_size=10)</br>
a1.add(6)</br>
a1.add(55)</br>
a1.add(10)</br>

a2=ArrayList()</br>
a2.add(1)</br>
a2.add(12)</br>
a2.add(9)</br>

x=a1+a2</br>
print(x)</br>
x=x*10</br>
print(x)</br>

x.sort_quick()</br>
print(x)</br>
```
output:</br>
index 0 :7</br>
index 1 :67</br>
index 2 :19</br>

index 0 :70</br>
index 1 :670</br>
index 2 :190</br>

index 0 :70</br>
index 1 :190</br>
index 2 :670</br>




## LinkedList:
    Advantages:
    1-no max limit fot the limlit
    2-

    disadvantages
    1-
List representaed by linked list</br>
**advantages**:</br>
1.no max limit fot the limlit</br>
2.  you can add as many elements as needed.</br>

**disadvantages**:</br>
1inserting/deleting at the end of the list, it will take O(N)</br>

# most important algorithms
1.add (self,val): Adding element at the end of the array if not filled</br>
2. add_at(self, k): setting new item at position k with value equal value. if at k position there is a node, it shifts them to left</br>
3.add_all(self,values): add all value in values, .</br>
4.add_first(self, val): adding item at head.</br>
5. add_last(self, val): adding item at last index.</br>
6.get_at(self,k): Returns value at index k</br>
7. get_first(self): returns the value of head.</br>
8. get_last(self):   returns the value of last element.</br>
9. index_of(self, searchable): Return the index of what is searched for </br></br>
10.  remove_at(self, k): remove node at index k</br>
11.  print_all(self): Printing all items of array</br>
12.  to_numpy(self, type=np.int32):return numpy array with size equal size of inserted elements with type equal to type</br>
13.   to_serties(self,type=np.int32): Return series compatible with pandas</br>
12 some methods </br>
  1-__add__</br>
  2-__radd__</br>
  3-__sub__</br>
  4-__rsub__</br>
  5-__mul__</br>
  6-__rmul__</br>
  7-__iadd__</br>
  8-__contains__</br>
  9-__iter__</br>
  10-__deepcopy__</br>
  11-__str__</br>
  
it supports sorting algorithms: </br>
  1-sort_selection</br>
  2-sort_insertion</br>
  3-sort_quick</br>
  4-sort_count</br>
  
it supports searching algorithms: </br>
  1-search_sequential</br>
  2-search_binary</br>
  
 Example:
 ```
 a1=LinkedList()
a1.add_all([6,55,10])

a2=LinkedList()
a2.add(1)
a2.add(12)
a2.add(9)

x=a1+a2
print(x)
x=x*10
print(x)

x.sort_insertion()
print(x)
```
output</br>

index 0 :7</br>
index 1 :67</br>
index 2 :19</br>

index 0 :70</br>
index 1 :670</br>
index 2 :190</br>

index 0 :70</br>
index 1 :190</br>
index 2 :670</br>

# ArrayStack </br>

Stack data structure implmented by Array list meaning it has no max size.</br>
You can access the top element </br>

**Advantages**: </br>
1- access any element O(1) </br>

**Disadvantages**: </br>
1- you need to specifiy the max size  </br>

# most important algorithms </br>
1. push(self, val):  adding element at the top of all previous </br>
2. pop(self):  removing the top element  </br>
3. peek(self):   Lookin at teh first element only without removing  </br>
4. get_actual_len(self)  Get the actual count of inserted elements in array </br>
5. get_free_space(self): Get count of free spaces in the array. </br>
6. replace(self, replaced, to): replace any element with given input </br>
7. print_all(self): replace all items in arry with specific value "replaced" to "to" </br>
8. to_numpy(self, type=np.int32): return numpy array with size equal size of inserted elements with type equal to type </br>
9. to_serties(self,type=np.int32): Return series compatible with pandas </br>
```
a1=ArrayStack()
a1.push(2)
a1.push(4)
a1.push(8)
a1.push(77)

print(a1.peek())
print(a1.pop())
print(a1.pop())
print(a1.pop())
```

output:
77
77
8
4


    
# LinkedStack </br>

Stack data structure implmented by Linked list meaning it has no max size. </br>
You can access the top element </br>

**Advantages**: </br>
1.access first element O(1) </br>
2. No MAX size </br>

**Disadvantages**: </br>
1.access to last element takes O(N) </br>

# most important algorithms </br>
1. push(self, val):  adding element at the top of all previous </br>
2. pop(self):  removing the top element  </br>
3. peek(self):   Lookin at teh first element only without removing  </br>
7. print_all(self): replace all items in arry with specific value "replaced" to "to" </br>
8. to_numpy(self, type=np.int32): return numpy array with size equal size of inserted elements with type equal to type </br>
9. to_serties(self,type=np.int32): Return series compatible with pandas </br>

```
a1=LinkedStack()
a1.push(2)
a1.push(4)
a1.push(8)
a1.push(77)

print(a1.peek())
print(a1.pop())
print(a1.pop())
print(a1.pop())

```

output: </br>
77 </br>
77 </br>
8 </br>
4 </br>


# LinkedBinarySearchTree
Binary search tree, implented by Linked list not array 
It assures that worst case for insertion, deletion,search is O(N),
but average is O(log(N))</br>



1. def add(self, val): Adding new node to the tree</br>
2. def get_min(self): Returns the min of the array, meaning the left most node</br>
3. get_max(self):  return the max value for the array, meaning the right most node.</br>
4.  delete(self, val): delete node with specific value.</br>
5.   contains(self, val):  does the tree contains that vlue</br>
6.   preorder(self):  returning list containsing the elemetn in preorder traversal</br>
        root- left-right</br>
7.inorder(self):  returning list containsing the elemetn in inorder traversal</br>
        Left - root -right</br>
8. postorder(self):   returning list containsing the elemetn in postorder traversal</br>
        left- right-root.</br>
        
```
a1=LinkedBinarySearchTree()
a1.add(2)
a1.add(4)
a1.add(8)
a1.add(45)
a1.add(45)
a1.add(9)
a1.add(38)
a1.add(7)

print(a1.get_min())
print(a1.get_max())
print(a1.preorder())
print(a1.inorder())
```
output:</br>
2</br>
45</br>
[2, 4, 8, 7, 45, 45, 9, 38]</br>
[2, 4, 7, 8, 9, 38, 45, 45]</br>

        
        
        

       



        


        
        






















