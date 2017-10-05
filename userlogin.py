list_workspace = ["mestworkspace", "codesplashworkspace","charletteworkspace"]
user_details = [{"email":"test@test.com", "password":"python3"}, {"email":"test@test.com","password":"mangoes"}]
User_Workspace = input ("Enter name of the workspace:  ")
email = ""
password = ""

#for workspace in list_workspace:
if User_Workspace in list_workspace:
	print("Please enter your login details:  ")
	email = input ("Please enter your email:  ")
	password = input ("Please enter your password:  ")

	for items in user_details:
		if email in items['email'] and password in items['password']:
			print("welcome")
		else:
			print("Incorrect Login details")
else:
	print("Sorry,you must be assigned to a workspace first")
