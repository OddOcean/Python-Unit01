############################################################################
#     Aidan Weygandt                        2.11.2021                      #
#     Unit 2 Problems                                                      #
#.    Age calculator, sum of digits, initial deposit, current time.        #
############################################################################
import math
print ("Problem #1\nI am a student at:"'\n')
print (" PPPPP    HH       HH     SSSSSS")
print ("PP    P   HH       HH   SS      SS")
print ("PP    P   HH       HH    SS     ")
print ("PPPPPP    HHHHHHHHHHH       SS")
print ("PP        HH       HH         SS")
print ("PP        HH       HH   SS      SS")
print ("PP        HH       HH     SSSSSS\n")

print ("Problem #2\nThe sum of the equation is:")
print ((58*42-35*55-11)/(14-4))
print ("\nProblem #3\nThe sum of 1+2+3+4+5+6+7+8+9 is:")
print (1+2+3+4+5+6+7+8+9)

print ("\nProblem #4\nThe area of a circle with a radius of 5.5 is:")
print ((13.86*13.86)*math.pi)

print ("\nProblem #5\nThe perimeter of a 4.5x7.5 rectangle is:")
print (4.5*2+7.5*2)
print ("The area of a 4.5x7.5 rectangle is:")
print (4.5*7.5)
popul = 312032486 #population of us

print ("\nProblem #6\nAssuming a world population of",popul)
maths = ((365*24*60*60)//7) #finds seconds per year and outputs one birth per 7 seconds
print ("If there is one birth every 7 seconds then there are",maths,"births per year")
moremaths = ((365*24*60*60)//13) #finds seconds per year and outputs one death per 13 seconds
print ("And if there is one death every 13 seconds then there are",moremaths,"deaths per year")
evenmoremaths = ((365*24*60*60)//45) #finds seconds per year and outputs one immagrent per second
print ("If there is one new immigrant every 45 seconds then there are",evenmoremaths,"new immigrants per year")
toomuchmaths = (maths - moremaths + evenmoremaths) #total people gained per year
print ("That means there is a net gain of",toomuchmaths,"people per year")
oneY = popul + toomuchmaths #population after one year
twoY = oneY + toomuchmaths #population after two years
threeY = twoY + toomuchmaths #population after three years
fourY = threeY + toomuchmaths #population after four years
fiveY = fourY + toomuchmaths #population after five years
print ("In one year there will be",oneY,"people in the US")
print ("In two years there will be",twoY,"people in the US")
print ("In three years there will be",threeY,"people in the US")
print ("In four years there will be",fourY,"people in the US")
print ("In five years there will be",fiveY,"people in the US")