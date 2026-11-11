###
# Password validator
# New password is at least 12 characters long
#

new_password = input("Enter your password: ")

if len(new_password) >= 12:
    print("Password has correct length")
else:
    print("Password is too short (min. 12 chars)")