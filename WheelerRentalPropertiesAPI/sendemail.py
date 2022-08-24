import smtplib
from email.message import EmailMessage
import passwords
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def Contact_Alert(name, user_email, user_phone, subject, body):
    msg = EmailMessage()
    msg.set_content("Name: {}\nContact Email: {}\nContact Phone: {}\nSubject: {} \nMessage: {} \n".format(name,user_email, user_phone, subject, body))
    msg['to'] = 'wheelerrentalproperties@gmail.com'
    msg['subject'] = subject

    user = 'wheeler.notifications@gmail.com'
    msg['from'] = 'wheeler.notifications@gmail.com'
    password = env('wheeler_notifications')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


def Application_Alert():
    msg = EmailMessage()
    msg.set_content("You have a new Application!")
    subject = "New Application"
    msg['to'] = 'wheelerrentalproperties@gmail.com'
    msg['subject'] = subject

    user = 'wheeler.notifications@gmail.com'
    msg['from'] = 'wheeler.notifications@gmail.com'
    password = env('wheeler_notifications')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
