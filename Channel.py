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

	def chanel_str(self):
		return "{},{},{}".format(self.__name, self.__purpose, self.__privacy)

	def get_name(self):
		return self.__name

class Chanel_list:
	def __init__(self, chanels = []):
		self.__chanels = chanels

	def load_chanels(self, chanelfile):
		with open(chanelfile) as file:
			for line in file.readlines():
				if line.strip():
					print(line)
					name, purpose, privacy = line.split(',')
					self.add_chanel(Channel(name, purpose, privacy))

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

	def check_chanel_name(self, name):
		for chanel in self.__chanels:
			if name == chanel.get_name():
				return "chanel exist already"
		return "chanel is free"

	def save_chanels(self):
		with open('chanels.csv', 'w+') as file:
			for chanel in self.__chanels:
				file.write(str(chanel.chanel_str()) + "\r")


my_chanels = Chanel_list()
my_chanels.load_chanels('chanels.csv')
my_chanels.add_chanel(Channel('test', 'testing to create chanel', 'private'))
my_chanels.save_chanels()
print(my_chanels.check_chanel_name('test'))


