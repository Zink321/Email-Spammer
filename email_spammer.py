import smtplib as root
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import art


#watermark
def menu():
	art.tprint("Email Spammer")
	print("\nFor Mail.ru :)")
menu()

#user data block (messages, recipient and etc)
def user_data():
	login = input('\nLogin: ')
	password = input('\nPassword: ')
	komu = input('\nTo: ')
	zagolovok = input('\nTopic: ')
	message = input('\nMessage: ')
	counter = input('\nHow many you want: ')

	return login, password, komu, zagolovok, message, counter

#gettig user data from return statement
login, password, komu, zagolovok, message, counter = user_data()

#function for mail sending with smtp server
def send_mail():

	msg = MIMEMultipart()

	msg[ 'Subject' ] = zagolovok
	msg[ 'From' ] = login

	msg.attach( MIMEText(message, 'plain'))

	server = root.SMTP_SSL("smtp.mail.ru", 465)
	server.login(login, password)
	server.sendmail(login, komu, msg.as_string() )

#spamming
def flood():
	i=0
	while i < int(counter):
		send_mail()
		i+=1
flood()
