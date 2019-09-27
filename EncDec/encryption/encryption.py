import string as strs, binascii, random, sys
from xmlp.xmlp import xmlPreProcessor as fileParser

#<ignore>
__randomHexPair = lambda: "".join([random.choice(strs.hexdigits) for i in range(2)])
__randomDigitPair = lambda: "".join([random.choice("3456789") for i in range(2)])

def functionPipeliner(functions, x):
	f = functions.pop()
	if (len(functions))>0:
		return f(functionPipeliner(functions, x))
	else:
		return f(x)

def __reverse(x):
	bufferArray = []
	i = 0
	while (i<len(x)):
		bufferArray.insert(0, x[i])
		i+=1
	return "".join(bufferArray)

def __toList(x):
	bufferArray = []
	i = 0
	while (i<len(x)):
		bufferArray.append(x[i])
		i+=1
	return bufferArray

def __fibonacciStepBack(p,pp):
		return p, pp, p-pp
#</ignore>


#<Forward>
def Invert(x):
	return __reverse(x)

def toHex(x):
	return binascii.hexlify(x.encode('utf-8')).decode('utf-8')

def firstInversion(x):
	x = __toList(x)
	x.insert(0, x.pop())
	return "".join(x)


def checkeredInsertion(x):
	bufferZone = []
	i = 0
	while (i<len(x)):
		bufferZone.append(x[i])
		bufferZone.append(__randomHexPair())
		i += 1
	
	return "".join(bufferZone)

def fibonacciInsertion(x):
	x = __toList(x)
	i = 0
	current,prev,prev_prev = 1, 0, 0
	while (current<len(x)):
		if (prev ==0 and prev_prev==0):
			current=1
		else:
			current = prev+prev_prev
		x.insert(current, __randomHexPair())
		prev_prev = prev
		prev = current
	return "".join(x)

def snake(x):
	mainBuffer = []
	x = __toList(x)
	pair = __randomDigitPair()
	x.append(__randomHexPair())
	x.insert(0,__randomHexPair())
	x.append(pair[1])
	x.insert(0, pair[0])
	x.append(__randomHexPair())
	x.insert(0, __randomHexPair())
	x = "".join(x)

	i = 0
	directionalStep = 1
	while (i<len(x)):
		temp = "".join(x[i:i+int(pair[0])])
		if directionalStep>0:
			mainBuffer.append(temp)
		else:
			mainBuffer.append(__reverse(temp))
		i+=int(pair[0])
		directionalStep *= -1
	return "".join(mainBuffer)
	
#</Forward>


#<Reverse>
def Invert(x):
	return __reverse(x)

def toString(x):
	return binascii.unhexlify(x.encode('utf-8')).decode('utf-8')

def rootPosition(x):
	x = __toList(x)
	x.append(x.pop(0))
	return "".join(x)
	
def checkeredDigest(x):
	bufferZ = []
	i = 0
	while (i<len(x)):
		bufferZ.append(x[i])
		i+=3
	
	return "".join(bufferZ)

def fibonacciDigest(x):
	if len(x)==1:
		return x
	bufferZone = __toList(x)
	current,prev,prev_prev = 0, 0, 0
	counter = 0
	while ((current+(counter))<len(bufferZone)):
		if (current==0):
			current = 1
		else:
			current = prev+prev_prev
		counter += 1
		prev_prev = prev
		prev = current
	current, prev, prev_prev = __fibonacciStepBack(prev, prev_prev)
	counter -= 1
	while (counter>=0):
		current, prev, prev_prev = __fibonacciStepBack(prev, prev_prev)
		counter -= 1
		bufferZone.pop(counter+current)
		bufferZone.pop(counter+current)
			
	return "".join(bufferZone)

def unSnake(x):
	mainBuffer = []
	key=int(x[2])
	i = 0

	directionalStep = 1
	while (i<len(x)):
		temp = "".join(x[i:i+key])
		if directionalStep>0:
			mainBuffer.append(temp)
		else:
			mainBuffer.append(__reverse(temp))
		i += key
		directionalStep *= -1
	return "".join(mainBuffer)[5:-5]
	
#</Reverse>

### EXECUTION FRAMEWORK

#<generate>

def getEncFunctions():
	return [lambda x: Invert(x), lambda x: toHex(x), lambda x: Invert(x), 
		lambda x: firstInversion(x), lambda x: Invert(x), lambda x: checkeredInsertion(x), 
		lambda x: Invert(x), lambda x: fibonacciInsertion(x), lambda x: Invert(x), 
		lambda x: fibonacciInsertion(x), lambda x: snake(x), lambda x: Invert(x), 
		lambda x: snake(x), lambda x: firstInversion(x), lambda x: firstInversion(x)]

def getDecFunctions():
	return [lambda x: rootPosition(x), lambda x: rootPosition(x), lambda x: unSnake(x), 
		lambda x: Invert(x), lambda x: unSnake(x), lambda x: fibonacciDigest(x), 
		lambda x: Invert(x), lambda x: fibonacciDigest(x), lambda x: Invert(x), 
		lambda x: checkeredDigest(x), lambda x: Invert(x), lambda x: rootPosition(x), 
		lambda x: Invert(x), lambda x: toString(x), lambda x: Invert(x)]

#</generate>

executionOrder = [0,1,0,2,0,3,0,4,0,4,5,0,5,2,2]
flag = None
myParser = fileParser()
myParser.parseFile(sys.argv[0],executionOrder,flag)
 
 #TESTING AREA (MAIN)
string = "This is a test string"
print(string)
string = functionPipeliner(getEncFunctions(), string)
print(string)
string = functionPipeliner(getDecFunctions(), string)
print(string)
