import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
#Next, log in to the server
server.login("nibinshatest@gmail.com", "1234!@#$")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("nibinshatest@gmail.com", "nibinshanibi@gmail.com", msg)
