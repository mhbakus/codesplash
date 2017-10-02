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
	    elif answer.lower() == '2':
	        #call the code for creating a workspace
	    else:
	        exit = False
