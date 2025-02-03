Lname = input("Enter last name: ")
Fname = input("Enter first name: ")
Age = input ("Enter age: ")
Contactnmb = input("Enter contact number: ")
Course = input("Enter course: ")

studin = f"Last Name: {Lname}\n First Name: {Fname}\n Age: {Age}\n Contact Number: {Contactnmb}\n Course: {Course}\n"
with open("student.txt", "a") as file:
    file.write(studin)
print ("Student information has been saved to 'student.txt'. ")