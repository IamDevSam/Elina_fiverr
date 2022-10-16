# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from university.management_system import UniversityManagementSystem
from university.program import Program
from university.students_collections import StudentsSingleLinkedList, StudentsDoubleLinkedList, StudentsLinkedStack, StudentsArrayQueue
from university.students import Student


def test_task_1():
    uni = UniversityManagementSystem("AUA")
    uni.add_student("Ani", "Hakobyan", 2023, Program.ComputerScience)
    uni.add_student("Mane", "Asatryan", 2024, Program.ComputerScience)
    uni.add_student("Avet", "Gevorgyan", 2024, Program.DataScience)
    uni.add_student("Aram", "Avetisyan", 2025, Program.ComputerScience)
    uni.add_student("Nane", "Avagyan", 2023, Program.EngineeringScience)
    study_group = uni.create_study_group(" TA PSS Attendance Tracker")
    students = [
        uni.get_student("Avet", "Gevorgyan"),
        uni.get_student("Aram", "Avetisyan"),
        uni.get_student("Nane", "Avagyan"),
        uni.get_student("Ani", "Hakobyan")
    ]
    print("Running Task 1, please resolve the errors")
    study_group.add_students(students)
    print(study_group.run_project())

def test_task_2(list_class):
    uni = UniversityManagementSystem("AUA")
    uni.add_student("Ani", "Hakobyan", 2023, Program.ComputerScience)
    uni.add_student("Mane", "Asatryan", 2024, Program.ComputerScience)
    uni.add_student("Avet", "Gevorgyan", 2024, Program.DataScience)
    uni.add_student("Aram", "Avetisyan", 2025, Program.ComputerScience)
    uni.add_student("Nane", "Avagyan", 2023, Program.EngineeringScience)
    students = [
        uni.get_student("Avet", "Gevorgyan"),
        uni.get_student("Mane", "Asatryan"),
        uni.get_student("Aram", "Avetisyan"),
        uni.get_student("Nane", "Avagyan"),
        uni.get_student("Ani", "Hakobyan")
    ]
    l = list_class()
    l.add_last(students[0])
    l.add_last(students[1])
    l.add_last(students[2])
    l.add_last(students[3])
    print("Running task 2, tests for remove_at function in " + list_class.__name__)

    print("\t Trying to remove element at negative position")
    s = l.size()
    result = l.remove_at(-1)
    if result == False and l.size() == s:
        print("\t\t PASS: no element is removed")
    else:
        print("\t\t FAIL: either wrong element was removed or false positive is returned")

    print("\t Trying to remove element at position out of list boundaries");
    s = l.size()
    result = l.remove_at(s + 10)
    if result == False and l.size() == s:
        print("\t\t PASS: no element is removed")
    else:
        print("\t\t FAIL: either wrong element was removed or false positive is returned")

    print("\t Trying to remove element at 0 position");
    s = l.size()
    result = l.remove_at(0)
    if result == True and l.first() == students[1] and s == l.size() + 1:
        print("\t\t PASS: first element is successfully removed")
    else:
        print("\t\t FAIL: first element is not removed or wrong element is removed")

    print("\t Trying to remove element at last position");
    s = l.size()
    result = l.remove_at(s - 1)
    if result == True and l.last() == students[2] and s == l.size() + 1:
        print("\t\t PASS: last element is successfully removed")
    else:
        print("\t\t FAIL: last element is not removed or wrong element is removed")

def test_task_3():
    uni = UniversityManagementSystem("AUA")
    uni.add_student("Ani", "Hakobyan", 2023, Program.ComputerScience)
    uni.add_student("Mane", "Asatryan", 2024, Program.ComputerScience)
    uni.add_student("Avet", "Gevorgyan", 2024, Program.DataScience)
    uni.add_student("Aram", "Avetisyan", 2025, Program.ComputerScience)
    uni.add_student("Nane", "Avagyan", 2023, Program.EngineeringScience)
    students = [
        uni.get_student("Avet", "Gevorgyan"),
        uni.get_student("Mane", "Asatryan"),
        uni.get_student("Aram", "Avetisyan"),
        uni.get_student("Nane", "Avagyan"),
        uni.get_student("Ani", "Hakobyan")
    ]
    l = StudentsSingleLinkedList()
    l.add_last(students[0])
    l.add_last(students[1])
    l.add_last(students[2])
    print("Running task 3, tests for add_before function of SingleLinkedList")

    print("\t Trying to call function for element not in list")
    s = l.size()
    result = l.add_before(students[3], students[4])
    if result == False and l.size() == s:
        print("\t\t PASS: no new element is added after non existing element")
    else:
        print("\t\t FAIL: either wrong element was found or false positive is returned")

    print("\t Trying to add new element before first element in list");
    s = l.size()
    result = l.add_before(students[0], students[4])
    if result == True and l.size() == s + 1 and l.first() == students[4]:
        print("\t\t PASS: newly added element is the new first")
    else:
        print("\t\t FAIL: either no element was added or it was added at wrong position")

def test_task_4():
    uni = UniversityManagementSystem("AUA")
    uni.add_student("Ani", "Hakobyan", 2023, Program.ComputerScience)
    uni.add_student("Mane", "Asatryan", 2024, Program.ComputerScience)
    uni.add_student("Avet", "Gevorgyan", 2024, Program.DataScience)
    uni.add_student("Aram", "Avetisyan", 2025, Program.ComputerScience)
    uni.add_student("Nane", "Avagyan", 2023, Program.EngineeringScience)
    students = [
        uni.get_student("Avet", "Gevorgyan"),
        uni.get_student("Mane", "Asatryan"),
        uni.get_student("Aram", "Avetisyan"),
        uni.get_student("Nane", "Avagyan"),
        uni.get_student("Ani", "Hakobyan")
    ]
    l = StudentsSingleLinkedList()
    l.add_last(students[0])
    l.add_last(students[1])
    l.add_last(students[2])
    l.add_last(students[3])
    l.add_last(students[4])
    print("Running task 4, tests for graduation year iterator of SingleLinkedList")

    print("\t Trying to iterate over students graduating at 2023")
    it = l.graduation_year_iterator(2023)
    counter = 0
    while True:
        try:
            s = next(it)
            counter += 1
            if s.get_graduation_year() != 2023:
                print("\t\t FAIL: student " + s.get_name() + "graduates on " + s.get_graduation_year())
        except StopIteration:
            if counter == 2:
                print("\t\t PASS: all students returned by iterator graduate on 2023")
            else:
                print("\t\t FAIL: number of students graduating on 2023 should be 2")
            break

    print("\t Check that empty iteration is done over graduates of year 2133")

    it = l.graduation_year_iterator(2123)
    check = True
    while True:
        try:
            s = next(it)
            check = False
        except StopIteration:
            if check:
                print("\t\t PASS: there are no students graduating on 2133");
            else:
                print("\t\t FAIL: iterator does not perform empty iteration");
            break

def test_task_5():
    uni = UniversityManagementSystem("AUA")
    uni.add_student("Ani", "Hakobyan", 2023, Program.ComputerScience)
    uni.add_student("Mane", "Asatryan", 2024, Program.ComputerScience)
    uni.add_student("Avet", "Gevorgyan", 2024, Program.DataScience)
    uni.add_student("Aram", "Avetisyan", 2025, Program.ComputerScience)
    uni.add_student("Nane", "Avagyan", 2023, Program.EngineeringScience)
    students = [
        uni.get_student("Avet", "Gevorgyan"),
        uni.get_student("Mane", "Asatryan"),
        uni.get_student("Aram", "Avetisyan"),
        uni.get_student("Nane", "Avagyan"),
        uni.get_student("Ani", "Hakobyan")
    ]
    s = StudentsLinkedStack()
    s.push(students[0])
    s.push(students[1])
    s.push(students[2])
    s.push(students[3])

    add_before_rec(s,students[1], students[4])

    #s.print()

''' Task 5: Implement recursive add_before function for Students LinkedList based stack, which inserts Student n before 
the first occurrence of Student a in Stack
'''
def add_before_rec(stack: StudentsLinkedStack, a: Student, e: Student):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''Comment out the test function calls below as you proceed with the implementations. 
    Note that all tests have a dependency from the first assignment'''
    test_task_1()
    #test_task_2(StudentsSingleLinkedList)
    #test_task_2(StudentsDoubleLinkedList)
    #test_task_3()
    #test_task_4()
    #test_task_5()







