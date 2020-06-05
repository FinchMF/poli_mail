import os
import smtplib
from email.message import EmailMessage

# setting up inputs for necessary information
email_username = input('Email: ')
email_password = input('Email Password: ')
name = input('What is your name? ')
borough = input('What borough do you live in? ')
address = input('What is your address? ')
phone = input('What is your phone number? ')

# grabbing the emails of council memebers
contacts = open('NYC/council_members_emails.txt', 'r')
council_members = contacts.read()
contacts.close()

# filling out the form
template = open('NYC/defund_NYPD.txt')
contents = template.readlines()
template.close()

contents[2] =  f'My name is {name} and I am a resident of {borough}. Last April, NYC Mayor Bill De Blasio proposed major budget cuts for the Fiscal Year 2021, especially to education and youth programs, while refusing to slash the NYPD budget by any significant margin.\n'
contents[-1] = f'Thank you, {name}, {address}, {email_username}, {phone}'

form_filled = ''.join(contents)

filled_template = open(f'NYC/defund_NYPD_{name}.txt', 'w')
filled_template.write(form_filled)
filled_template.close()

body = open(f'NYC/defund_NYPD_{name}.txt', 'r')
body = body.read()


msg = EmailMessage()
msg['Subject'] = 'Commit to Vote No on the Mayor\'s Budget / Defund the NYPD'
msg['From'] = email_username
msg['To'] = council_members
msg.set_content(body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_username, email_password)
    smtp.send_message(msg)


print('You have successfully emailed all NYC Council Members a request to commit towards defunding NYPD')