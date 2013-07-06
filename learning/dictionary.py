#Dictionary representing uniform distribution of probabilities of rolling dice
mydict = {1:1/6.0, 2:1/6.0, 3:1/6.0, 4:1/6.0, 5:1/6.0, 6:1/6.0}
mydictComprehension = {x:1/6.0 for x in xrange(1,6)}
print mydict
print mydictComprehension
