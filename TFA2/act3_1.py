Fname = input("Enter you first name: ")
Lname = input("Enter your last name: ")
Age = input ("Enter you age: ")

fullnm = Fname + " " + Lname
slicd = Fname[:4]

txt = "Hello, {}! Welcome. You are {} years old."

print ("\nFull name: ", fullnm)
print ("Sliced Name: ", slicd)
print ("Greeting Meessage: ", (txt.format(slicd, Age)))
