student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height = total_height + height

students_number = 0
for number in student_heights:
    students_number = students_number + 1

average = int(round(total_height/students_number,0))
print(average)
