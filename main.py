from messages import *
from user import *
from workspace import *
import getpass

mail_client = Email('smtp.gmail.com', 587)
mail_client.connect('elkana@meltwater.org', 'elykips+254')

userlist = UserGroup()
userlist.load_users('user.csv')

def singup():
	verification = Verification()
	work_admin = WorkSpaceAdmin()
	workspace = WorkSpace()

	email = input("Enter Email: ")
	verification.generate_random_numbers()
	verification.send_notification(email)

	confirmation_token = input("Enter Code: ")
	result = verification.verify_code(confirmation_token)

	if result == True:
		print("Good Guy, Let's setup your workspace")

		admin_full_name = input("Enter Full Name: ")
		admin_name = input("Enter Display Name: ")
		admin_pswrd = getpass.getpass('Password:')
		
		work_admin.create_admin_dict(admin_full_name, admin_name, admin_pswrd, email)

		userlist.add_user(User(admin_full_name, admin_name, email, admin_pswrd))
		userlist.save_user()

		purpose = input(" 1 for school\n 2 for work\n 3 for shared interest group\n 4 for others\n Answer:  ")
		
		if purpose == '1':
			purpose = "school"
		elif purpose == '2':
			purpose = 'work'
		elif purpose == '3':
			purpose = 'shared interest'
		elif purpose == '4':
			purpose = 'others'


		size_of_team = input(" Enter Size of team: ")
		name_of_coy = input(" Company Name: ")
		workspace.create_work_space(name_of_coy, purpose, size_of_team, email)

		print(workspace.get_workspaces())
	else:
		print("gerarahia mehn")

def connections():
	pass
	email = input("Please enter your email address : ")
	password = getpass.getpass('Password: ')

	if userlist.check_user(email, password):
		print("great you're connected")
	else:
		print("email or password incorect")


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
	        connections()
	    elif answer.lower() == '2':
	    	singup()
	    	pass
	        #call the code for creating a workspace
	    else:
	    	pass