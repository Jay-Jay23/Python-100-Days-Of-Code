# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_sum = 0

for total in student_heights:
    height_sum = total + height_sum

student_sum =0
for total in student_heights:
    student_sum = student_sum + 1

average_height =round(height_sum/student_sum)
print(average_height)
