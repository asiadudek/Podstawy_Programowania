#Napisz program, który sprawdza, czy użytkownik posiada wymagane uprawnienia.

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = required_permissions.issubset(user_permissions)   #sprawdza, czy A jest podzbiorem B (każdy element A jest w B)
print(has_permissions)  # Will return False because "execute" is missing.