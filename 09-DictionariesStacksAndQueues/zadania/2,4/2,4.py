#Ukończ program wyświetlający otrzymane adresy e-mail, które znajdują się na liście spamu.

emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = spam_list & emails_received # Intersection, wyswietlamy tylko to co jest zarowno w zbiorze 1 jak i w drugim
print("Spam emails:", spam_emails)