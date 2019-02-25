#!~/Git/Cloudoftwits/ python

#import pycrypto as pc
import pyfiglet
from Crypto.Cipher import AES
from Crypto import Random


class APIcred:
	"""
	attributes of an API key:
	name - to identify what type of key it is
	input_data - to assign a plain text value to the key
	encrypted key - the result of encrypting the key
	where to store the key???
	"""

	def __init__(self):
		self.CONSUMER_KEY = ''
		self.CONSUMER_SECRET = ''
		self.ACCESS_TOKEN = ''
		self.ACCESS_SECRET = ''

	def get_Consumer_Key(self):
		while 1:
			CONSUMER_KEY = input('\nEnter your Consumer Key: ')
			if CONSUMER_KEY == "":
				print("You must enter the Consumer Key!")
			else:
				print ("Consumer Key: ", CONSUMER_KEY)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		self.CONSUMER_KEY = CONSUMER_KEY

	def get_Consumer_Secret(self):
		while 1:
			CONSUMER_SECRET = input('\nEnter your Consumer Secret: ')
			if CONSUMER_SECRET == '':
				print("You must enter a Consumer Secret!")
			else:
				print ("Consumer Secret: ", CONSUMER_SECRET)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		self.CONSUMER_SECRET = CONSUMER_SECRET

	def get_Access_Token(self):
		while 1:
			ACCESS_TOKEN = input('\nEnter your Access Token: ')
			if ACCESS_TOKEN == '':
				print('You must enter an Access Token!')
			else:
				print('Access Token: ', ACCESS_TOKEN)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		self.ACCESS_TOKEN = ACCESS_TOKEN

	def get_Access_Secret(self):
		while 1:
			ACCESS_SECRET = input('\nEnter your Access Secret: ')
			if ACCESS_SECRET == '':
				print('You must enter an Access Secret!')
			else:
				print('Access Secret: ', ACCESS_SECRET)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		self.ACCESS_SECRET = ACCESS_SECRET

	def encrypt_input(self, input_data):
		padding = '{'
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CFB, iv)
		self.input_data = iv + cipher.encrypt(b'input')
		return input_data

	def get_Filepath(self):
		FILEPATH = input("\nEnter the path where you would like "
				  "to save your encrypted credentials. \n"
				  "(OR Press Enter to save to ~/Documents/creds/cot.txt): ")
		if FILEPATH == '':
			self.FILEPATH = '~/Documents/creds/cot.txt'
		else:
			self.FILEPATH = FILEPATH 




if __name__ == '__main__':
	
#	def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, input):
#			padding = '{'
#	iv = Random.new().read(AES.block_size)
#	cipher = AES.new(key, AES.MODE_CFB, iv)
#	self.input = iv + cipher.encrypt(b'input')

	def banner():
		print("")
		print(pyfiglet.figlet_format("                                @   ", font = "octal"))
		print(pyfiglet.figlet_format("                            @     @   ", font = "octal"))
		print(pyfiglet.figlet_format("                    @                     @   ", font = "octal"))
		print(pyfiglet.figlet_format("@     Loud Mouth Soup    @", font = "octal"))
		print(pyfiglet.figlet_format("@     Loud Mouth Soup    @", font = "octal"))
		result = pyfiglet.figlet_format("@  Cloud of Twits    @", font = "tombstone")
		print(result)
		print(pyfiglet.figlet_format("@     Loud Mouth Soup    @", font = "octal"))
		print(pyfiglet.figlet_format("@     Loud Mouth Soup    @", font = "octal"))
		print("by")
		print(pyfiglet.figlet_format("@ Loud Mouth Soup @", font = "cybersmall"))
		print("\nWelcome to Cloud of Twits \n\n"
		  "In this configuration file you will setup and encrypt your API keys.\n"
		  "You must have the folling modules installed to run this program:\n"
		  "   \n"
		  "	pip3 install pycrypto os tweepy numpy pandas matplotlib textblob \n\n"
		  "You will need to configure your API keys from twitter for this program \n"
		  "to run.  (See readme for instructions on how to set up a Twitter API) \n"
		  "\n")
		print("Please enter your Twitter API keys here, your keys will be encrpyted \n"
		  "and saved to a file. \n\n")


	print(banner())
	cred = APIcred()
	cred.get_Filepath()	
	cred.get_Consumer_Key()
	cred.get_Consumer_Secret()	
	cred.get_Access_Token()
	cred.get_Access_Secret()
	


#	CONSUMER_KEY_input = input('Enter your Consumer Key: ')
#	CONSUMER_SECRET_input = input('Enter your Consumer Secret: ')
#	ACCESS_TOKEN_input = input('Enter your Access Token: ')
#	ACCESS_SECRET_input = input('Enter your Access Secret: ')



#class EncryptKey(APIkey):
#
#	def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, input):
#		padding = '{'
#		iv = Random.new().read(AES.block_size)
#		cipher = AES.new(key, AES.MODE_CFB, iv)
#		self.input = iv + cipher.encrypt(b'input')
	



	#	print("Enter your CONSUMER KEY: ")
	#	CONSUMER_KEY = str(input())

	#	print("Enter your CONSUMER SECRET: ")
	#	CONSUMER_SECRET = str(input())

	#	print("Enter your ACCESS TOKEN: ")
	#	ACCESS_TOKEN = str(input())

	#	print("Enter your ACCESS SECRET: ")
	#	ACCESS_SECRET = str(input())




# roman spreads to 3 lines
# octal is cool.. place underneath


#print("ooooo                                    .o8  ooo        ooooo                           .   oooo         .oooooo..o")                                  
#print("`888'                                   `888  `88.       .888'                         .o8   `888        d8P'    `Y8")                                  
#print("`888          .ooooo.  oooo  oooo   .oooo888   888b     d'888   .ooooo.  oooo  oooo  .o888oo  888 .oo.   Y88bo.       .ooooo.  oooo  oooo  oo.ooooo.")  
#print("`888         d88' `88b `888  `888  d88' `888   8 Y88. .P  888  d88' `88b `888  `888    888    888P"Y88b   `"Y8888o.  d88' `88b `888  `888   888' `88b") 
#print(" 888         888   888  888   888  888   888   8  `888'   888  888   888  888   888    888    888   888       `"Y88b 888   888  888   888   888   888") 
#print(" 888       o 888   888  888   888  888   888   8    Y     888  888   888  888   888    888 .  888   888  oo     .d8P 888   888  888   888   888   888")
#print("o888ooooood8 `Y8bod8P'  `V88V"V8P' `Y8bod88P" o8o        o888o `Y8bod8P'  `V88V"V8P'   "888" o888o o888o 8""88888P'  `Y8bod8P'  `V88V"V8P'  888bod8P'") 
#print("                                                                                                                                            888")       
#print("                                                                                                                                           o888o ")    
          
