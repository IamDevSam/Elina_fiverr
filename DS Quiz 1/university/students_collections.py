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
        pass

    ''' Task 3: Implement add_before function which adds the Student e before the first occurrence of Student a in list.
        False is returned if Student a is not found in list. '''
    def add_before(self, a: Student, e: Student) -> bool:
        pass

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
        return self.__first._data

    def last(self) -> Student:
        return self.__last._data

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
        pass

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