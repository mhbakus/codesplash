# class Channel(object):
# 	purpose = {1 : "operation", 2 : "tech", 3 : "marketing"}
	
# 	def __init__(self, name, private = False, purpose, member):
# 		self.name = name
# 		self.privacy = privacy
# 		self.purpose = purpose
# 		self.member = member 

# 	def get_channel_name():
# 		name = input("Enter Channel name: ")

# 	def get_purpose():
# 		for k, v in purpose.items():
# 			print()
		
# Check if login is true
# class Channel:
# 	def __init__(self, name):
# 		self.name = name
		

# 	def create_channel(self, name, privacy, purpose):
# 		self.name = input("Enter Channel name: ")
		
# 	Channel =[]


# 		for user in workspace:
# 			if new_user == user and login == True:

class Channel:
	def __init__(self, name, purpose, privacy):
		self.__name = name
		self.__purpose = purpose
		self.__privacy = privacy

	def __repr__(self):
		return '''
		chanel name : {}
		chanel purpose : {}
		chanel privacy : {} '''.format(self.__name, self.__purpose, self.__privacy)

class Chanel_list:
	def __init__(self, chanels = []):
		self.__chanels = chanels


	def add_chanel(self, chanel):
		self.__chanels.append(chanel)
		print("chanel added successfully")


	def delete_chanel(self, chanel):
		if chanel in self.__chanels:
			self.__chanels.remove(chanel)
			print("chanel deleted successfully")
		else:
			print("the doesn't exist")


	def get_all_chanel(self):
		for chanel in self.__chanels:
			print(chanel)

my_chanels = Chanel_list()

my_chanels.add_chanel(Channel("beta", "talk about the beta purpose", "private"))
my_chanels.add_chanel(Channel("test", "talk about the test purpose", "private"))
my_chanels.add_chanel(Channel("launch", "talk about the launch purpose", "private"))
my_chanels.get_all_chanel()


