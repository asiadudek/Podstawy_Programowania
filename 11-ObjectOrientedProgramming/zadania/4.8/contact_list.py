from contact import Contact

class ContactList:
    def __init__(self):
        self.contacts = [] #pusta lista na kontakty

    def add_contact(self, name, email, telephone):
        contact = Contact(name, email, telephone) #zmienna lokalna
        self.contacts.append(contact) #dodajemy nasz kontakt do listy

    def show_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}  {contact.email}  {contact.telephone}")