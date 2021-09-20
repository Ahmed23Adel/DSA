Most important data structures, associated with very optimized sorting, and searching algrothims.

Data structure:</br>
1-ArrayList </br>
2-LinkedList </br>
3-stack implemented with array (ArrayStack)</br>
4-stack implemented with linkedList (LinkedStack)</br>
3-stack implemented with array (ArrayQueue)</br>
4-Queue implemented with linkedList (linkedQueue)</br>
5-binary serach tree, implemented by Linked list (LinkedBinarySearchTree)</br>

Sorting Algorithms:</br>
1-selection</br>
2-insertion</br>
3-quick sort</br>
4-counting sort</br>

searching algorithms:</br>
1-sequential</br>
2-binary</br>


## ArrayList:
 A list represented by array</br>
advantages:</br>

  1-Access any element ay any index O(1)</br>
  2-inserting/deleting an element at the end of arry is O(1)</br>
  3-fixed size array,cannot be changed after intialization, so it doesn't resize at each addition </br>
disadvantages:</br>
  1- insertion at the first of array will all elements taking O(N)</br>
  2- size cannot be changed if needed more space.</br>

most important algorithms
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
        
        



















