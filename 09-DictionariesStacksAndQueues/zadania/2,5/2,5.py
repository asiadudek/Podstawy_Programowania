#Napisz program, który łączy te listy i jednocześnie usuwa duplikaty.

contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = set(contacts_A | contacts_B)  #elementy z obu zbiorow bez powtorzen (suma)
print("Merged contacts:", merged_contacts)