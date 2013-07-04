def count_list(var1, var2):

    i = 0
    numbers = []

    for i in range(0, var1, var2):
        print "At the top i is %d" % i
        numbers.append(i)

#        i += var2
        print "Number now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num



