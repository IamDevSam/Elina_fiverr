"""This module is for university management."""
from collections import deque
from typing import Optional, List

from university.program import Program
from university.students import Student, ESStudent, CSStudent, DSStudent
from university.study_group import StudyGroup


class UniversityManagementSystem:
    """This class is for university management."""
    ID = 0

    def __init__(self, name: str):
        """
        The constructor of the UniversityManagementSystem class.
        :param name:
        """
        self.__name: str = name
        self.__students: List[Optional[Student]] = list()
        self.__study_groups: deque = deque()

    def add_student(self, name: str, surname: str, gy: int, program_type: Program) -> None:
        """
        Adding new student.
        :param name:
        :param surname:
        :param program_type:
        :return:
        """
        if program_type == Program.ComputerScience:
            student = CSStudent(name, surname, gy, UniversityManagementSystem.ID)
        elif program_type == Program.DataScience:
            student = DSStudent(name, surname, gy, UniversityManagementSystem.ID)
        elif program_type == Program.EngineeringScience:
            student = ESStudent(name, surname, gy, UniversityManagementSystem.ID)
        else:
            print("No such program")
            return
        UniversityManagementSystem.ID += 1
        self.__students.append(student)

    def get_student(self, name: str, surname: str) -> Optional[Student]:
        """
        Get student by name and surname.
        :param name:
        :param surname:
        :return:
        """
        for student in self.__students:
            if student.get_name() == name and student.get_surname() == surname:
                return student
        return None

    def create_study_group(self, name: str) -> StudyGroup:
        """
        Create new study group.
        :param name:
        :return:
        """
        study_group = StudyGroup(name)
        self.__study_groups.append(study_group)
        return study_group

