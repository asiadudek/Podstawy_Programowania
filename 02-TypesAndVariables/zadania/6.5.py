###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input("Enter the phone number: ")
print(f"Phone number: {phone[0:3]}","-",f"{phone[3:6]}","-",f"{phone[-3:]}")