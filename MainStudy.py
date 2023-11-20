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


#this method just prints in the function without returning anything
def banjoPlaying(input):
	if(input[0].upper()	== 'R'):
		print(input, "plays banjo")
	else:
		print(input, "does not play banjo")
	return

#this method returns a longer string which is kinda weird
def banjoPlayingAlt(input):
	if(input[0].upper() == 'R'):
		return input + " plays banjo"
	else:
		return input + " does not play banjo"

#print(banjoPlayingAlt("Robert"))
#banjoPlaying("Xenon")

def countByX(count,amount):

	#you can oneline this by just returning thetemp list instead of initializing it...
	#like this:
	# return [(i+1)*count for i in range(amount)]
	#and it works.
	temp = [(i+1)*count for i in range(amount)]
	return temp
#print(countByX(3,10))

def loveFunc(flower1, flower2):
	#easier way that is shortcutting the logic
	#return flower1%2 != flower2%2
	return(True if(flower1%2 != flower2%2) else False)
#print(loveFunc(2,4))


def needleInHaystack(input):
	return "found the needle at position " + str(input.index('needle'))
	#index searches each index of the list and returns the position of what ur
	#searching for
	for i in range(len(input)):
		if(input[i] == 'needle'):
			return "found the needle at position " + str(i)

#print(needleInHaystack([2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]))
#the [::-1] is saying, start at the back
def reverseString(input):
	return input[::-1]
#print(reverseString("whatever"))

def reverseAndMirror(input1, input2):
	input1 = input2[::-1] + "@@@" + input1[::-1] + input1
	#swapcase inverse the case, so Water becomes wATER
	return input1.swapcase()
#print(reverseAndMirror("Water", "Fish")) 

def max(input):
	temp = input[0]
	for i in range(1, len(input), 1):
		if(temp < input[i]) :
			temp = input[i]
	return temp

def min(input):
	temp = input[0]
	for i in range(1, len(input), 1):
		if(temp > input[i]):
			temp = input[i]
	return temp
#there are fucking min() and max() functions that will find the max and min values
#of a list fuck me...
#print(max([12,1,2,3,4,5,132]))
#print(min([1,2,3,4,-132112, 0, -32]))

#iterating thru for loop another way:

temp =[0,1,2,3,4,2,33,321,-232]
test = temp[0]
#this starts at the second index of the temp list and continues on, apparently.
for i in temp[1:]:
	if i > test:
		test = i
#print(test)

def removeChar(s):
	#when given a string, remove all of a specific char from it
	temp = ""
	for i in s:
		if i == '!':
			pass
		else:
			temp += i


	#another way to do it... 
	#return s.replace('!','')
	#that just searches the entire string for the chars in first input, and
	#replaces them with the char in the second input
	return temp
#print(removeChar("Hello! World!"))

def repeatingStr(num, string):
	return string * num
#print(repeatingStr(3,"what"))

def feast(beast, dish):
	return beast[0] == dish[0] and beast [-1] == dish[-1] 
#print(feast("chickadee", "chocolate cakd"))

def strToNum(s):
	return int(s)
print(strToNum("-743"))

#triangle inequality theorem... 
def isTriangle(a,b,c):
	return a+b > c and a+c > b and b+c >a
#print(isTriangle(4,2,3))

def countPosSumNeg(arr):
	temp = [0,0]
	if not arr:
		return temp.clear()
	for i in arr:
		if i > 0:
			temp[0]+=1
		else:
			temp[1]+=i
	return temp
def posNegAlt(arr):
	pos = sum(1 for x in arr if x > 0)
	neg = sum(i for i in arr if i < 0)
	return [pos, neg] if len(arr) else []
#print(posNegAlt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
#print(countPosSumNeg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

def growing(arr):
	temp = 1
	for i in arr:
		temp*=i
	return temp
	
print(growing([1,2,3,4,5,0]))

#there is a multiplication function in math that multiplies everything together...
#math.prod(input list i think)






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