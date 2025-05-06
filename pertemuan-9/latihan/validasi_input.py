class User:
    def __init__(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_username(self, username_baru):
        if len(username_baru) >= 5:
            self.__username = username_baru
        else:
            print("Username minimal 5 karakter!")

user = User("admin123")
user.set_username("user")  # Output: Username minimal 5 karakter!
print(user.get_username())  # Output: admin123