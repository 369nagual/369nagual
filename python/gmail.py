# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
from database import data
from passwords import *

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(my_email, app_password)

# message to be sent
message = data
# sending the mail
# TO-DO: sending the empty message
s.sendmail(my_email, receivers_email, str(message))

# terminating the session
s.quit()
