
import emails

email = emails.read_from_file('email.txt')

print("Sender: ",emails.email_sender(email))
print("Recipient:", emails.email_recipient(email))
print("Subject:",emails.email_subject(email))
print("Body: ", emails.email_body(email))
