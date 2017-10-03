import smtplib, random, csv

class Verification:
	def __init__(self):
		self.random_key = ''

	def generate_random_numbers(self):
		s=list(range(6))
		random.shuffle(s) # << shuffle before print or assignment
		self.random_key = "".join(str(x) for x in s)
		return self.random_key


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

	def verify_code(self, code_received):
		if code_received == self.random_key:
			return True
		else:
			return False

class WorkSpaceAdmin:

	def __init__(self, admins_dict = {}, admin_list = []):
		self.admins_dict = admins_dict
		self.admin_list = admin_list

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

	def create_work_space(self, name, team_purpose, size_of_team, email):
		WorkSpace.work_dict['name'] = name
		# if self.team_purpose == '1':
		# 	WorkSpace.work_dict['team_purpose'] = 'shool'
		# elif self.team_purpose == '2':
		# 	WorkSpace.work_dict['team_purpose'] = 'work'
		# elif self.team_purpose == '3':
		# 	WorkSpace.work_dict['team_purpose'] = 'shared interest'
		# elif self.team_purpose == '4':
		# 	WorkSpace.work_dict['team_purpose'] = 'others'
		WorkSpace.work_dict['size_of_team'] = size_of_team
		WorkSpace.work_dict['admin_mail'] = email
		WorkSpace.work_dict['team_purpose'] = team_purpose
		WorkSpace.work_dict['url'] = name + ".slack.com"
		# f = open('workspace.csv','w')
		# f.write(str(WorkSpace.work_dict)) 
		# f.close()

		fieldnames = ["WorkSpaceName", "TeamSize", "Email", "Purpose", "Url"]
		writer = csv.DictWriter(newfile, fieldnames=fieldnames)
		for row in WorkSpace.work_dict:
			writer.writerow(row)


		WorkSpace.work_list.append(WorkSpace.work_dict)

	def get_workspaces(self):
		return WorkSpace.work_list
	

if __name__ == "__main__":
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

		print(workspace.get_workspaces())
	else:
		print("gerarahia mehn")

