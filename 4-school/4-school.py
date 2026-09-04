from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Student:
    name: str
    marks: dict


class Statics(ABC):
    @abstractmethod
    def average(self, stud_list):
        raise NotImplementedError


class Notifier(ABC):
    @abstractmethod
    def notify(self, name):
        raise NotImplementedError


class StudentAverage(Statics):
    def average(self, stud_list):
        res_dict = {}
        for student in stud_list:
            res_dict[student.name] = sum([v for k, v in student.marks.items()]) / len(student.marks)
        return res_dict


class CourseAverage(Statics):
    def average(self, stud_list):
        res_dict = {}
        for student in stud_list:
            for key, val in student.marks.items():      
                if res_dict.get(key) is None:
                    res_dict[key] = val  
                else:
                    res_dict[key] = (res_dict[key] + val) / 2
        return res_dict


class ConsoleNotifier(Notifier):
    def notify(self, name):
        print(f'{name} - у этого ученика средний бал < 3.5:')

@dataclass
class Journal:
    students: list[Student] = field(default_factory=list)

    def add_student(self, student: Student):
        self.students.append(student)

    def list_student(self):
        return self.students

@dataclass
class StatisticsService:
    journal: Journal
    statistics: Statics

    def get_statistics(self):
        return self.statistics.average(self.journal.list_student())

@dataclass
class Monitoring:
    journal: Journal
    statistics: Statics
    notifier: Notifier

    def run_monitor(self):
        students = self.statistics.average(self.journal.list_student())
        for name, mark in students.items():
            if mark < 3.5:
                self.notifier.notify(name)


journal = Journal()

journal.add_student(Student('Alex', {'math': 2, 'physics': 4}))
journal.add_student(Student('Masha', {'math': 3, 'physics': 5}))
print(journal.list_student())

student_stat = StatisticsService(journal, StudentAverage())
res = student_stat.get_statistics()
print(res)

course_stat = StatisticsService(journal, CourseAverage())
res = course_stat.get_statistics()
print(res)

monitor = Monitoring(journal, StudentAverage(), ConsoleNotifier())
monitor.run_monitor()