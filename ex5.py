my_name = 'Charles W. Spangler'
my_age = 40 #years
my_age_mo = my_age * 12 #months
my_age_day = my_age * 365 #days
my_age_hour = my_age_day * 24 #hours
my_age_min = my_age_hour * 60 # minutes
my_age_sec = my_age_min * 60 # seconds
my_height = 68 #inches
my_cent_height = my_height / 2.54 #in centimeters
my_weight = 230 #lbs
my_kilo_weight = my_weight / 2.20 #in kilograms
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'
e1 = "C"
e2 = "h"
e3 = "e"
e4 = "e"
e5 = "s"
e6 = "e"
e7 = "B"
e8 = "u"
e9 = "r"
e10 = "g"
e11 = "e"
e12 = "r"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "That's %d centimeters for the UK folks." % my_cent_height
print "He's is %s years old." % my_age
print "That is %d days OR %d months old." % (my_age_day, my_age_mo)
print "Or %d hours OR %d seconds old." % (my_age_hour, my_age_sec)
print "He's %d pounds heavy." % my_weight
print "Thats %d kilograms for you Brits." % my_kilo_weight
print "Acutually that is pretty overweight!"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth


#the next line is tricky
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight
)
print "." * 40
print e1 + e2 + e3 + e4 + e5 + e6,
print e7 + e8 + e9 + e10 + e11 + e12
