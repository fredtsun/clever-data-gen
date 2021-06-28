import random
from collections import defaultdict, OrderedDict

import models as m


class ReferenceCache:
    def __init__(self):
        self._cache = defaultdict(list)

    def add(self, type, data):
        self._cache[type].append(data)

    def retrieve_random(self, type):
        return random.choice(self._cache[type])

    def retrieve_all(self, type):
        return self._cache[type]


def generate_school(index, rc: ReferenceCache):
    school = m.School(
        **{
            "School_id": f"id_{index}",
            "School_name": f"school_name_{index}",
            "School_number": f"school_number_{index}",
        }
    )
    rc.add(m.School, school.School_id)
    return school


def generate_staff(index, rc: ReferenceCache):
    all_schools = rc.retrieve_all(m.School)
    # todo make this configurable later
    skip_id = random.choice(all_schools)
    staff_id = f"staff_id_{index}"
    staff = [
        m.Staff(
            **{
                "School_id": school_id,
                "Staff_id": staff_id,
                "Staff_email": f"Fn.Ln+{index}@fakemail.com",
                "First_name": "Staff Fn",
                "Last_name": f"Ln {index}",
            }
        )
        for school_id in all_schools if school_id != skip_id 
    ]
    rc.add(m.Staff, staff_id)
    return staff


def generate_student(index, rc: ReferenceCache):
    student = m.Student(
        **{
            "School_id": rc.retrieve_random(m.School),
            "Student_id": f"student_id_{index}",
            "First_name": "Student Fn",
            "Last_name": f"Ln {index}",
        }
    )
    rc.add(m.Student, student.Student_id)
    return student


def generate_teacher(index, rc: ReferenceCache):
    teacher = m.Teacher(
        **{
            "School_id": rc.retrieve_random(m.School),
            "Teacher_id": f"teacher_id_{index}",
            "First_name": "Teacher Fn",
            "Last_name": f"Ln {index}",
        }
    )
    rc.add(m.Teacher, teacher.Teacher_id)
    return teacher


def generate_section(index, rc: ReferenceCache):
    section = m.Section(
        **{
            "School_id": rc.retrieve_random(m.School),
            "Section_id": f"section_id_{index}",
            "Teacher_id": rc.retrieve_random(m.Teacher),
            "Name": f"Section {index}"
        }
    )
    rc.add(m.Section, section.Section_id)
    return section


def generate_enrollment(index, rc: ReferenceCache):
    return m.Enrollment(
        **{
            "School_id": rc.retrieve_random(m.School),
            "Section_id": rc.retrieve_random(m.Section),
            "Student_id": rc.retrieve_random(m.Student),
        }
    )


DataGenMapping = OrderedDict(
    {
        m.School: generate_school,
        m.Staff: generate_staff,
        m.Student: generate_student,
        m.Teacher: generate_teacher,
        m.Section: generate_section,
        m.Enrollment: generate_enrollment,
    }
)


def generate(config, rc: ReferenceCache):
    _map = {}
    for datatype, genfunc in DataGenMapping.items():
        count = config[datatype].get("count", 0)
        assert count > 0, "%s count must be at least 1" % datatype.__name__
        data = []
        for i in range(count):
            gendata = genfunc(i, rc)
            if isinstance(gendata, list):
                data += gendata
            else:
                data.append(gendata)
        _map[datatype] = data
    return _map
