def cheese_and_crackers(cheese_count, boxes_of_cheese):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_cheese
	print "Man that enough for a party."
	print "Someone bring a cheese knife. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can make and use varibles:"
amount_cheese = 20
amount_boxes = 30
cheese_and_crackers(amount_cheese, amount_boxes)

print "We can do math inside too:"
cheese_and_crackers(10 + 10, 40 - 10)

print "We can also combine math and varibles:"
cheese_and_crackers(amount_cheese + 100,  amount_boxes * 3)
