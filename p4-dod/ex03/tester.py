from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except Exception as e:
    print(f"TypeError: {e}")
