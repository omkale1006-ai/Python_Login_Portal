class LoginSystem:
  def __init__(self):
      # 👥 Multiple users stored as a dictionary
      self.users = {
          "omkale": "1006",
          "raj": "1234",
          "shruti": "abcd",
          "ravi": "pass123"
      }

  def validate_login(self, username, password):
      if username in self.users and self.users[username] == password:
          print(f"✅ Welcome, {username}! You have successfully logged in. 🙌")
      else:
          print("❌ Incorrect username or password. Please try again.")

# 🔁 Interface
print("🔐 Welcome to the Multi-User Login Portal!")
user = input("👤 Enter username: ")
pwd = input("🔑 Enter password: ")

login = LoginSystem()
login.validate_login(user, pwd)
