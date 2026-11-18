
import emails
import os #modul ktory sluzy do pracy z folderami, sciezkami

# Ustawiamy folder roboczy na folder, w którym leży skrypt.
# __file__ = ścieżka skryptu, abspath = pełna ścieżka, dirname = sam folder (bez nazwy pliku),
# chdir = ustawia ten folder jako roboczy. Dzięki temu program zawsze znajdzie clothing.csv.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


email = emails.read_from_file('email.txt')

print("Sender: ",emails.email_sender(email))
print("Recipient:", emails.email_recipient(email))
print("Subject:",emails.email_subject(email))
print("Body: ", emails.email_body(email))
