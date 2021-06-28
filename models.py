from dataclasses import dataclass
import abc


class CleverData:
    pass


@dataclass
class School(CleverData):
    School_id: str
    School_name: str
    School_number: str


@dataclass
class Staff(CleverData):
    School_id: str
    Staff_id: str
    Staff_email: str
    First_name: str
    Last_name: str


@dataclass
class Student(CleverData):
    School_id: str
    Student_id: str
    First_name: str
    Last_name: str


@dataclass
class Teacher(CleverData):
    School_id: str
    Teacher_id: str
    First_name: str
    Last_name: str


@dataclass
class Section(CleverData):
    School_id: str
    Section_id: str
    Teacher_id: str
    Name: str

@dataclass
class Enrollment(CleverData):
    School_id: str
    Section_id: str
    Student_id: str
