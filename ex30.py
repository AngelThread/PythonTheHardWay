people = 30
cars = 40
buses = 15

if cars > people: # Checks if cars' quantity more than people's
    print "We should take the cars."
elif cars < people:
    print"We should not take the cars."
else: # Then it means car == people then
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "All right let's just take the buses."
else:
    print "Fine, let's stay home then."
