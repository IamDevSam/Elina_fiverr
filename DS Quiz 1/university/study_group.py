"""This module is designed for study groups."""
from typing import List, Optional

from university.students import Student


class StudyGroup:
    """This class is for study groups."""

    def __init__(self, name: str):
        """
        Constructor of the study group.
        :param name: name of the group
        :param students: list of the students
        """
        self.__name: str = name
        self.__students: List[Student] = list()

    def add_students(self, students: list) -> None:
        """
        Add new students.
        :param students: list of the students
        :return:
        """
        for student in students:
            self.add_student(student)


    def add_student(self, student: Student) -> None:
        """
        Add new student.
        :param student: student object
        :return:
        """
        self.__students.append(student)

    def run_project(self) -> None:
        """
        Run project.
        :return:
        """
        work = ""
        for student in self.__students:
            work = work + student.practice() + " \n"
        return work
