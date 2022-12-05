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


#smtp выбор
def smtpchoose():
	print('Choose smtp server (1-3)')
	print('\n1. smtp.gmail.com (didn`t work) \n2. smtp.yandex.ru \n3. smtp.mail.ru')
	a = int(input('Your choose: '))

	match a:
		case 1:
			url = 'smtp.gmail.com'
		case 2:
			url = 'smtp.yandex.ru'
		case 3:
			url = 'smtp.mail.ru'

	if (a > 3 or a < 1):
		print('Invalid choose \n')

	return url

#получаем ссылку smtp сервера
url = smtpchoose()



#блок данных для входа и сообщения
def user_data():
	login = input('\nLogin: ')
	password = input('\nPassword: ')
	komu = input('\nTo: ')
	zagolovok = input('\nTopic: ')
	message = input('\nMessage: ')

	return login, password, komu, zagolovok, message

#получаем данные пользователя
login, password, komu, zagolovok, message = user_data()



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
