# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#average heigth without using len or sum functions
#find the lenght of the list without using the len function like this
i=0
for sh in student_heights:
    i += 1
#print(i)
# find the sum with for loop
totalsum=0
for sh in student_heights:
    totalsum = totalsum + sh
#print(totalsum)

average_height = totalsum / i
print(round(average_height))