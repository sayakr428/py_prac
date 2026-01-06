students = {
    "Sayak": {
        "Degree": "B.Tech in CSE",
        "Age": 24,
        "University": "SRM University",
        "Location": "Remote",
        "Company": "Derq",
        "Experience": "3 Years",
        "Role": "AI Infrastructure & Automation Engineer"
    },
    "Shlok": {
        "Degree": "B.Tech in CSE",
        "Age": 24,
        "University": "SRM University",
        "Location": "Noida",
        "Company": "Magicine Pharma",
        "Experience": "3 Years",
        "Role": "Software Engineer"
    }
}

students.update({
    "Arbind": {
        "Degree": "B.Tech in CSE",
        "Age": 24,
        "University": "SRM University",
        "Location": "Hyderabad",
        "Company": "Deloitte",
        "Experience": "3 Years",
        "Role": "IAM Consultant"
    }
})

print("Current Students in the Database:")
for name in students:
    print(f"{name} - {students[name]['Role']} at {students[name]['Company']}")  

input_name = input("Enter the name of the student: ")

found = False

for name in students:
    if name == input_name:
        print(students[name])
        found = True
        break

if not found:
    print("Student not found.")

print(dir(students))
