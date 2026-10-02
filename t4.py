subjects = ["Maths", "Physics", "Chemistry", "English", "Hindi"]

student_marks = []
name=input("Enter your name :")
for subject in subjects:
     mark = int(input(f"Enter {subject} marks : "))
    # yahan subject aur mark dictionary mein store karo
     student_marks.append(mark)

student = {
      "marks":student_marks,
      "name":name
}

total = 0
passed=0
failed=0

for mark in student["marks"]:
    total += mark
    if mark >32:
       result='pass'
       passed+=1
    else:
        result = 'fail'
        failed+=1
average = total / len(student["marks"])
y = max(student["marks"])
z = min(student["marks"])

if average >89:
   grade = 'A'

elif average > 74:
     grade = 'B'

elif average > 59:
     grade = 'C'

elif average > 32:
     grade = 'D'

else:
     grade = 'F'
for i in range(len(subjects)):
    print(subjects[i], ":", student_marks[i])

print("Name:", student["name"])
print("Total:", total)
print("Average:", average)
print("maximum marks:",y)
print("minimum marks:",z)
print("result:",result)
print("subject passed:",passed)
print("subject failed:",failed)
print("your Grade:",grade)

