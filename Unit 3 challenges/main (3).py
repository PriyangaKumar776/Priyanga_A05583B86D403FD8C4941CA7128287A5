class Student:
    def _init_(self, name, roll_number, gpa):
        self.name = name
        self.roll_number = roll_number
        self.gpa = gpa

    def _repr_(self):
        return f"{self.name} (Roll No: {self.roll_number}, GPA: {self.gpa})"

def sort_students(student_list):
    # Use a lambda function as the key for sorting to sort by GPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.gpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "A123", 3.7),
    Student("Bob", "B456", 3.9),
    Student("Charlie", "C789", 3.5),
    Student("David", "D101", 4.0),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)