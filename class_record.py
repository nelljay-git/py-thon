added_students = []
added_grades = []

while True:
    user_input = input("Enter student name: ")
    user_input_id = int(input("Enter student id: "))

    user_input = user_input.upper()

    added_students.append(user_input)
    added_grades.append(user_input_id)

    print(f"{user_input} added to the list!")
    for i in range(len(added_students)):
        print(f"{added_students[i]} ID: {added_grades[i]}")