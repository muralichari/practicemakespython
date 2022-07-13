users = {}

with open('password.txt') as f:
	for line in f:
		if not line.startswith('#'):
			user_info  = line.split(":")
			users[user_info[0]] = user_info[2]


for username in sorted(users):
	print(f'{username} : {users[username]}')