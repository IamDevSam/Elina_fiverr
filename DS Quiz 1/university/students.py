"""This module is designed for student classes."""
from abc import ABC, abstractmethod


class Student(ABC):
    """Abstract base class for all students."""

    def __init__(self, name: str, surname: str, gy: int, id: int):
        """
        Student class constructor
        :param name: student's name
        :param surname: student's surname
        :param gy: student's graduation year
        :param id: student's id
        """
        self.__name: str = name
        self.__surname: str = surname
        self.__id: int = id
        self.__graduation_year = gy

    @abstractmethod
    def study(self) -> None:
        """
        Abstract method study.
        :return:
        """
        pass

    @abstractmethod
    def practice(self) -> str:
        """
        Abstract method study.
        :return:
        """
        pass

    def get_name(self) -> str:
        """
        Getting student name.
        :return:
        """
        return self.__name

    def get_surname(self) -> str:
        """
        Getting student surname.
        :return:
        """
        return self.__surname

    def get_graduation_year(self) -> str:
        """
        Getting student surname.
        :return:
        """
        return self.__graduation_year


class ESStudent(Student):
    """Class for ESStudents."""

    def __init__(self, name: str, surname: str, gy: int, id: int):
        """
        ESStudent class constructor.
        :param name:
        :param surname:
        :param graduation_year:
        :param id:
        """
        super().__init__(name, surname, id)

    def study(self) -> None:
        """Make ESStudent study. """
        print("I love developing microcontrollers")

    def practice(self) -> str:
        """Make ESStudent practice its knowledge. """
        return "Working on HW components []=[]"


class CSStudent(Student):
    """Class for CSStudent."""

    def __init__(self, name: str, surname: str, gy: int, id: int):
        """
        CSStudent class constructor.
        :param name:
        :param surname:
        :param graduation_year:
        :param id:
        """
        super().__init__(name, surname, gy, id)

    def practice(self) -> str:
        """Make CSStudent practice its knowledge. """
        return "Connecting the UI to the mainframe <<->>"


class DSStudent(Student):
    """Class for DSStudent."""

    def __init__(self, name: str, surname: str, gy: int, id: int):
        """
        DSStudent class constructor.
        :param name:
        :param surname:
        :param graduation_year:
        :param id:
        """
        super().__init__(name, surname, gy, id)

    def study(self) -> None:
        """Make DSStudent study. """
        print("I love to study DS and Algorithms")

    @abstractmethod
    def practice(self) -> str:
        """Make DSStudent practice its knowledge. """
        return "Let me figure out how to monetize it!"
