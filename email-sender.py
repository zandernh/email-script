import smtplib
from email.message import EmailMessage

email = EmailMessage()
email.set_content(
    '''
    
    [ Add your message here ]
    
    '''
)

# insert your email subject line as a string
email['Subject'] = ''
# insert your email here as a string
sender = email['From'] = ''
# add your email address below so Bcc functionality can take place
receiver = email['To'] = ''
# add the emails you want to message in this list, as strings, and separated by commas
recipient_list = []
email['Bcc'] = ','.join(recipient_list)


# You can google the smtp host details and port number you need to use for your particular email account -- I'll leave info here so you can see layout
with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
    server.ehlo()
    server.starttls()
    # insert your password below, or app password generated from your gmail account
    server.login(user=sender, password='')
    server.send_message(email)

# execute the script by running in PyCharm
# # or navigate to file location on terminal/command line and run --> python email-sender.py