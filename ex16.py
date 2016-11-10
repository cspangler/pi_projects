from sys import argv

script, filename = argv
prompt = ">>> "

print "We're going to erase this file --> %r <--" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want to erase this file, hit RETURN."

raw_input(prompt)

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file... >>>Completed<<<"
target.truncate()

print "Now I'm going ask you to input 3 lines of text."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Writing lines to file...>>>Completed<<<"

updated_text = line1 + "\n" + line2 + "\n" + line3 + "\n"

target.write(updated_text)

print "And finally, we close the file."
target.close()

print "Now would you like to open the file and read it?"
print "Hit CTRL-C (^C) to abort OR RETURN to continue."
raw_input(prompt)

print "Type the filename you wish to open:"
file_again = raw_input(">>> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
