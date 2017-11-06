__author__ = 'admin'
from robot.libraries.BuiltIn import BuiltIn
#rangeVar=
def numEval(rangeVar):
    a= []
    print "arg: %d" ,rangeVar
    rangeVar=   int(rangeVar)+1
    for i in range(1,rangeVar):
        if (i%3==0):
            if(i%3==0 and i%5==0):
                print "FizzBUzz"
                a.append("FizzBuzz")
            else:
                print "Fizz"
                a.append("Fizz")
        elif(i%5==0):
            if(i%3==0 and i%5==0):
                print "FizzBUzz"
                a.append("FizzBuzz")
            else:
                print("BUZZ")
                a.append("Buzz")
        else:
            print i
            a.append(i)
    return a
#numEval(101)


