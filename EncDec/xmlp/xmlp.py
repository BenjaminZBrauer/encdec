class xmlPreProcessor:
	tagsOpen = 0
	contents = None
	isReading, isGenerating = False, False
	currentInstruction = None
	forward, reverse = [], []
	flag = None

	def __removePreviouslyGeneratedCode(self):
		contents = []
		skipping = False
		for i in range(0, len(self.contents)):
			if not skipping:
					contents.append(self.contents[i])

			if self.__isInstruction(self.contents[i]):
				instruction = self.__isInstruction(self.contents[i]).lower()
				if instruction =='generate':
					skipping = True
				elif instruction == '/generate':
					skipping = False
					contents.append(self.contents[i])
				
		return contents

	def __reverse(self,x):
		bufferArray = []
		i = 0
		while (i<len(x)):
			bufferArray.insert(0, x[i])
			i += 1
		return bufferArray

	def __openTag(self):
		self.tagsOpen += 1

	def __closeTag(self):
		self.tagsOpen -= 1

	def __readLine(self,line):
		if self.__isInstruction(line):
			self.isReading = False
		else:
			line = line.replace(' ', '')
			line = line.replace('\t', '')
			line = line.replace('\n', '')
			if line!='':
				if line[0:3]=="def":
					if self.currentInstruction.lower()=="forward":
						self.forward.append(line[3:line.index('(')])
					elif self.currentInstruction.lower()=="reverse":
						self.reverse.append(line[3:line.index('(')])

	def __generateCode(self,file,index,positions):
		forward, reverse = [], []
		forward.append("\ndef getEncFunctions():\n\treturn [")
		reverse.append("\ndef getDecFunctions():\n\treturn [")
		
		def __append(array,func,count):
			array.append("lambda x: "+func+"(x)")
			array.append(", "+("\n\t\t" if (count+1)%3==0 else ""))
		
		if self.flag==None:
			if positions==None:
				self.reverse = self.__reverse(self.reverse)
				for i in range(len(self.forward)):
					__append(forward, self.forward[i], i)

				for i in range(len(self.reverse)):
					__append(reverse, self.reverse[i], i)
			else:
				reversedPositions = self.__reverse(positions)
				for i in range(len(positions)):
					__append(forward, self.forward[positions[i]], i)
					__append(reverse, self.reverse[reversedPositions[i]], i)
			#clean up
			forward.pop()
			reverse.pop()
			forward.append("]\n")
			reverse.append("]\n\n")
			forward = "".join(forward)
			reverse = "".join(reverse)
			generatedCode = "".join([forward,reverse])
		
		elif self.flag=='f':
			if positions==None:
				self.reverse = self.__reverse(self.reverse)
				for i in range(len(self.forward)):
					__append(forward, self.forward[i], i)
			else:
				for i in range(len(positions)):
					__append(forward, self.forward[positions[i]], i)
			#clean up
			forward.pop()
			forward.append("]\n\n")
			forward = "".join(forward)
			generatedCode = forward
		elif self.flag=='r':
			if positions==None:
				self.reverse = self.__reverse(self.reverse)
				for i in range(len(self.reverse)):
					__append(reverse, self.reverse[i], i)
			else:
				reversedPositions = self.__reverse(positions)
				for i in range(len(positions)):
					__append(reverse, self.reverse[reversedPositions[i]], i)
			#clean up
			reverse.pop()
			reverse.append("]\n\n")
			reverse = "".join(reverse)
			generatedCode = reverse
		else:
			raise SyntaxError(" -- Unrecognised flag used (options are 'f' or 'r') -- ")

		
		#add generated text
		self.contents.insert(index, generatedCode)
		f = open(file,"w")
		f.write("".join(self.contents))
		f.close()


	def __isInstruction(self,line):
		instruction = []
		if line[0:2] == "#<":
			for c in line:
				if c=='<':
					self.__openTag();
				elif  c=='>':
					self.__closeTag();
				if self.tagsOpen>0 and (c!='<' and c!='>'):
					instruction.append(c)

		if self.tagsOpen>0:
			raise SyntaxError("(an) XML tag(s) is/are open.")
			quit()
		return "".join(instruction) if instruction else False

#MAIN
	def parseFile(self,file,positions = None, flag = None):
		instructions = []
		counter = 0
		self.contents = (open(file, "r")).readlines()
		self.flag = flag

		for line in self.contents:
			instruction = []
			counter += 1
			if self.isReading:
				self.__readLine(line)
			elif self.isGenerating:
				counter -= 1
				self.contents = self.__removePreviouslyGeneratedCode()
				self.__generateCode(file,counter,positions)
				break
			else:
				instruction = self.__isInstruction(line)
				if instruction:
					if instruction.lower()=="ignore":
						continue
					if instruction[0]!='/':
						if instruction.lower()!="generate":
							if (flag=='f' and instruction.lower()=="forward") or (flag=='r' and instruction.lower()=="reverse") or (flag==None):
								self.isReading = True
								self.currentInstruction = instruction
						else:
							if self.isReading:
								raise  SyntaxError("generating within a read-block is not allowed")
							else:
								self.isGenerating = True
