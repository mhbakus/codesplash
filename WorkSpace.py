import csv, os, random, smtplib

class Verification:
	def __init__(self):
		self.random_key = ''

	#used to generate random numbers which are returned with this function test
	def generate_random_numbers(self):
		s=list(range(6))
		random.shuffle(s) # << shuffle before print or assignment
		self.random_key = "".join(str(x) for x in s)
		return self.random_key

	#used to send the random number to the email of the account user
	def send_notification(self, receiver_email):
		gmail_mail_config = "elkana@meltwater.org"
		gmail_password_config = "elykips+254"
		content = self.random_key

		#----------- SMTP CONFIGS -----------# 
		mail = smtplib.SMTP('smtp.gmail.com',587)
		mail.ehlo()
		mail.starttls()
		mail.login(gmail_mail_config, gmail_password_config)
		mail.sendmail(gmail_mail_config, receiver_email, content)
		mail.close()
		print("Succesfully sent, Please check email for confirmation code")

	#used to verify the code entered to make sure it is same as the one sent
	def verify_code(self, code_received):
		if code_received == self.random_key:
			return True
		else:
			return False

class WorkSpaceAdmin:

	def __init__(self, admins_dict = {}, admin_list = []):
		self.admins_dict = admins_dict
		self.admin_list = admin_list

	#use to create the admin of the workspace
	def create_admin_dict(self, fullname, username, password, email):
		self.admins_dict['fullname'] = fullname
		self.admins_dict['username'] = username
		self.admins_dict['password'] = password
		self.admins_dict['email'] = email
		self.admin_list.append(self.admins_dict)





class WorkSpace(WorkSpaceAdmin):
	work_list = []
	work_dict = {}
	def __init__(self, name = '', list_channel = ["general", "random"]):
		super().__init__(admins_dict = {}, admin_list = [])
		self.name = name
		# self.url = self.name + "slack.com"
		self.list_channel = list_channel
		self.team_purpose = ''
		self.size_of_team = 0
		self.user_role = ''

	#used to write to the csv the content of the class that was created
	def create_work_space(self, name, team_purpose, size_of_team, email):
		self.url = name + ".slack.com"
		has_header = False
		with open('workspace.csv', 'r') as f:
			for line in f:
				if len(line) >= 1:
					has_header = True
					break
				else:
					pass


		with open('workspace.csv', 'a') as file:
			messages = csv.DictWriter(file, fieldnames = ["WorkSpaceName", "TeamSize", "Email", "Purpose", "Url"])
			if not has_header:
				messages.writeheader()
			messages.writerow({'WorkSpaceName': name, 'TeamSize': size_of_team, 'Email': email, 'Purpose': team_purpose, 'Url': self.url })
			#WorkSpace.work_list.append(WorkSpace.work_dict)

	def get_workspaces(self):
		return WorkSpace.work_list
	

if __name__ == "__main__":
	verification = Verification()#create an instance of the verification
	work_admin = WorkSpaceAdmin()#cerate an instance of the work_admin
	workspace = WorkSpace()#create an instance of the workspace

	email = input("Enter Email: ")
	verification.generate_random_numbers()
	verification.send_notification(email)

	confirmation_token = input("Enter Code: ")
	result = verification.verify_code(confirmation_token)

	if result == True:
		print("Good Guy, Let's setup your workspace")

		admin_full_name = input("Enter Full Name: ")
		admin_name = input("Enter Display Name: ")
		admin_pswrd = input("Type Your Password: ")
		
		work_admin.create_admin_dict(admin_full_name, admin_name, admin_pswrd, email)
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

		#print(workspace.get_workspaces())
	else:
		print("gerarahia mehn")

