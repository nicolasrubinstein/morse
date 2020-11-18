from dict import DICT, INV_DICT 

class MorseMessage:
	def __init__(self, string):
		self.string = string

	def decript(self):
		splitted_message = self.string.split(" ")
		for index, letter in enumerate(splitted_message):
			try:
				if letter == "/":
					splitted_message[index] = " "
				else:
					splitted_message[index] = INV_DICT[letter]
			except KeyError:
				return False
		result = ""
		for letter in splitted_message:
			result += letter 
		return result


	def encript(self):
		splitted_message = list(self.string.upper())

		for index, letter in enumerate(splitted_message):
			try:
				if letter == " ":
					splitted_message[index] = "/"
				else:
					splitted_message[index] = DICT[letter]
			except KeyError:
				return False 

		result = ""
		for letter in splitted_message:
			result += letter + " "
		
		return result

	def get_status(self):
		
		if self.encript():
			return "Decripted"
		elif self.decript():
			return "Encripted"
		else:
			return "No-morse"
	

p1 = MorseMessage("Nicolas Rubinstein")

print(p1.encript())