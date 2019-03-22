#!~/Git/Cloudoftwits/ python

#import pycrypto as pc
import pyfiglet
from Crypto.Cipher import AES
from Crypto import Random


#class APIcred:
"""
attributes of an API key:
name - to identify what type of key it is
input_data - to assign a plain text value to the key
encrypted key - the result of encrypting the key
where to store the key??? Strictly speaking, 
references to names in modules are attribute 
references: in the expression 

modname.funcname, modname 

is a module object and funcname is an attribute of it.

Try moving cred methods and assign as variables


"""
#CONSUMER_KEY = input('\nEnter your Consumer Key: ')



#	def __init__(self, plain_text):
#		self.plain_text = plain_text

		#self.cipher_text = cipher_text











		#self.input_data = iv + cipher.encrypt(b'input')




if __name__ == '__main__':
	
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



	def get_Filepath():
		FILEPATH = input("\nEnter the path where you would like "
				  "to save your encrypted credentials. \n"
				  "(OR Press Enter to save to ~/Documents/creds/cot.txt): ")
		if FILEPATH == '':
			FILEPATH = '~/Documents/creds/cot.txt'
		else:
			return FILEPATH 


	def get_Consumer_Key():
		while 1:
			CONSUMER_KEY = input('\nEnter your Consumer Key: ')
			if CONSUMER_KEY == "":
				print("You must enter the Consumer Key!")
			else:
				print ("Consumer Key: ", CONSUMER_KEY)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		return CONSUMER_KEY 
		
	
	def get_Consumer_Secret():
		while 1:
			CONSUMER_SECRET = input('\nEnter your Consumer Secret: ')
			if CONSUMER_SECRET == '':
				print("You must enter a Consumer Secret!")
			else:
				print ("Consumer Secret: ", CONSUMER_SECRET)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		return CONSUMER_SECRET


	def get_Access_Token():
		while 1:
			ACCESS_TOKEN = input('\nEnter your Access Token: ')
			if ACCESS_TOKEN == '':
				print('You must enter an Access Token!')
			else:
				print('Access Token: ', ACCESS_TOKEN)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		return ACCESS_TOKEN


	def get_Access_Secret():
		while 1:
			ACCESS_SECRET = input('\nEnter your Access Secret: ')
			if ACCESS_SECRET == '':
				print('You must enter an Access Secret!')
			else:
				print('Access Secret: ', ACCESS_SECRET)
				confirm = input('Is this correct? (Y / N): ')
				if confirm == 'Y' or confirm == 'y':
					break
		return ACCESS_SECRET


	def encrypted_input(pt_input):
		key = b'pt_input'
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CFB, iv)
		ct_output = iv + cipher.encrypt(b'pt_input')
		return ct_output


	print(banner())
	FILEPATH = get_Filepath()
	CONSUMER_KEY = get_Consumer_Key()
	CONSUMER_SECRET = get_Consumer_Secret()
	ACCESS_TOKEN = get_Access_Token()
	ACCESS_SECRET = get_Access_Secret()

	e_CONSUMER_KEY = encrypted_input(CONSUMER_KEY)
	print(e_CONSUMER_KEY)


	#CONSUMER_KEY = APIcred(conkey)


	#print(APIcred.plain_text)




	#cons = APIcred(APIcred.get_Consumer_Key)
	
	#APIcred.get_Consumer_Key()
	#cred = APIcred()

	#ckey = APIcred(get_Consumer_Key(), 1)
	#cred.get_Filepath()	
	
	#cred.get_Consumer_Secret()	
	#cred.get_Access_Token()
	#cred.get_Access_Secret()
	
	#print(cons.get_Consumer_Key)

	#APIcred.CONSUMER_KEY

	#print(wtf)
	#print(cred)



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
          
