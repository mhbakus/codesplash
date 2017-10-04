#creating a channel object
class Channel:
	def __init__(self, name, purpose, privacy):
		self.__name = name
		self.__purpose = purpose
		self.__privacy = privacy

	#printing one chanel
	def __repr__(self):
		return '''
		chanel name : {}
		chanel purpose : {}
		chanel privacy : {} '''.format(self.__name, self.__purpose, self.__privacy)

	#returm the channel in one line
	def chanel_str(self):
		return "{},{},{}".format(self.__name, self.__purpose, self.__privacy)

	#get the name of the variable
	def get_name(self):
		return self.__name

#class of chanel list object
class Chanel_list:
	def __init__(self, chanels = []):
		self.__chanels = chanels

	#load all the channels from a csv file
	def load_chanels(self, chanelfile):
		with open(chanelfile) as file:
			for line in file.readlines():
				if line.strip():
					print(line)
					name, purpose, privacy = line.split(',')
					self.add_chanel(Channel(name, purpose, privacy))

	#adding an object chanel in the channel list
	def add_chanel(self, chanel):
		self.__chanels.append(chanel)
		print("chanel added successfully")

	#deleting an object channel
	def delete_chanel(self, chanel):
		if chanel in self.__chanels:
			self.__chanels.remove(chanel)
			print("chanel deleted successfully")
		else:
			print("the doesn't exist")

	#get all the channels
	def get_all_chanel(self):
		for chanel in self.__chanels:
			print(chanel)

	#checking the name of a channel in the list of channel
	def check_chanel_name(self, name):
		for chanel in self.__chanels:
			if name == chanel.get_name():
				return "chanel exist already"
		return "chanel is free"

	#save all the channels in a csv file
	def save_chanels(self):
		with open('chanels.csv', 'w+') as file:
			for chanel in self.__chanels:
				file.write(str(chanel.chanel_str()) + "\r")

#test 
# my_chanels = Chanel_list()
# my_chanels.load_chanels('chanels.csv')
# my_chanels.add_chanel(Channel('test', 'testing to create chanel', 'private'))
# my_chanels.save_chanels()
# print(my_chanels.check_chanel_name('test'))


