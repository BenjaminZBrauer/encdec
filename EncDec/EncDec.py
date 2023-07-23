"""
Encryption/Decryption Program:
	-e "YourStringToEncrypt"	  Encrypt a string
	-d "YourStringToDecrypt"	  Decrypt a string
	-h or --help			  This text you are reading

The code in encryption/__init__.py is generated on every call to this program.
- To modify the execution order, edit the "executionOrder" list in this file.
- To add new functions (and their inversions for decryption), modify "encryption/__init__.py"
- To expand upon the XMLP functionality, new features can be implemented in "xmlp/__init__.py"
"""
import sys
import encryption as encryptor
from xmlp import xmlPreProcessor as fileParser

executionOrder = [0,1,0,2,5,2,2]
flag = None
myParser = fileParser()
myParser.parseFile("encryption/__init__.py",executionOrder,flag)
g_Mode = None

def Set_Program_Mode(mode):
	global g_Mode
	g_Mode = mode[1].lower()

if len(sys.argv)==1:
		print(__doc__)
		exit()	

if (len(sys.argv)>1):
	Set_Program_Mode(sys.argv[1])

	if sys.argv[1]=="--help" or sys.argv[1]=="-h":
		print(__doc__)
		exit()

	elif g_Mode == 't':
		testString = "This is a test string :)."
		print(testString)
		x = encryptor.functionPipeliner(encryptor.getEncFunctions(),testString)
		print(x)
		x = encryptor.functionPipeliner(encryptor.getDecFunctions(),x)
		print(x)
		exit()

if (len(sys.argv)==3):
	if sys.argv[2][0] == '-':
		sys.argv[1],sys.argv[2] = sys.argv[2], sys.argv[1]

	if g_Mode == 'e':
		x = encryptor.functionPipeliner(encryptor.getEncFunctions(),sys.argv[2])
		print(x)
	elif g_Mode == 'd':
		x = encryptor.functionPipeliner(encryptor.getDecFunctions(),sys.argv[2])
		print(x)

	else:
		print("Unrecognized flag (are you calling \"python EncDec.py [-e or -d] [\"stringToProcess\"]  ?\"")
		print("exiting...")
		exit()
else:
	print("EncDec.py invalid arguments.")
	print("exiting...")
	print(__doc__)
	exit()