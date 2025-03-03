import time as time_stone

# Colors

YELLOW = "\033[93m"
RESET = "\033[0m"

name = "Mark"
students_name = ["ESP", "TLE", "Math", "English", "Filipino", "Science", "Mapeh"]
students_id = [76, 70, 75, 74, 74, 74, 73]
students_count = str(len(students_name))
gpa_student = round(sum(students_id) / 7)

print(f"Total students listed: {students_count}")
for i in range(len(students_name)):
     print(f"{students_name[i]} -> {students_id[i]}")
   
print(f"Total GPA of {name} is: {YELLOW}{gpa_student}{RESET}")
if gpa_student <= 75:
     print("Failed")
elif gpa_student > 75:
     print("Passed")
