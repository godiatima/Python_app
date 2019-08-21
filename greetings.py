users = ['Admin', 'Ruth', 'Rick', 'Morty', 'Peter']
users_admin = [ ]


for user in users_admin:
	if  user in  users:
		 print("Hello " + user.title() + ", Would you like to see a status report?")
	else:
		print("Hello "  + user.title() + ", thank you for logging in again.")
	   

