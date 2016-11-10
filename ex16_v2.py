prompt = ">>> "

print "What's your first name?"
fname = raw_input(prompt)

print "Thanks %s! What file would you like to open?" % fname
target = raw_input(prompt)

print "Opening the file... %s" % target
target_open = open(target, 'a+')

print "File Name: ", target_open.name
print "Is file closed: ", target_open.closed
print "Opened in mode: ", target_open.mode
print "\n"

print "Lets read the contents of the file then append some data."
print "Hit RETURN to continue "
raw_input(prompt)

print target.read()

print "\n" + "Now lets append some data to the end of the file."
print "Hit RETURN to continue "
raw_input(prompt)

print "I am going to ask for 3 lines of text."
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

updated_text = line1 + "\n" + line2 + "\n" + line3 + "\n"
target_open.write(updated_text)

print "Here is the appended file contents...."
print target.read()

print "Closing the file... %s" % target_open
target_open.close()
print "Is the file closed: ", target_open.closed
