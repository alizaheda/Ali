import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#From and to whom E-Mali
fromaddress = 'dellali792@gmail.com'
toaddress = 'ali.zaheda.93@gmail.com'
#need to form the message how its look like
subject = 'My Baby'

msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = subject

body ='Come To Me Baby'
msg.attach(MIMEText(body,'plain'))


filename='dellali792.txt'
attachment  = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)


#need to give my info account
username = 'dellali792@gmail.com'
password = input("geben Sie Passwort ein")
#now need to actual E-Mail send
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddress, toaddress, text)
server.quit()