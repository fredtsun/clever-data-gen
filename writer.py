import csv
from dataclasses import asdict
import models as m

filenames = {
    m.School: 'schools.csv',
    m.Staff: 'staff.csv',
    m.Student: 'students.csv',
    m.Teacher: 'teachers.csv', 
    m.Section: 'sections.csv',
    m.Enrollment: 'enrollments.csv' 
}

def write_to_csv(path, generated_data_map):
	for datatype, data in generated_data_map.items():
		with open(path + filenames[datatype], 'w', newline='') as csvfile:
			fieldnames = list(datatype.__annotations__.keys())
			dw = csv.DictWriter(csvfile, fieldnames=fieldnames)
			dw.writeheader()
			dw.writerows(asdict(row) for row in data)