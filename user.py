import hashlib
class User:
	def __init__(self, name, username, email, password):
		self.__name = name
		self.__username = username
		self.__email = email
		self.__password = self.encrypt(password)
		self.__workspace = list()


	def get_email(self):
		return self.__email


	def get_password(self):
		return self.__password

	def user_str(self):
		return "{},{},{},{}".format(self.__name, self.__username, self.__email, self.__password)


	def __repr__(self):
		return '''
		name : {}
		username : {}
		email : {}
		'''.format(self.__name, self.__username, self.__email, self.__password)


	def encrypt(self, password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest()


	def add_workspace(self, wspace):
		self.__workspace.append(wspace)
		return "workspace added to userworspace"


	def get_worspace(self):
		for workspace in self.__workspace:
			print(workspace)


	def update_password(self, old_password, password):
		if self.__password == encrypt(old_password):
			self.__password = encrypt(password)
			return "password updated succesfuly"
		else:
			return "the password that you give is not correct"


	def remove_workspace(self, workspace):
		if workspace in self.__workspace:
			self.__workspace.remove(workspace)
			return "you have removed for {} successfully".format(workspace)
		else:
			return "unable to found the workspace that you have provided"


class UserGroup:
	def __init__(self, userlist = []):
		self.__users = userlist


	def load_users(self, userfile):
		with open(userfile) as file:
			for line in file.readlines():
				if line.strip():
					name, username, email, password = line.split(',')
					self.add_user(User(name, username, email, password))


	def add_user(self, user):
		if isinstance(user, User):
			self.__users.append(user)
			return "user added successfully "
		else:
			return "{} is not a user".format(user)


	def get_all_user(self):
		for user in self.__users:
			print(user)


	def save_user(self):
		with open('user.csv', 'w+') as file:
			for user in self.__users:
				file.write(str(user.user_str()) + "\r")

	def check_user(self, email, password):
		pwdhach = hashlib.sha256(password.encode('utf-8')).hexdigest()
		for user in self.__users:
			user_mail = user.get_email()
			user_pwd = user.get_password()
			if user_mail == email and user_pwd == password:
				return "correct"
		return "not correct"

# momo = User("momo", "moh", "momo@mail.fr", "123456")

# print(momo)