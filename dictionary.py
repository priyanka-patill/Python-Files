student_records = {
    "student1": {"name": "Pooja", "grades": [99,98,100], "attendance": 25},
    "student2": {"name": "Manav", "grades": [92,89,95], "attendance": 20},
    "student3": {"name": "Aniket", "grades": [90, 88, 93], "attendance": 22},
}

# Function to add or update a student record
def add_or_update_student(student_id, name, grades, attendance):
    student_records[student_id] = {"name": name, "grades": grades, "attendance": attendance}

# Function to display all student records
def display_records():
    for student_id, record in student_records.items():
        print(f"ID: {student_id}, Name: {record['name']}, Grades: {record['grades']}, Attendance: {record['attendance']}")

# Example usage
display_records()
print("\nAdding a new student...\n")
add_or_update_student("student4", "Saarthak", [89, 92, 85], 21)
display_records()
print("\nUpdating student2...\n")
add_or_update_student("student2", "Manav", [90, 80, 88], 19)
display_records()
