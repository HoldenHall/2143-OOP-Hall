"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: 
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.shift = 3
	"""
	Nice string representation of your class to help debug.
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.cipherText = message
			self.__decrypt()
	"""
	@ Name: getCipherText
	@ Description: returns cipherText
	@ Params:
				None
	"""
	def getCipherText(self):
		return self.cipherText

	"""
	@ Name: getPlainText
	@ Description: returns PlainText
	@ Params:
				None
	"""
	def getPlainText(self):
		return self.plainText
	"""
	@ Name: setShift
	@ Description: sets the value for shift
	@ Params:
				Shift{int}
	"""
	def setShift(self,shift):
		self.shift = shift
	"""
	@ Name: getShift
	@ Description: returns the value for shift
	@ Params:
				None
	"""
	def getShift(self):
		return self.shift
	"""
	@ Name: cleanData
	@ Description: determines if the letter in plain text is lowercase,
	if it is lowercase is is changed to it's uppercase equivalent. After
	this it calls the method below.
	@ Params:
			None
	"""
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			if ord(letter) == 32:
				continue
			if ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			else:
				self.cleanText += letter
		self.alphaNumeric_Data()

	"""
	@ Name: alphaNumeric_Data
	@ Description: Determines if any letters in cleanText are a symbol.
	It does this by comparing cleanText to a list and makes a new list without
	the symbols. Afterwards this list is changed into a string.
	@ Params:
			None
	"""
	def alphaNumeric_Data(self):
		AlphaNumeric = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		cleanList = []
		for letter in self.cleanText:
			if letter in AlphaNumeric:
				cleanList.append(letter) #adds the letters that are AlphaNumeric to a list
			else:
				continue
		self.cleanText = ''.join(cleanList) #this list is then changed into a string

	"""
	Encrypts plaintext not ciphertext
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
		    self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
		    
		
	
	"""
	Decrypts ciphertext not plaintext
	"""
	def __decrypt(self):
		l= []
		for letter in self.cipherText:
		    temp = self.cipherText
		    temp = chr((((ord(letter)-65) - self.shift) % 26)+65)
		    l+= temp
		self.plainText = ''.join(l)
		self.cleanText = ''.join(l)
             

"""
Only run this if we call this file directly:
"""
if __name__=='__main__':

    alice = ShiftCipher()
    alice.promptUserMessage()
    print(alice)


    bob = ShiftCipher()
    bob.setMessage(alice.getCipherText(),True)
    print(bob)
    bob.setMessage(alice.getPlainText(),False)