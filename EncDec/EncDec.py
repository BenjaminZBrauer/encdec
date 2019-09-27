"""
############################################################
Encryption/Decryption Program:
	-e "YourStringToEncrypt"	  Encrypt a string
	-d "YourStringToDecrypt"	  Decrypt a string
	-h or --help			  This text you are reading
############################################################
"""
import sys
import encryption.encryption as encryptor
g_Mode = None

def Set_Program_Mode(mode):
	global g_Mode
	if (mode[1].lower()=='e'):
		g_Mode = True
	elif (mode[1].lower()=='d'):
		g_Mode = False
	else:
		g_Mode = None
if (len(sys.argv)>1):		
	if sys.argv[1]=="--help" or sys.argv[1]=="-h":
		print(__doc__)
		quit()

if (len(sys.argv)==3):
	if sys.argv[2][0] == '-':
		sys.argv[1],sys.argv[2] = sys.argv[2], sys.argv[1]

	Set_Program_Mode(sys.argv[1])

	if g_Mode == True:
		x = encryptor.functionPipeliner(encryptor.getEncFunctions(),sys.argv[2])
		print(x)
	elif g_Mode == False:
		x = encryptor.functionPipeliner(encryptor.getDecFunctions(),sys.argv[2])
		print(x)

	else:
		print("Unrecognized flag (are you calling \"python EncDec.py [-e or -d] [\"stringToProcess\"]  ?\"")
		print("quiting...")
		quit()
else:
	print("EncDec.py accepts exactly 2 arguments.")
	print("quiting...")
	quit()

