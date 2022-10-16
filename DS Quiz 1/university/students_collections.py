"""This module is designed for collection classes."""
from abc import ABC, abstractmethod
from university.students import Student


class Collection(ABC):
    """Abstract base class for all collections."""

    @abstractmethod
    def add(self, e) -> None:
        pass

    @abstractmethod
    def remove(self) -> None:
        pass

    @abstractmethod
    def empty(self) -> None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

class List(Collection):
    abstractmethod
    def add_first(self, e) -> None:
        pass

    abstractmethod
    def add_last(self, e) -> None:
        pass

    abstractmethod
    def remove_first(self) -> bool:
        pass

    abstractmethod
    def remove_last(self) -> bool:
        pass

    @abstractmethod
    def first(self) -> Student:
        pass

    @abstractmethod
    def last(self) -> Student:
        pass

class Queue(Collection):
    @abstractmethod
    def enqueue(self, e):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

class Stack(Collection):
    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass


class StudentsSingleLinkedList(Collection):
    def __init__(self):
        self._first: StudentsSingleLinkedList._Node = None
        self._last: StudentsSingleLinkedList._Node = None
        self._size: int = 0

    class _Node:
        def __init__(self, d, n = None):
            self._data: Student = d
            self._next: StudentsSingleLinkedList._Node = n

    ''' Task 2: Implement remove_at function which removes element at given index if it exists in the list.
        False is returned otherwise. 
    '''
    def remove_at(self, index: int) -> bool:
        # Handlings the cases when index will be out of boundaries
        if index < 0 or index >= self._size:
            return False
        else:
            # If linked list is empty return False
            if self._first == None:
                return False
    
            # Store head node
            self._last = self._first
    
            # If head needs to be removed
            if index == 0:
                self._first = self._last._next
                self._last = None

                # reducing the linkedlist size by 1 and return True
                # after node deletion from linkelist
                self._size -= 1
                return True
    
            # Find previous node of the node to be deleted
            for iterator in range(index -1):
                self._last = self._last._next
                if self._last is None:
                    break
    
            # If position is more than number of nodes return False
            if self._last is None:
                return False
            if self._last._next is None:
                return False
    
            # Node self._last._next is the node to be deleted
            # store pointer to the next of node to be deleted
            next_node = self._last._next._next
    
            # Unlink the node from linked list
            self._last._next._next = None
            self._last._next = next_node

            # reducing the linkedlist size by 1 after deletion
            self._size -= 1

            return True

    ''' Task 3: Implement add_before function which adds the Student e before the first occurrence of Student a in list.
        False is returned if Student a is not found in list. '''
    def add_before(self, a: Student, e: Student) -> bool:
        # If linked list is empty return False
        if self._first == None:
            return False

        self._last = self._first
        prev = None

        # Create new node with data as Student 'e'
        new_student = StudentsSingleLinkedList._Node(e)

        # First check if new student is needed to be added at start
        if self._first._data == a:
    
            # Point to next to current head
            new_student._next = self._first
    
            # Update the head pointer
            self._first = new_student
            
            # increasing the list size by 1 after insertion
            self._size += 1
            
            return True

        # search for first occurrence of Student 'a' in list.
        while self._last != None:
            if self._last._data == a:
                break
            else:
                prev = self._last
                self._last = self._last._next

        # check if the Student 'a' exists
        if self._last == None:
            return False

        # Make next of new Node as next of prev_node
        new_student._next = prev._next
   
        # make next of prev_node as new_node
        prev._next = new_student

        # increasing the list size by 1 after insertion
        self._size += 1

        return True


    ''' Task 4: Implement graduation year forward iterator, which iterates over the students graduating on given year 
    '''
    def graduation_year_iterator(self, grad_year):
        pass

    def add_first(self, e) -> None:
        pass

    def add_last(self, e) -> None:
        if self.is_empty():
            self._last = self._first = StudentsSingleLinkedList._Node(e)
        else:
            self._last._next = StudentsSingleLinkedList._Node(e)
            self._last = self._last._next
        self._size += 1

    def remove_first(self) -> bool:
        pass

    def remove_last(self) -> bool:
        pass

    def first(self) -> Student:
        return self._first._data

    def last(self) -> Student:
        return self._last._data

    def add(self, e) -> None:
        self.add_first(e)

    def remove(self, e) -> None:
        self.remove_last()

    def empty(self) -> None:
        self._first = self._last = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size


class StudentsDoubleLinkedList(Collection):
    def __init__(self):
        self.__first: StudentsDoubleLinkedList.Node = None
        self.__last: StudentsDoubleLinkedList.Node = None
        self.__size: int = 0

    class Node:
        def __init__(self, d, n = None, p = None):
            self._data: Student = d
            self._next: StudentsDoubleLinkedList.Node = n
            self._prev: StudentsDoubleLinkedList.Node = p

    ''' Task 2: Implement remove_at(index) function which removes element at given index if it exists in the list. 
         False is returned otherwise. '''
    def remove_at(self, index: int) -> bool:
        # Handlings the cases when index will be out of boundaries
        # or list if empty
        if index < 0 or index >= self.__size or self.__first == None:
            return False
        else:
            self.__last = self.__first
            i = 0
        
            # traverse up to the node at given index from
            # the beginning
            while ( self.__last != None and i < index ):
                if i == index:
                    break
                else:
                    self.__last = self.__last._next
                    i = i + 1
        
            # if 'index' is greater than the number of nodes
            # in the doubly linked list
            if (self.__last == None):
                return False
        
            # delete the node pointed to by 'self.__last'

            # If node to be deleted is head node
            if (self.__first == self.__last):
                self.__first = self.__last._next
                self.__first._prev = None

                # reducing the list size by 1 after deletion
                self.__size -= 1
                return True

            # If node to be deleted is tail/last node
            if (self.__last._next == None):
                self.__last = self.__last._prev
                self.__last._next = None
                
                # reducing the list size by 1 after deletion
                self.__size -= 1
                return True

        
            # Change next only if node to be deleted is NOT
            # the last node
            if (self.__last._next != None):
                self.__last._next._prev = self.__last._prev
        
            # Change prev only if node to be deleted is NOT
            # the first node
            if (self.__last._prev != None):
                self.__last._prev._next = self.__last._next
            
            # reducing the list size by 1 after deletion
            self.__size -= 1

            return True

    def add_first(self, e) -> None:
        pass

    def add_last(self, e) -> None:
        if self.is_empty():
            self.__last = self.__first = StudentsDoubleLinkedList.Node(e)
        else:
            self.__last._next = StudentsDoubleLinkedList.Node(e, None, self.__last)
            self.__last = self.__last._next
        self.__size += 1

    def remove_first(self) -> bool:
        pass

    def remove_last(self) -> bool:
        pass

    def first(self) -> Student:
        return self.__first._data

    def last(self) -> Student:
        return self.__last._data

    def add(self, e) -> None:
        self.add_first(e)

    def remove(self, e) -> None:
        self.remove_last()

    def empty(self) -> None:
        self.__first = self.__last = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size


class StudentsArrayQueue(Queue):
    def __init__(self):
        self._arr = [None] * 10
        self._size = 0
        self._first = 0

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass

    def first(self):
        pass

    def last(self):
        pass

    def add(self, e) -> None:
        self.enqueue(e)

    def remove(self, e) -> None:
        self.dequeue()

    def empty(self) -> None:
        self._size = 0
        self._first = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size


class StudentsLinkedStack(Stack):
    class Node:
        def __init__(self, d = None, n = None):
            self._next = n
            self._data = d

    def __init__(self):
        self._first = None
        self._size = 0

    def push(self, e):
        pass

    def pop(self):
        pass

    def top(self):
        return self._first

    def add(self, e) -> None:
        self.push(e)

    def remove(self, e) -> None:
        self.pop()

    def empty(self) -> None:
        self.__size = 0
        self._first = None

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def print(self):
        temp = self._first
        while temp != None:
            print(temp._data.get_name())
            temp = temp._next