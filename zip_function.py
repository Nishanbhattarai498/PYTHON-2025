usernames=["nishan","bro","mister"]
passwords=("password","abc123","hey")
login_dates=["1/1/2022","1/2/2023","1/2/300"]



users=list(zip(usernames,passwords,login_dates))

for i in users:
    print(i)

print(type(users))