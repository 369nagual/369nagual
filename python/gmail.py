# # Python code to illustrate Sending mail from
# # your Gmail account
# import smtplib
# import test
#
# my_email = "vitkashubin@gmail.com"
# user_password = "Yustas2008/2020"
# app_password = "yzaeerlxhbbkldot"
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
#
# # start TLS for security
# s.starttls()
#
# # Authentication
# s.login(my_email, app_password)
#
# # message to be sent
# message = "TEST PYTHON TEST"
#
# # sending the mail
# s.sendmail(my_email, "vitkashubin@mail.ru", message)
#
# # terminating the session
# s.quit()
#
