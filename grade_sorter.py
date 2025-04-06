import time as time_stone

# Colors

YELLOW = "\033[93m"
RESET = "\033[0m"

name = "Wneljae"
students_name = ["ESP", "TLE", "Math", "English", "Filipino", "Science", "Mapeh"]
students_id = [76, 70, 75, 74, 74, 74, 73]
students_count = str(len(students_name))
gpa_student = round(sum(students_id) / 7)
for_i = (len(students_name))

print(f"Total students listed: {students_count}")
for i in range(for_i):
     print(f"{students_name[i]} -> {students_id[i]}")
   #  time_stone.sleep(1)
print(f"Total GPA of {name} is: {YELLOW}{gpa_student}{RESET}")
if gpa_student <= 75:
     print("Failed")
elif gpa_student > 75:
     print("Passed")