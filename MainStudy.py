"""
in python the script itself is executed from top to bottom, there is 
definitely a way to change that but i am not sure yet.

"""

#BTW THE WAY TO BULK FOLD STUFF IS CTRL SHIFT [ TO OPEN AND CTRL SHIFT ] TO CLOSE
#LEARNING MATERIAL

#using this as filler will do more with later...
def main():
	list()
#not sure if necessary but it's a function completer for other langauges so i'm leaving it
#here for now.
#	return(0) 



"""
technically this is a list but i am trying to figure out if there is a differnce
in python...
"""
def array():
	array1 = ["a","b","c"]
	array1[2] = "garf"
	print(array1[2])
"""
seperated them for future purposes, this will be primary learning script, fuck learning cpp
right now when i dont like using complicated IDE's and would rather just stick with text
editors.
"""
def list():
	list1 = []
	list1.append(56)
	print(list1)


"""
importing: yoinking shit from other libraries or people
literally just functions that can have a lot of stuff in it.

"""
from random import *
#imports everything from the random module

from math import sqrt
#just imports the sqrt function from math module


"""
random module works off a seed, so you can set a unique seed and use that for
your random stuff, and change it to get a different sequence of random
numbers whenever you wnat.
"""
seed(0)



def sortingTake1():

	#creating a list that has 50 spots that are all filled with 0 (the int)
	randList = [0] * 50

	#for loop counting from 0 (always starts at 0), to the amount of slots in  randlist
	for i in range(len(randList)):

		#sets each slot to a random number between 1 and 1000
		randList[i] = randrange(1,1000)
	print(randList)

	#fun function that uses quick sort (i believe) to sort through your list of ints
	#maybe doubles too, will check later
	#wont reorder the list, but instead returns a sorted list (like a new one i think)
	print(sorted(randList))


#sortingTake1()


#
"""
all codewars code goes here... 

"""


def squareSum(numbers):
	#function takes all inputs and returns the sum of the squares of those numbers
	sum = 0
	for i in numbers:
		sum += i**2

	#an alternate version instead of adding it yourself is using the sum() function
	#so instead of having multiple lines, you can do 
	#return sum(i ** 2 for i in numbers) to do the same thing
	#since you can one line
	return sum 

def numString(input):
	return str(input)

#print(numString(5999595493))

def invertNum(input):
	return -1*input
#print(invertNum(-43.24243))



"""
INFORMATION ABOUT CLASSES
"""
class tester:
	#initialization operation, makes it empty, like a reset maybe?
	#so that you can have multiple instances of this class working serperately maybe?
	def __init__(self):
		self.emptyList = []
		#you can add anything in here I imagine you can add more complex logic and other 
		#functions that would be unique to the tester class and not work unless looking in
		#here.
		pass
	def fnTest(self,a, b):
		return a+b

# #making a new class object
# x = tester()
# #calling one of the variables in the class, and you can call any of them.
# x.emptyList.append(5)
# print(x.fnTest(5,6))
# print(x.emptyList)