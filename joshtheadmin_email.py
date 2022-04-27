# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

def ipupdate_notification(envir, new_ip, send_to, notes):
    message = Mail(
        from_email='noreply@joshtheadmin.com',
        to_emails=send_to,
        subject='Your IP address has updated',
        html_content='The IP address for '+ envir + ' has been updated to ' + new_ip + " Notes: " + notes)
    try:
        sg = SendGridAPIClient(os.environ.get('YOUR_SENDGRID_APIKEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)