import time

students =[]

while True:
 name = input("What is the student name?:")
 age = input("What is the student age?:")
 gender = input("What is the students gender?:")
 course = input("what is the students course?:")

 applicant = {
    "name": name,
    "age": age,
    "gender": gender,
    "course": course,
 }


 students.append(applicant)

 print("please wait. We are procesing the data...")
 time.sleep(1.8)

 print("A student has been added to the portal.")
 print(students)

 time.sleep(1.8)

 print("A students has been added to the portal.")
 print(students)

 time.sleep(0.5)

 #option to procceed or exit the program
 option = input("Do you want to continue?(y/n):")

 if option == "y":
    continue
 elif option == "n":
    break
 else:
    print("Invalid command. Will stop anyway. Till future notice")
    time.sleep(0.5)
    break