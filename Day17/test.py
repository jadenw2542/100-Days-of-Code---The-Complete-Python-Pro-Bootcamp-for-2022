class User:
    def __init__(self, user_id, username):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 1

    def follow(self, user):
        user.followers += 1
        user.following += 1

user_1 = User("001", "Jaden")
user_2 = User("002", "Mum")
print(user_1.username)
user_1.follow(user_2)
print(user_2.followers)

