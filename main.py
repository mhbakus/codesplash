from messages import *
import user

mail_client = Email('smtp.gmail.com', 587)
mail_client.connect('mhbakus@gmail.com', 'mh41170788')

def connections():
	reponse = input("Please enter your email address : ")
	subject = "welcome on slack"
	content = '''
	welcome on Slack
	your security code is 123-456
	enter this code in the application to verify your email

	'''
	mail_client.send('mail@codesplashslack.com', reponse, subject, content)

if __name__ == "__main__":
	#print a message for select a action create workspace or login
	
	exit = False
	while not exit:
	    answer = input('''
	       __  __ _____ _   _ _   _ 
	      |  \/  | ____| \ | | | | |
	      | |\/| |  _| |  \| | | | |
	      | |  | | |___| |\  | |_| |
	      |_|  |_|_____|_| \_|\___/ 
	      

	      1 .  login to your workspace

	      2 .  create a workspace

	      3 .  exit

	      ''')

	    if answer.lower() == '1':
	        #call the code for login
	        pass
	    elif answer.lower() == '2':
	    	pass
	        #call the code for creating a workspace
	    else:
	    	pass