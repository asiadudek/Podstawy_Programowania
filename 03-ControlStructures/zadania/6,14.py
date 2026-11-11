

facebook = False
twitter = True
instagram = True

print("Facebook: ",facebook)
print("Twitter: ",twitter)
print("Instagram: ",instagram)

if (facebook and instagram) or (facebook and twitter) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")