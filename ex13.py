from sys import argv

script, fname, lname = argv

print "The script is called:", script
print "Your name is:", fname + " " + lname

age = raw_input("How old are you? ")

print "Thanks " + fname + " you are " + age + " years old."
