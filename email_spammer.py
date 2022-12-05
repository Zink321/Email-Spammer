import smtplib as root
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart



#меню (бета)
def menu():
	print("░█▀▀▀ ░█▀▄▀█ ─█▀▀█ ▀█▀ ░█─── 　 ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█▀▄▀█ ░█▀▄▀█ ░█▀▀▀ ░█▀▀█ ")
	print("░█▀▀▀ ░█░█░█ ░█▄▄█ ░█─ ░█─── 　 ─▀▀▀▄▄ ░█▄▄█ ░█▄▄█ ░█░█░█ ░█░█░█ ░█▀▀▀ ░█▄▄▀ ")
	print("░█▄▄▄ ░█──░█ ░█─░█ ▄█▄ ░█▄▄█ 　 ░█▄▄▄█ ░█─── ░█─░█ ░█──░█ ░█──░█ ░█▄▄▄ ░█─░█ ")
	print('                                                                      By Zink')
	print('')
menu()


#Выбор smtp для отправки
print('Choose smtp server (1-3)')
print('\n1. smtp.gmail.com (didn`t work) \n2. smtp.yandex.ru \n3. smtp.mail.ru')
a = int(input('Your choose: '))


#Проверка на долбаеба (говнокод)
if (a == 1):
	url = 'smtp.gmail.com'
elif (a == 2):
	url = 'smtp.yandex.ru'
elif (a == 3):
	url = 'smtp.mail.ru'
elif (a > 1 or a > 3):
	print('Invalid choose')



#блок данных для входа и сообщения
login = input('\nLogin: ')
password = input('\nPassword: ')
komu = input('\nTo: ')
zagolovok = input('\nTopic: ')
message = input('\nMessage: ')


#функция хуюнкция для отправки
def send_mail():

	msg = MIMEMultipart()

	msg[ 'Subject' ] = zagolovok
	msg[ 'From' ] = login
	body = message
	msg.attach( MIMEText(body, 'plain'))

	server = root.SMTP_SSL(url, 465)
	server.login(login, password)
	server.sendmail(login, komu, msg.as_string() )
send_mail()
