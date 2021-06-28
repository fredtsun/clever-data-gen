# Configuration (how much data should be generated, etc) just make this a big dictionary or something.
# Generation logic for each data type (staff, students, teachers, etc.)
# Linking resources together (i.e.) users get generated first, ids are saved somewhere so other data types can reference them.
# Serializing the generated data into a CSV
from os import write
from writer import write_to_csv
from generate import ReferenceCache, generate
import models as m

config = {
    m.School: {"count": 300},
    m.Staff: {"count": 15000},
    m.Student: {"count": 200},
    m.Teacher: {'count': 20},
    m.Section: {'count': 100},
    m.Enrollment: {'count': 100},
}

def main():
    rc = ReferenceCache()
    data = generate(config, rc)
    write_to_csv('./', data)

if __name__ == "__main__":
    main()
