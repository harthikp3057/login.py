# login.py

def login(username, password):
    stored_username = "admin"
    stored_password = "1234"

    if username == stored_username and password == stored_password:
        return "Login successful!"
    else:
        return "Login failed!"
