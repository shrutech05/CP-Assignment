# 1. Create a CSV File and Read It to Convert Data into a Dictionary

import csv

# Create a CSV file with student data
data = [
    ['RollNo', 'Name', 'Subject1', 'Subject2', 'Subject3', 'Total'],
    [1, 'Alice', 85, 90, 88, 0],
    [2, 'Bob', 78, 82, 79, 0],
    [3, 'Charlie', 92, 85, 91, 0]
]

with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

students_dict = {}
with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = row['RollNo']
        row['Total'] = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        students_dict[rollno] = row

print("2. Student Data Dictionary:")
print(students_dict)


# 2. Create a VCard from Contact Details

# Accept contact details from the user and create a vCard
def create_vcard():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nADR:{address}\nEND:VCARD"
    with open(f"{name}_vcard.vcf", "w") as file:
        file.write(vcard)
    print("3. vCard created successfully!")

create_vcard()


# 3. Create a Subdirectory and Copy a File to the Subdirectory

import os
import shutil
def create_subdirectory_and_copy_file():
    subdir_path = 'new_subdirectory'
    if not os.path.exists(subdir_path):
        os.mkdir(subdir_path)
    src_file = 'source_file.txt' # Example file name
    dest_file = os.path.join(subdir_path, 'copied_file.txt')
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)
        print(f"4. File copied to {dest_file}")
    else:
        print(f"{src_file} does not exist!")

create_subdirectory_and_copy_file()


# 4. Copy Contents from One File to Another and Convert Lowercase to Uppercase

def copy_and_convert_case():
    with open('source.txt', 'r') as source_file:
        content = source_file.read()
    content_upper = content.upper()
    with open('destination.txt', 'w') as destination_file:
        destination_file.write(content_upper)
    print("5. Contents copied and converted to uppercase successfully!")

copy_and_convert_case()


# 5. Merge Lines Alternately from Two Files
def merge_lines_alternatively():
    with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('merged_file.txt', 'w') as output_file:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        max_lines = max(len(lines1), len(lines2))
        for i in range(max_lines):
            if i < len(lines1):
                output_file.write(lines1[i])
            if i < len(lines2):
                output_file.write(lines2[i])
    print("6. Files merged successfully!")

merge_lines_alternatively()


# 6. Serialize and Deserialize Employee Object

import pickle

# Define an Employee class
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

# Serialize the Employee object
def serialize_employee():
    emp = Employee(101, 'John Doe', '2023-04-01', 50000)
    with open('employee.pkl', 'wb') as file:
        pickle.dump(emp, file)
    print("7. Employee object serialized successfully!")

def deserialize_employee():
    with open('employee.pkl', 'rb') as file:
        emp = pickle.load(file)
    print("Employee Details (Deserialized):")
    print(f"Empcode: {emp.empcode}, Name: {emp.empname}, DOJ: {emp.doj}, Salary: {emp.salary}")

serialize_employee()
deserialize_employee()


# 7. Remove Specific Words ('a', 'the', 'an') from a Text File

# Remove specific words and replace them with a blank space
def remove_words_from_file():
    with open('text_file.txt', 'r') as file:
        content = file.read()
    content_modified = content.replace('a ', ' ').replace('the ', ' ').replace('an ', ' ')
    with open('modified_text_file.txt', 'w') as new_file:
        new_file.write(content_modified)

    print("8. Words removed and file modified successfully!")

remove_words_from_file()
