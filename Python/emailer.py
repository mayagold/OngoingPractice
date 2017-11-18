emails = []

try:
    email_file = open('emails.txt', 'r')
except FileNotFoundError as err: 
    print(err)

for line in email_file:
    emails.append(line.strip())

print(emails)
