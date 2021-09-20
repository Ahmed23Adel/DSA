import ctypes
import numpy as np
#import pandas as pd
class ArrayList:
    """
    A list represented by array
    advantages:
    ------------
        1-Access any element ay any index O(1)
        2-inserting/deleting an element at the end of arry is O(1)
        3-fixed size array,cannot be changed after intialization, so it doesn't resize at each addition 
    disadvantages:
    ----------------
        1- insertion at the first of array will all elements taking O(N)
        2- size cannot be changed if needed more space.

    Default max size is 10.
    Methods
    --------
        get_actual_len():Get the actual count of inserted elements in array

        get_free_space():Get count of free spaces in the array.

        add(self,val):Adding element at the end of the array if not filled

        add_at_shift(self,k,value):  addin at specified index k, value

        add_at_replace(self,k,value): add value at index k

        def add_all(self,values): Given a list of items, insert them all to the array list if possible, at the end of array

        remove_at(self, k): Remove item in array at index k, meaning it will shift elemens to the left

        remove_all_indicies(self, lst_removable): Given a list of indices, remove all indecied in it.

        contains(self, searchable): Checking if array containg specific value.

        index_of(self, searchable):return the index if desired element:

        is_empty(self):  is array empty?

        replace(self, replaced, to): replace all items in arry with specific value "replaced" to "to"

        clear(self):  delete and clear all items in array

        is_full(self): return True if the array is full of elements

    """


    def __init__(self,max_size=10):
        self._max_size=max_size
        self._n=0 #the index at which next element to be inserted
        self._ary=self._make_array(self._max_size) # array to be inserted at.
        self._next_k=-1

    #making new array of type ctypes.py_object which is like pointer in C
    def _make_array(self,new_capacity):
        return (new_capacity*ctypes.py_object)()

    #only returning max size decided at intialization.
    def __len__(self):
        return self.get_actual_len()

    def get_actual_len(self):
        """ Get the actual count of inserted elements in array
        
        Parameters:
        -----------
        None.
        Returns:
        ----------
        integer saysing count of inserted elements in the array.
        """
        return self._n
    
    def get_free_space(self):
        """ Get count of free spaces in the array.

        Parameters:
        ----------
        None.

        Returne:
        ----------
        integer representing count of free spaces in the array
        """
        return self._max_size-self._n

    def __getitem__(self,k):
        """ Returning an item at index k
        Parameters:
        -----------
        k: int; the index of desired element
        
        returns:
        --------
        returning the elemnt at index k
        if K not int returns TypeErro
        if k not valid index return Index Error.
        """
        try:
            k=int(k)
        except:            
            raise TypeError("the index should be integer")
        if not 0<=k<self._n:
            return self._return_index_error
        return self._ary[k]

    def _return_index_error(self,k):
        """ just checking for the best error to be return for accessing an element in array
        """
        if k<0:
            raise IndexError("Invalid index; index can't be less than zero")
        if k>= self._n:
            raise IndexError("Invalid index; index can't be equal of greater than (index+1) of the last elemetn in list")

    def __setitem__(self,k,value):
            """ adding at specified index k, value
            like add_at_replace()

            Parameter:
            -----------
            k: index to be inserted at.
            value: value to be inserted at index k

            Returne:
            ----------
            IndexError if k not valid
            
            """
            self._setitem_replace(k,value)

    def add (self,val):
        """Adding element at the end of the array if not filled

        Parameter:
        ----------
        val: value to be inserted at the end of the array
        
        Retruns:
        None.
        """
        if self.is_full():
            raise IndexError("Array is Full, can't insert more")
        self._setitem_shift(self._n,val)
        
    def add_at_shift(self,k,value):
        """ adding at specified index k, value

        Parameter:
        -----------
        k: index to be inserted at.
        value: value to be inserted at index k

        Returne:
        ----------
        IndexError if k not valid
        
        """
        self._setitem_shift(k,value)

    def add_at_replace(self,k,value):
        """add value at index k
        if ary at inde k if not none, filled with something
        it replace it with value given to function

        Parameter:
        ------------
        k: index to be inserted at
        value: value to be inserted at index k

        Returnes:
        ---------
        Index error if k not valid index
        
        """
        return self._setitem_replace(k,value)

    def add_all(self,values):
        """Given a list of items, insert them all to the array list if possible, at the end of array

        Parameters:
        ------------
        valuse: any kind of list 

        Returne:
        -------
        IndexError if size not valid

        """
        isToInsert=(len(values)+self._n)<=self._max_size # is eligible to insert?
        if isToInsert:
            count=0
            for i in range(self._n, self._n+len(values)):
                self._ary[i]=values[count]
                count +=1
            self._n +=len(values)
        else:
            raise IndexError("size of input is too large to fit in the free space of array")        

    def _setitem_shift(self,k,value):
        """ Settting a value at specified index k
        if that place is filled with anything not None:
            if shift all elements statring of index k to the end of arry one step to the right

        Paramets:
        -----------
        k: index to be inserted at.
        value: value to be inserted at if possible.
         
        Returne:
        ----------
        Index Error if k not valid
        """
        isToInsert= (k>=0) and (k <= self._n) and (self._n <self._max_size)  ## is it eligible to insert at that index?
        if isToInsert:
            for i in range(self._n,k,-1): ## shift elements to right.
                self._ary[i]=self._ary[i-1]
            self._ary[k]=value
            self._n += 1 # we have one more element
        else:
            return self._return_index_error(k)
        
    def _setitem_replace(self,k,value):
        if k ==self._n:
            self._ary[k]=value
            self._n += 1
        elif 0 <= k <self._n:
            self._ary[k]=value
        else:
            return self._return_index_error(k)

    def remove_at(self, k):
        """ Remove item in array at index k, meaning it will shift elemens to the left

        Parameters:
        ------------
        k: index to be removed at

        Returns:
        ----------
        return Index error if index not valid
        
        """
        isToRemove = (0<=k<self._n) and not ( self._n ==0)
        if isToRemove:
            for i in range(k, self._n-1):
                self._ary[i]=self._ary[i+1]
            self._ary[self._n-1]=None
            self._n -=1
        else:
            raise IndexError("invalid index")
   
    def remove_all_indicies(self, lst_removable):
        """Given a list of indices, remove all indecied in it.

        Parameters:
        -------------
        lst_removable: list of removed elements

        Returns:
        ----------
        Return IndexError if one of lst_removable not valid to remove.
        
        """
        #check all elements to be valid.
        for rmv in lst_removable:
            if not self._is_valid(rmv):
                raise IndexError("one of element in removable array is no valid")
        count =0
        self._tmp_ary=self._make_array(len(self))

        for i in range(self._n):
            if i not in lst_removable:
                self._tmp_ary[count]=self._ary[i]
                count +=1
        
        self._ary=self._tmp_ary
        self._n -=len(lst_removable)

    def _is_valid(self, index):
        """ is index valid?
        Parameter: index to be checked at
        Returne :None
        """
        return 0<=index<self._n
   
    def contains(self, searchable):
        """Checking if array containg specific value.

        Parameter:searchable item to be searched for.

        Returns:
        -------
        True if found, False if not found. 
        
        """
        for i in range(0, self._n):
            if self._ary[i]==searchable:
                return True
        return False
    
    def index_of(self, searchable):
        """ return the index if desired element:

        Parameters:
        --------
        searchable: item to be searched for

        Returens: index of item if found
        if not found it return KeyError
        """
        for i in range(0, self._n):
            if self._ary[i]==searchable:
                return i
        raise KeyError("no value found like that")

    def is_empty(self):
        """ is array empty?
        
        """
        return self._n==0

    def replace(self, replaced, to):
        """ replace all items in arry with specific value "replaced" to "to"

        Parameters:
        -----------
        replaced: we will search for this item to be replaces by "to"
        to: if found any thing equal replaces will be replaced by "to"
        """

        for i in range(self._n):
            if self._ary[i]==replaced:
                self._ary[i]=to

    def clear(self):
        """ delete and clear all items in array

        Paremters:
        ---------
        None
        Returns: 
        -------
        None


        """
        for i in range(self._n):
            self._ary[i]=None
        self._n=0

    def is_full(self):
        """ return True if the array is full of elements

        Parametes:
        ----------
        None.

        Retruns:
        return True if the array is full of elements
        """
        return self._n==self._max_size

    def print_all(self):
        """Printing all items of array
        Paramters:
        -----------
        None.

        Retruns:
        -----------
        None.
        
        """

        for i in range(self._n):
            print("index ",i," :",self._ary[i])

    def to_numpy(self, type=np.int32):
        """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return np.array([self._ary[i] for i in range(self._n) ],type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return pd.Series(self.to_numpy(type))

    def __add__(self, b):
        """ add values ot two array
        
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add(self._ary[i]+b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add(self._ary[i]+b._ary[i])
            return ary_lst

    def __radd__(self, b):
        """ add values ot two array
        
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]+b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]+b._ary[i])
            return ary_lst

    def __sub__(self, b):
        """subtract values of two arrays
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]-b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]-b._ary[i])
            return ary_lst

    def __rsub__(self, b):
        """subtract values of two arrays
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]-b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]-b._ary[i])
            return ary_lst

    def __mul__(self, b):
        """multiply values of two arrays
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]*b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]*b._ary[i])
            return ary_lst

    def __rmul__(self, b):
        """multiply values of two arrays
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]*b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]*b._ary[i])
            return ary_lst

    def __iadd__(self,b):
        """ add values ot two array
        
        """
        if isinstance(b,int):
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]+b)
            return ary_lst
        if not self._n ==b._n:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ary_lst=ArrayList(self._max_size)
            for i in range(self._n):
                ary_lst.add_item(self._ary[i]+b._ary[i])
            return ary_lst

    def __contains__(self, s):
        return self.contains(s)

    def __next__(self):
        self._next_k +=1
        if self._is_valid(self._next_k):
            return self._ary[self._next_k]
        else:
            self._next_k =-1
            raise StopIteration()
   
    def __iter__(self):
        return self
        
    def __deepcopy__(self,memo):
        """
        it copies deeply element of current array and return copy of that

        Parameters
        ----------
        

        Returns
        -------
        result : TYPE
            new array with exactly same elements as before..

        """
        result=ArrayList(max_size=self._max_size)
        for i in range(self.get_actual_len()):
            result.add(self[i])
            
        return result
    
    def sort_selection(self,inplace=True):
        """
        sorting the list using selection algorithm
        it takes O(N^2)
        stable and in-place
    
        Parameters
        ----------
        lst : ArrayList, or Linkedlist
            DESCRIPTION.
        inplace: Bool
            if true, it edits the given list, if false, 
            it return new one and not editing the original one.
    
        Returns
        -------
        None.
        """
        if inplace:
            sort_selection(self,True)
        else:
            return sort_selection(self,False)
        
    def sort_insertion(self,inplace=True):
        """
        Parameters
        ----------
        inplace : bool, optional
        do you want to sort the given lst, or return new one?

        Returns
        -------
        new_lst : TYPE
        if inplace==false, then it returns new one..

        """
        if inplace:
            sort_insertion(self,True)
        else:
            return sort_insertion(self,False)
        
    def sort_quick(self, inplace=True):
        """
        Quick sort, 
        Code taken from Geeks for gekks: https://www.geeksforgeeks.org/python-program-for-quicksort/
        
        Best case O(NLog n)
        worst case O(N^2)
        Average case O(Nlog N)
    
        Parameters
        ----------
        lst : TYPE
            vector
        low : TYPE
            lowest index to start sort from
        high : TYPE
            upper limit
        inplace : bool, optional
            do you want to sort the given lst, or return new one?
        Returns
        -------
        anew_lst : TYPE
            if inplace==false, then it returns new one..
    
        """
        if inplace:
            sort_quick(self, 0, len(al)-1,True)
        else:
            return sort_quick(self, 0, len(al)-1,True)
        
    def sort_count(self, inplace=True):
        """
        Sorting the array by counting algorithm
        taking O(N) 
        but not in place

        Parameters
        ----------
        inplace : bool, optional
            if true, it sort the original array, else it return new one. The default is True.

        Returns
        -------
        new_lst : TYPE
            if inplace is true, it return new one..

        """
        if inplace:
            sort_count(self)
        else:
            new_lst=copy.deepcopy(self)
            sort_count(new_lst)
            return new_lst
        
    def __str__(self):
        output=""
        for i in range(self._n):
            output += "index "+str(i)+" :"+str(self._ary[i]) +"\n"
        return output
    
    def search_sequential(self,s):
        """
        search in the list by sequentional algorithm
        it takes maximum O(N)

        Parameters
        ----------
        s : 
            what you are looking for.

        Returns
        -------
        TYPE
            index of element you are searching for .
            -1 if  not found

        """
        return search_sequential(self,s)
                    
class Node:
    """Single node made specifically for LinkedList class
    """
    def __init__(self, data, next):
        """Constructor for Node.
        
        Parameter
        ----------
        data: data stored at this single node
        
        """
        if not data ==None:
            self.data=data
        else:
            self.data=None

        if not next== None:
            self.next=next
        else:
            self.next=None

class LinkedList:
    """List representaed by linked list
    Advantages:
    1-no max limit fot the limlit
    2- you can add as many elements as needed

    disadvantages
    1-inserting/deleting at the end of the list, it will take O(N)
    
    """
    def __init__(self):
        """Constructor 

        Parameter:
        ----------
        None.

        
        """
        self._head=None
        self._size=0
        self._next_k =-1

    def __len__(self):
        """ Returns the length of the list

        parameters:
        -------------
        None

        Returns:
        -----------
        integer representing the size of the list.
        """
        return self._size

    def add (self, value):
        """add new value to the list
        you need only to attach the value at that node, not an instace of the node.

        Paramters:
        ---------
        value: value wanted to be inserted at the last node.

        Returns:
        ----------
        None.
        
        """
        tmp_node=Node(value,None)# creating node.
        #if no head was created?
        if self._head== None:
            self._head=tmp_node
            self._size=1
        # there was a head intialized before.
        else:
            crnt_node=self._head
            ##looping till find the last node.
            while not crnt_node.next ==None:
                crnt_node=crnt_node.next
            crnt_node.next=tmp_node
            self._size +=1

    def __setitem__(self, k, value):
        """ setting new item at position k with value equal value.

        paramters:
        -----------
        k: index at which the new node will be create it could range from 0 to size 
        value: value new node created

        Returns:
        ------------
        None.
        
        """
        self.add_at_replace(k, value)
        
    def add_at(self,k, value):
        """ setting new item at position k with value equal value.
        if at k position there is a node, it shifts them to left.

        paramters:
        -----------
        k: index at which the new node will be create it could range from 0 to size 
        value: value new node created

        Returns:
        ------------
        None.
        
        """

        if k >self._size:
            raise IndexError("invalid index: k>max size" )
        if k==0 and self._size==0:
            self._head=Node(value,None)
            self._size=1

        elif not self._size ==0 and k==0:
            tmp_node=Node(value,None)
            tmp_node.next=self._head
            self._head=tmp_node
            self._size +=1

        elif k==self._size:
            crnt_node=self._head
            new_node=Node(value,None)
            for i in range(self._size-1):
                crnt_node=crnt_node.next
            crnt_node.next=new_node
            self._size +=1
        else:
            crnt_node=self._head
            new_node=Node(value,None)
            for i in range(k-1):
                crnt_node=crnt_node.next

            new_node.next=crnt_node.next
            crnt_node.next=new_node

            self._size +=1
            
    def add_at_replace(self,k, value):
        """ setting new item at position k with value equal value.
        if at positoin k there is elemnt, it updates it 

        paramters:
        -----------
        k: index at which the new node will be create it could range from 0 to size 
        value: value new node created

        Returns:
        ------------
        None.
        
        """

        if k >self._size:
            raise IndexError("invalid index: k>max size" )
        if k==0 and self._size==0:
            self._head=Node(value,None)
            self._size=1

        elif not self._size ==0 and k==0:
            #updating the value
            self._head.data=value

        elif k==self._size:
            #inserting new vlaue
            crnt_node=self._head
            new_node=Node(value,None)
            for i in range(self._size-1):
                crnt_node=crnt_node.next
            crnt_node.next=new_node
            self._size +=1
        else:
            #updating the value
            crnt_node=self._head
            for i in range(k):
                crnt_node=crnt_node.next
            crnt_node.data=value           

    def add_all(self,values):
        """add all value in values, 

        parameters:
        values:iterator 

        returns:
        ---------
        Nonee
        
        """
        for value in values:
            self.add_at(self._size, value)

    def __getitem__(self, k):
        """return item at index equal k

        Parameters:
        -----------
        k: index (int)

        Returns:
        ----------
            value at node at index k
        """
        return self.get_at(k)

    def add_first(self, val):
        """adding item at head.

        Parameters:
        -----------
        val: values inserted at head

        Returns:
        --------
        None.

        """
        self.add_at(0, val)

    def add_last(self, val):
        """adding item at last index.

        Parameters:
        -----------
        val: values inserted at last index

        Returns:
        --------
        None.
        
        """
        self.add_at(self._size,val)

    def get_at(self,k):
        """Returns value at index k:

        Parameters:
        ----------
        k: index to be returned.

        Returnes:
        ---------
        value at index k
        if index not valid, it returns IndexError
        
        """
        isToGet= 0<=k<self._size
        if isToGet:
            crnt_node=self._head
            for i in range(k):
                crnt_node=crnt_node.next
            return crnt_node.data
        else:
            raise IndexError("invalid index")

    def get_first(self):
        """returns the value of head.

        Paramters:
        ----------
        None.

        Returns:
        -----
        value of head.
        """
        return self.get_at(0)

    def get_last(self):
        """returns the value of last element.

        Paramters:
        ----------
        None.

        Returns:
        -----
        value of last element.
        """
        return self.get_at(self._size-1)

    def clear(self):
        """ it clear the whole list.

        """
        crnt_node=self._head
        next_node=crnt_node.next
        while not next_node.next == None:
            del crnt_node
            crnt_node=next_node
            next_node=next_node.next
        del crnt_node
        self._size=0

    def contains(self, searchable):
        """ it returns True, if list contains what is searced for.

        Paremeters:
        ------------
        searchable: what you are looking for

        Returns:
        ---------
        Ture if found; False otherwise.
        """
        crnt_node=self._head
        while not crnt_node.next == None:
            if crnt_node.data== searchable:
                return True
            crnt_node=crnt_node.next
        if crnt_node.data== searchable:
            return True
        return False

    def index_of(self, searchable):
        """Return the index of what is searched for
        
        Parameters:
        -------
        searchable: what you are looking for.
        
        
        Returns:
        ----------
        reutnr index of node having value searchable
        
        """
        crnt_node=self._head
        index =0
        while not crnt_node.next == None:
            if crnt_node.data== searchable:
                return index
            index +=1
            crnt_node=crnt_node.next
        if crnt_node.data==searchable:
            return index +1
        else:
            raise IndexError("Not found")
    
    def remove_first(self):
        """it removes the head of linked list.
        
        parameters:
        -------
        None.
        
        
        Returns:
        -------
        none.
        """
        self.remove_at(0)

    def remove_last(self):
        """it removes the last element of linked list
        
        parameters:
        -------
        None.
        
        
        Returns:
        -------
        none.
        """
        self.remove_at(self._size)

    def remove_at(self, k):
        """remove node at index k

        parameters:
        -----------
        k: index of node you want to remove.

        returns:
        ---------
        none.
        """
        if self._size==0:
            pass
        else:
            if k==0:
                prev_head=self._head
                self._head=self._head.next
                del prev_head
                self._size -=1
            elif k==self._size:
                crnt_node=self._head
                prev_node=None
                for i in range(k-1):
                    prev_node=crnt_node
                    crnt_node=crnt_node.next
                prev_node.next=crnt_node.next
                del crnt_node
            else:
                crnt_node=self._head
                prev_node=None
                for i in range(k):
                    prev_node=crnt_node
                    crnt_node=crnt_node.next
                prev_node.next=crnt_node.next
                del crnt_node

    def print_all(self):
        """Printing all items of array
        Paramters:
        -----------
        None.

        Retruns:
        -----------
        None.
        
        """

        if self._head == None:
            return
        else:
            crnt_node=self._head
            counter=0
            while not crnt_node.next  == None:
                print("index ",counter," :",crnt_node.data)
                crnt_node=crnt_node.next
                counter +=1
            print("index ",counter," :",crnt_node.data)
            
    def to_numpy(self, type=np.int32):
        """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        nmpy=np.zeros(self._size)
        crnt_node=self._head
        counter=0
        while not crnt_node.next  == None:
             nmpy[counter]=crnt_node.data
             crnt_node=crnt_node.next
             counter +=1 
        nmpy[counter]=crnt_node.data
        
        return nmpy

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return pd.Series(self.to_numpy(type))

    def __add__(self, b):
        """ add values to the list
        
        Parameters:
        --------------
        b: could be either integer or list
        
        
        
        """
        if isinstance(b,int):
            ll_lst=LinkedList()
            crnt_node=self._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data+b)
                 crnt_node=crnt_node.next
            ll_lst.add(crnt_node.data+b)
            return ll_lst
        if not self._size ==b._size:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ll_lst=LinkedList()
            crnt_node=self._head
            crnt_node_b=b._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data+ crnt_node_b.data)
                 crnt_node=crnt_node.next
                 crnt_node_b=crnt_node_b.next
            ll_lst.add(crnt_node.data+ crnt_node_b.data)
 
            return ll_lst
        
    def __radd__(self, b):
        """ add values to the list
        
        Parameters:
        --------------
        b: could be either integer or list
        
        
        
        """
        if isinstance(b,int):
            ll_lst=LinkedList()
            crnt_node=self._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data+b)
                 crnt_node=crnt_node.next
            ll_lst.add(crnt_node.data+b)
            return ll_lst
        if not self._size ==b._size:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ll_lst=LinkedList()
            crnt_node=self._head
            crnt_node_b=b._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data+ crnt_node_b.data)
                 crnt_node=crnt_node.next
                 crnt_node_b=crnt_node_b.next
            ll_lst.add(crnt_node.data+ crnt_node_b.data)
 
            return ll_lst
        
    def __sub__(self, b):
        """ subtract values to the list
        
        Parameters:
        --------------
        b: could be either integer or list
        
        """
        if isinstance(b,int):
            ll_lst=LinkedList()
            crnt_node=self._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data-b)
                 crnt_node=crnt_node.next
            ll_lst.add(crnt_node.data-b)
            return ll_lst
        if not self._size ==b._size:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ll_lst=LinkedList()
            crnt_node=self._head
            crnt_node_b=b._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data- crnt_node_b.data)
                 crnt_node=crnt_node.next
                 crnt_node_b=crnt_node_b.next
            ll_lst.add(crnt_node.data- crnt_node_b.data)
 
            return ll_lst
        
    def __mul__(self, b):
        """ multiply values to the list
        
        Parameters:
        --------------
        b: could be either integer or list
        
        
        
        """
        if isinstance(b,int):
            ll_lst=LinkedList()
            crnt_node=self._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data*b)
                 crnt_node=crnt_node.next
            ll_lst.add(crnt_node.data*b)
            return ll_lst
        if not self._size ==b._size:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ll_lst=LinkedList()
            crnt_node=self._head
            crnt_node_b=b._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data* crnt_node_b.data)
                 crnt_node=crnt_node.next
                 crnt_node_b=crnt_node_b.next
            ll_lst.add(crnt_node.data* crnt_node_b.data)
 
            return ll_lst
    
    def __rmul__(self, b):
        """ multiply values to the list
        
        Parameters:
        --------------
        b: could be either integer or list
        
        
        
        """
        if isinstance(b,int):
            ll_lst=LinkedList()
            crnt_node=self._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data*b)
                 crnt_node=crnt_node.next
            ll_lst.add(crnt_node.data*b)
            return ll_lst
        if not self._size ==b._size:
            raise  IndexError("array sizes of two elemetns are not the same")
        else:
            ll_lst=LinkedList()
            crnt_node=self._head
            crnt_node_b=b._head
            while not crnt_node.next  == None:
                 ll_lst.add(crnt_node.data* crnt_node_b.data)
                 crnt_node=crnt_node.next
                 crnt_node_b=crnt_node_b.next
            ll_lst.add(crnt_node.data* crnt_node_b.data)
 
            return ll_lst
        
    def _is_valid(self, index):
        """ is index valid?
        Parameter: index to be checked at
        Returne :None
        """
        return 0<=index<self._size
    
    def __contains__(self, s):
        return self.contains(s)

    def __next__(self):
        self._next_k +=1
        if self._is_valid(self._next_k):
            return self[self._next_k]
        else:
            self._next_k =-1
            raise StopIteration()
   
    def __iter__(self):
        return self
    
    def sort_selection(self,inplace=False):
        """
        sorting the list using selection algorithm
        it takes O(N^2)
        stable and in-place
    
        Parameters
        ----------
        lst : ArrayList, or Linkedlist
            DESCRIPTION.
        inplace: Bool
            if true, it edits the given list, if false, 
            it return new one and not editing the original one.
    
        Returns
        -------
        None.
        """
        if inplace:
            sort_selection(self,False)
        else:
            return sort_selection(self,True)
        
    def sort_insertion(self,inplace=True):
        """
        Parameters
        ----------
        inplace : bool, optional
        do you want to sort the given lst, or return new one?

        Returns
        -------
        new_lst : TYPE
        if inplace==false, then it returns new one..

        """
        if inplace:
            sort_insertion(self,True)
        else:
            return sort_insertion(self,False)
        
    def sort_quick(self, inplace=True):
        """
        Quick sort, 
        Code taken from Geeks for gekks: https://www.geeksforgeeks.org/python-program-for-quicksort/
        
        Best case O(NLog n)
        worst case O(N^2)
        Average case O(Nlog N)
    
        Parameters
        ----------
        lst : TYPE
            vector
        low : TYPE
            lowest index to start sort from
        high : TYPE
            upper limit
        inplace : bool, optional
            do you want to sort the given lst, or return new one?
        Returns
        -------
        anew_lst : TYPE
            if inplace==false, then it returns new one..
    
        """
        if inplace:
            sort_quick(self, 0, len(al)-1,True)
        else:
            return sort_quick(self, 0, len(al)-1,True)
        
    def sort_count(self, inplace=True):
        """
        Sorting the array by counting algorithm
        taking O(N) 
        but not in place

        Parameters
        ----------
        inplace : bool, optional
            if true, it sort the original array, else it return new one. The default is True.

        Returns
        -------
        new_lst : TYPE
            if inplace is true, it return new one..

        """
        if inplace:
            sort_count(self)
        else:
            new_lst=copy.deepcopy(self)
            sort_count(new_lst)
            return new_lst

    def __str__(self):
        output=""
        if self._head == None:
            return ""
        else:
            crnt_node=self._head
            counter=0
            while not crnt_node.next  == None:
                output += "index " + str(counter) +" :" + str(crnt_node.data) +"\n"
                crnt_node=crnt_node.next
                counter +=1
            output += "index " + str(counter) +" :" + str(crnt_node.data) +"\n"
            
        
        
        return output
    
    def search_sequential(self,s):
        """
        search in the list by sequentional algorithm
        it takes maximum O(N)

        Parameters
        ----------
        s : 
            what you are looking for.

        Returns
        -------
        TYPE
            index of element you are searching for .
            -1 if  not found

        """
        return search_sequential(self,s)

    def search_binary(self,s, sort_by=sort_insertion):
        """
        serachs by binary algorithm
        it takes O(log(N))
        But the array must be sorted first
        
        if sorted you may pass:
            print(al.search_binary(2,sort_by=lambda x:x))

        Parameters
        ----------
        s : TYPE
            what you are lookin for.
        sort_by : TYPE, optional
            algorithm to user to sort the array. The default is sort_insertion.

        Returns
        -------
        TYPE
            index at which what you are looking for is at
            -1 if not found.

        """
        sort_by(self)
        return serach_binary(self,0, len(self)-1,s)
        
        
                    
                
class ArrayStack:
    """    Stack data structure implmented by Array list meaning it has no max size.

        You can access the top element
     Advantages:
         --------
         1- access any element O(1)
         
     Disadvantages:
         ------------
         1- you need to specifiy the max size 
         
    """
    

    def __init__(self,max_size=10):
        
        self._maX_size=max_size
        self._ary=ArrayList(self._maX_size)
        self._top=0
        
    def push(self, val):
        """ 
        adding element at the top of all previous

        Parameters
        ----------
        val : same as all previous
            value to inserted at top of all previous.

        Returns
        -------
        None.

        """
        if self._top < self._maX_size:
            self._ary[self._top]=val
            self._top +=1
        else:
            raise IndexError("list if filled")

    def pop(self):
        """
        removing the top element 

        Returns
        -------
        returned : the value at the top of all elements
        """
        
        if self._top >0:
            returned= self._ary[self._top-1]
            self._top -=1
            return returned
        else:
            raise IndexError("list is empty")
    
    def peek(self):
        """
        Lookin at teh first element only without removing 

        Returns
        -------
        TYPE
            the element at the top all elements..

        """

        return self._ary[self._top-1]

    def __len__(self):
        return self._maX_size
    
    def get_actual_len(self):
        """ Get the actual count of inserted elements in array
        
        Parameters:
        -----------
        None.
        Returns:
        ----------
        integer saysing count of inserted elements in the array.
        """
        return self._ary.get_actual_len()
   
    def get_free_space(self):
        """ Get count of free spaces in the array.

        Parameters:
        ----------
        None.

        Returne:
        ----------
        integer representing count of free spaces in the array
        """
        return self._ary.get_free_space()
 
    def is_empty(self):
        """ is array empty?
        """
        return self._ary.is_empty()

    def is_full(self):
        """ return True if the array is full of elements

        Parametes:
        ----------
        None.

        Retruns:
        return True if the array is full of elements
        """
        return self._ary.is_full()

    def contains(self, searchable):
        """Checking if array containg specific value.

        Parameter:searchable item to be searched for.

        Returns:
        -------
        True if found, False if not found. 
        """
        return self._ary.contains(searchable)

    def clear(self):
        """ delete and clear all items in array

        Paremters:
        ---------
        None
        Returns: 
        -------
        None


        """
        self._ary.clear()
        self._top=0
    
    def replace(self, replaced, to):
        self._ary.replace(replaced, to)
        
    def print_all(self):
        """ replace all items in arry with specific value "replaced" to "to"

        Parameters:
        -----------
        replaced: we will search for this item to be replaces by "to"
        to: if found any thing equal replaces will be replaced by "to"
        """
        self._ary.print_all()

    def to_numpy(self, type=np.int32):
       """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
       return self._ary.to_numpy(type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return self._ary.to_serties(type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return self._ary.to_serties()

class LinkedStack:
    """
    Stack data structure implmented by Linked list meaning it has no max size.
    
    You can access the top element
     Advantages:
         --------
         1- access first element O(1)
         2- No MAX size
         
     Disadvantages:
         ------------
         1- access to last element takes O(N)
         
    """
    def __init__(self):
        self._ary=LinkedList()
        
    def push(self, val):
        """ 
        adding element at the top of all previous

        Parameters
        ----------
        val : same as all previous
            value to inserted at top of all previous.

        Returns
        -------
        None.

        """
        self.add_first(val)
   
    def pop(self):
        """
        removing the top element 

        Returns
        -------
        returned : the value at the top of all elements

        """
        returned= self._ary.get_first()
        self._ary.remove_first()
        return returned
        
    def peek(self):
        """
        Lookin at teh first element only without removing 

        Returns
        -------
        TYPE
            the element at the top all elements..

        """
        return self._ary.get_first()

    def __len__(self):
        return len(self._ary)

    def is_empty(self):
        """ is array empty?
        """
        return len(self._ary)==0

    def contains(self, searchable):
        """Checking if array containg specific value.

        Parameter:searchable item to be searched for.

        Returns:
        -------
        True if found, False if not found. 
        """
        return self._ary.contains(searchable)

    def clear(self):
        """ delete and clear all items in array

        Paremters:
        ---------
        None
        Returns: 
        -------
        None


        """
        self._ary.clear()
        
    def print_all(self):
        """ replace all items in arry with specific value "replaced" to "to"

        Parameters:
        -----------
        replaced: we will search for this item to be replaces by "to"
        to: if found any thing equal replaces will be replaced by "to"
        """
        self._ary.print_all()

    def to_numpy(self, type=np.int32):
       """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
       return self._ary.to_numpy(type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return self._ary.to_serties(type)
        
class ArrayQueue:
    """Queue implemented by array, you can only access what was inserted first
    advantages:
        1- faster access
    """
    
    def __init__(self, max_size=10):
        self._max_size=max_size
        self._ary=ArrayList(self._max_size)
        self._front=-1
        self._rear=-1

    def is_empty(self):
        """
        return if array is empty

        Returns
        -------
        TYPE Boolean
            True if it's empty, False if not empty.

        """
        return (self._front==-1) and (self._rear==-1)

    def is_full(self):
        """
        return if array is full of elements.

        Returns
        -------
        bool
            True if it's full, False if not not..

        """
        if (self._rear+1)%self._max_size ==self._front :
            return  True
        return False

    def enqueue(self, val):
        """
        Adding value at the end of queue.

        Parameters
        ----------
        val : any type
            value inserted at end of queue.

        Raises
        ------
        IndexError
            if array is full.

        Returns
        -------
        None.

        """
        if(self.is_full()):
            raise IndexError("list is full")

        if self.is_empty():
            self._front=0
            self._rear=0
        else:
            self._rear=(self._rear+1)%self._max_size

        self._ary[self._rear]=val

    def dequeu(self):
        """
        access and remove the last element of aray.
        

        Raises
        ------
        IndexError
            if array is empty.

        Returns
        -------
        value of first element in queue. and remove it.

        """
        if self.is_empty():
            raise IndexError("list is empty")
        elif self._front==self._rear:
            returned=self._ary[self._front]
            self._rear=-1
            self._front=-1
            return returned

        else:
            returned=self._ary[self._front]
            self._front =(self._front+1)%self._max_size
            return returned
        
    def __len__(self):
        return self._maX_size
    
    def get_actual_len(self):
        """ Get the actual count of inserted elements in array
        
        Parameters:
        -----------
        None.
        Returns:
        ----------
        integer saysing count of inserted elements in the array.
        """
        return self._ary.get_actual_len()
   
    def get_free_space(self):
        """ Get count of free spaces in the array.

        Parameters:
        ----------
        None.

        Returne:
        ----------
        integer representing count of free spaces in the array
        """
        return self._ary.get_free_space()

    def contains(self, searchable):
        """Checking if array containg specific value.

        Parameter:searchable item to be searched for.

        Returns:
        -------
        True if found, False if not found. 
        """
        return self._ary.contains(searchable)

    def clear(self):
        """ delete and clear all items in array

        Paremters:
        ---------
        None
        Returns: 
        -------
        None


        """
        self._ary.clear()
        self._front=-1
        self._rear=-1
    
    def replace(self, replaced, to):
        self._ary.replace(replaced, to)
        
    def print_all(self):
        """ replace all items in arry with specific value "replaced" to "to"

        Parameters:
        -----------
        replaced: we will search for this item to be replaces by "to"
        to: if found any thing equal replaces will be replaced by "to"
        """
        self._ary.print_all()

    def to_numpy(self, type=np.int32):
       """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
       return self._ary.to_numpy(type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return self._ary.to_serties(type)

class LinkedQueue:
    """Queue implemented by Linked list, you can only access what was inserted first
    advantages:
        1no max size
    """
    
    def __init__(self, max_size=10):
        self._ary=LinkedList()

    def is_empty(self):
        """
        return tur if queue is empty

        Returns
        -------
        Bool
            if is empty reutrn true, otherwise return false..

        """
        return len(self._ary)==0

    
    def enqueue(self, val):
        """
        adding element at the last of queue.

        Parameters
        ----------
        val : 
            add that val at the end of queue..

        Returns
        -------
        None.

        """
        self._ary.add_last(val)

    def dequeu(self):
        """
        access the first element in queue, and removes it.

        Returns
        -------
        returned : 
            value at first positition of queue..

        """
        returned=self._ary.get_first()
        self._ary.remove_first()
        return returned

    def __len__(self):
        return len(self._ary)

    def is_empty(self):
        """ is array empty?
        """
        return len(self._ary)==0

    def contains(self, searchable):
        """Checking if array containg specific value.

        Parameter:searchable item to be searched for.

        Returns:
        -------
        True if found, False if not found. 
        """
        return self._ary.contains(searchable)

    def clear(self):
        """ delete and clear all items in array

        Paremters:
        ---------
        None
        Returns: 
        -------
        None


        """
        self._ary.clear()
        
    def print_all(self):
        """ replace all items in arry with specific value "replaced" to "to"

        Parameters:
        -----------
        replaced: we will search for this item to be replaces by "to"
        to: if found any thing equal replaces will be replaced by "to"
        """
        self._ary.print_all()

    def to_numpy(self, type=np.int32):
       """return numpy array with size equal size of inserted elements with type equal to type
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
       return self._ary.to_numpy(type)

    def to_serties(self,type=np.int32):
        """ Return series compatible with pandas
        
         Parameters:
         ------------
         type: type of nd array to numpy

         Return:
         --------
         1-d nd array with size equal isnerted elements .

        """
        return self._ary.to_serties(type)
        
class LinkedBinarySearchTree:
    """Binary search tree, implented by Linked list not array 
    It assures that worst case for insertion, deletion,search is O(N),
    but average is O(log(N))
    """
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        

    def add(self, val):
        """
        Adding new node to the tree

        Parameters
        ----------
        val : 
            value inserted at new node..

        Returns
        -------
        None.

        """
        # if head is empty
        if not self.val: 
            self.val = val
            return
        
        if val <= self.val:
            if self.left:
                self.left.add(val)
                return
            self.left = LinkedBinarySearchTree(val)
            return

        if self.right:
            self.right.add(val)
            return
        self.right = LinkedBinarySearchTree(val)

    def get_min(self):
        """
        Returns the min of the array, meaning the left most node

        Returns
        -------
        TYPE
            the min of the array.

        """
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        """
        return the max value for the array, meaning the right most node.

        Returns
        -------
        TYPE
            the max val for the tree.

        """
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        """
        delete node with specific value.

        Parameters
        ----------
        val : TYPE
            value to be deleted.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        if self == None:
            return self
        # go to left ? or go to right?
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        #choosing what to put in the parent node
        if self.right == None:
            return self.left
        
        if self.left == None:
            return self.right
        # if delete leaf--> just delete it.
        # if delete parent has one lear--> make child the parent
        #otherwise: find largest in the left subtree.
        largest_left = self.left
        while largest_left.right:
            largest_left = largest_left.right
        self.val = largest_left.val
        self.left = self.left.delete(largest_left.val)
        return self

    def contains(self, val):
        """
        does the tree contains that vlue

        Parameters
        ----------
        val : TYPE
            what you are looking for..

        Returns
        -------
        TYPE
            True if exists, flase otherwise..

        """
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)
    
    def preorder(self):
        """
        returning list containsing the elemetn in preorder traversal
        root- left-right
        Parameters
        ----------
        vals : TYPE
            it will fill that array.

        Returns
        -------
        vals : TYPE
            return the given array but filled with elements in preorder traverlsal.

        """
        return self._preorder([])
    
    def inorder(self):
        """
        returning list containsing the elemetn in inorder traversal
        Left - root -right
        Parameters
        ----------
        vals : TYPE
            it will fill that array.

        Returns
        -------
        vals : TYPE
            return the given array but filled with elements in inorder traverlsal.

        """
        return self._inorder([])
    
        

    def postorder(self):
        """
        returning list containsing the elemetn in postorder traversal
        left- right-root.
        Parameters
        ----------
        vals : TYPE
            it will fill that array.

        Returns
        -------
        vals : TYPE
            return the given array but filled with elements in postorder traverlsal.
        """
        return self._postorder([])


    def _preorder(self, vals):
        """
        helper functoin

        """
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left._preorder(vals)
        if self.right is not None:
            self.right._preorder(vals)
        return vals

    def _inorder(self, vals):
        if self.left is not None:
            self.left._inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right._inorder(vals)
        return vals

    def _postorder(self, vals):
        if self.left is not None:
            self.left._postorder(vals)
        if self.right is not None:
            self.right._postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
    
import copy
def sort_selection(lst,inplace=True):
    """
    sorting the list using selection algorithm
    it takes O(N^2)
    stable and in-place

    Parameters
    ----------
    lst : ArrayList, or Linkedlist
        DESCRIPTION.
    inplace: Bool
        if true, it edits the given list, if false, 
        it return new one and not editing the original one.

    Returns
    -------
    None.

    """
    
    def _swap(a,b):
        tmp=lst[b]
        lst[b] =lst[a]
        lst[a]=tmp
    if inplace:
        for i in range(len(lst)-1):
            min_idx = i
            for j in range(i+1, len(lst)):
                if lst[j]< lst[min_idx]:
                    min_idx=j
                _swap(min_idx,i)
    else:
        new_lst=copy.deepcopy(lst)
        sort_selection(new_lst,True)
        return new_lst

def sort_insertion(lst,inplace=True):
    """
    performs insertion sort
    worst case: O(N^2)
    bes case :O(N) (if mostly sorted)
    but in place and stable

    Parameters
    ----------
    lst : vector
        array to be sorted
    inplace : bool, optional
        do you want to sort the given lst, or return new one?

    Returns
    -------
    new_lst : TYPE
        if inplace==false, then it returns new one..

    """
    if inplace:
        for i in range(1, len(lst)):
  
            cur_element = lst[i]
            j = i-1
            while j >=0 and cur_element < lst[j] :
                    lst[j+1] = lst[j]
                    j -= 1
            lst[j+1] = cur_element
    else:
        new_lst=copy.deepcopy(lst)
        sort_insertion(new_lst,True)
        return new_lst
    
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
def sort_quick(lst, low, high, inplace=True):
    """
    Quick sort, 
    Code taken from Geeks for gekks: https://www.geeksforgeeks.org/python-program-for-quicksort/
    
    Best case O(NLog n)
    worst case O(N^2)
    Average case O(Nlog N)

    Parameters
    ----------
    lst : TYPE
        vector
    low : TYPE
        lowest index to start sort from
    high : TYPE
        upper limit
    inplace : bool, optional
        do you want to sort the given lst, or return new one?
    Returns
    -------
    anew_lst : TYPE
        if inplace==false, then it returns new one..

    """
    if inplace:
        if low < high:
      
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(lst, low, high)
      
            # Separately sort elements before
            # partition and after partition
            sort_quick(lst, low, pi-1)
            sort_quick(lst, pi+1, high)
    else:
        if len(lst) == 1:
            return lst
        new_lst=copy.deepcopy(lst)
        sort_quick(new_lst,True)
        return new_lst
        
def sort_count(arr):
    """
    Count sort space fot time tradeoff.

    Parameters
    ----------
    arr : vector
        vector to be sorted.

    Returns
    -------
    arr : TYPE
        sorted one

    """
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr

def search_sequential(lst, s):
    i=0
    while i<len(lst) and not lst[i]  == s:
        i +=1
    if i<len(lst):
        return i
    else:
        return -1
    
def serach_binary (arr, l, r, x):
    """
    the lst must be sorted
    code taken from GeeksForGeeks https://www.geeksforgeeks.org/binary-search/

    """
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
          
        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return serach_binary(arr, l, mid-1, x)
  
        # Else the element can only be present 
        # in right subarray
        else:
            return serach_binary(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1
    






