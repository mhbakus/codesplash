import datetime
import smtplib
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import __init__

class Message:
	def __init__(self, user_id, messages = [], users = []):
		self.__user_id = user_id
		self.__messages = messages
		self.__users = users

	def send_message(self, from_id, targert_id, message_text):
		#check that the user exit
		find = False
		for user in self.__users:
			if targert_id == user.id:
				find = True
		if not find:
			return "user doesn't exist "
		else:
			time = datetime.datetime.now()
			message = [from_id, targert_id, message_text, time]
			self.__messages.append(message)
			return "message sent succesfully"


	def get_message(self, user_id):
		messages = list()
		for message in self.__messages:
			if message[1] == user_id:
				print(message)


class Email:
	def __init__(self, client, port):
		self.__client = client
		self.__port = port
		self.__conected = False


	def connect(self, login, passwd):
		self.__server = smtplib.SMTP(self.__client, self.__port)
		self.__server.starttls()
		self.__server.login(login, passwd)
		self.__conected = True

	def send(self, from_add, to_add, msg_subject, content):
		if self.__conected:
			fromadress = from_add
			msg = MIMEMultipart()
			msg['From'] = fromadress
			msg['To'] = to_add
			msg['Subject'] = msg_subject
			body = content
			msg.attach(MIMEText(body, 'plain'))
			text = msg.as_string()
			self.__server.sendmail(fromadress, email, text)

		else:
			return "you should be connected"


# Mymail = Email('smtp.gmail.com', 587)
# Mymail.connect('', '')
