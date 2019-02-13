def loop(num):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 2
        print "Numbers now: ", numbers

        print "At the bottom i is %d" %i

        print "The numbers: "

        for k in numbers:
            print k

loop(10)
