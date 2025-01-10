name : str = input("Enter Your Name:")
fathername : str = input("Enter Your Father Name:")
rollno : int = int(input("Enter Your Roll Number:"))
date : str = input("Enter The Date:")
year : int = int(input("Enter Your Year:"))
total_marks = ("100")
subject_list = ["Maths","Physics", "Chemistry", "Computer Science", "English"]
marks_list = []

marks_list.append(int(input("Enter Maths Marks:")))
marks_list.append(int(input("Enter Physics Marks:")))
marks_list.append(int(input("Enter Chemistry Marks:")))
marks_list.append(int(input("Enter Computer Science Marks:")))
marks_list.append(int(input("Enter English Marks:")))

maths_grade = "A*" if marks_list[0] >= 90 else "A" if marks_list[0] >= 80 else "B" if marks_list[0] >= 70 else "C" if marks_list[0] >= 60 else "D" if marks_list[0] >= 50 else "F"
physics_grade =  "A*" if marks_list[1] >= 90 else "A" if marks_list[1] >= 80 else "B" if marks_list[1] >= 70 else "C" if marks_list[1] >= 60 else "D" if marks_list[1] >= 50 else "F"
chemistry_grade = "A*" if marks_list[2] >= 90 else "A" if marks_list[2] >= 80 else "B" if marks_list[2] >=70 else "C" if marks_list[2] >= 60 else "D" if marks_list[2] >= 50 else "F"
computer_science_grade = "A*" if marks_list[3] >= 90 else "A" if marks_list[3] >= 80 else "B" if marks_list[3] >=70 else "C" if marks_list[3] >= 60 else "D" if marks_list[3] >= 50 else "F"
english_grade = "A*" if marks_list[4] >= 90 else "A" if marks_list[4] >= 80 else "B" if marks_list[4] >=70 else "C" if marks_list[4] >= 60 else "D" if marks_list[4] >= 50 else "F"

maths_marks = marks_list[0]
physics_marks = marks_list[1]
chemistry_marks = marks_list[2]
computer_science_marks = marks_list[3]
english_marks = marks_list[4]


maths = f"You obtained {maths_marks} marks out of {total_marks} in Maths. Your grade is {maths_grade}"
physics = f"You obtained {physics_marks} marks out of {total_marks} in Physics. Your grade is {physics_grade}"
chemistry = f"You obtained {chemistry_marks} marks out of {total_marks} in Chemistry. Your grade is {chemistry_grade}"
computer_science = f"You obtained {computer_science_marks} marks out of {total_marks} in Computer Science. Your grade is {computer_science_grade}"
english = f"You obtained {english_marks} marks out of {total_marks} in English. Your grade is {english_grade}"

name = f"Students Name : {name}"
fathername = f"Father's Name : {fathername}"
rollno = f"Roll Number : {rollno}"
date = f"Date : {date}"
year = f"Year : {year}"
print("***********************************************************")
print("*************************")

print(name)
print(fathername)
print(rollno)
print(date)
print(year)
print(maths)
print(physics)
print(chemistry)
print(computer_science)
print(english)
