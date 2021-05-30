#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


sender = 'ddvsfdvsdfvgdfsbv@gmail.com'
password = 'ping21!@#$%'
receiver = ''

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Certificate attached'



pdfname = ''

gmails2 = ["kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com",
           "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", 'bookmate1@gmail.ru',
           "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com"]

indexes=['ivi', 'moretv','iTunes','coursera','treoogrephia','esquire','Sinchronizaciabnbn','Miph','storytell','bookmate','Litres','okko','Amediateka']

#########my counters
ivi=0
moretv=0
itunes=0
coursera=0
treogrephia=0
esquire=0
sync=0
myph=0
storytell=0
bookmate=0
litress=0
okko=0
amediateka=0

"""Run administrative tasks."""
string = "rfff"
textfile='/home/riki/Documents/Hakatons/mietDjango/rep/data/account_entities.csv'
user_name=''
cert_name=''
with open('/home/riki/Documents/Hakatons/mietDjango/rep/data/account_entities.csv','r',encoding="utf8", errors='ignore') as file:
    reader = csv.reader(file)
    for row in reader:
      #  print(row)
        for i, f in enumerate(row):
            if i == 2:
                user_name=f
                print(user_name)
                body = '''Hello,
                        Here is your certficate
                        '''+'\ngoodluck BRO'
                message.attach(MIMEText(body, 'plain'))
            if i == 15:
                receiver = f
                receiver = "kirillbb.baranov2012@gmail.com"
                print('2')
            if i == 18:
                if f == 'ivi':
                    pdfname='ivi_'+str(ivi)+'.pdf'
                    pdfname = '/home/riki/Documents/Hakatons/mietDjango/rep/data/case.pdf'
                    ivi = ivi + 1
                    # open the file in bynary
                    binary_pdf = open(pdfname, 'rb')
                    print('pdf open')
                    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                    # payload = MIMEBase('application', 'pdf', Name=pdfname)
                    payload.set_payload((binary_pdf).read())

                    # enconding the binary into base64
                    encoders.encode_base64(payload)

                    # add header with pdf name
                    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                    message.attach(payload)

                    # use gmail with port
                    session = smtplib.SMTP('smtp.gmail.com', 587)

                    # enable security
                    session.starttls()

                    # login with mail_id and password
                    session.login(sender, password)

                    text = message.as_string()
                    session.sendmail(sender, receiver, text)
                    session.quit()
                    print('Mail Sent')
                    if f == 'moretv':
                        pdfname = 'moretv_' + str(moretv) + '.pdf'
                        moretv=moretv+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'iTunes':
                        pdfname = 'itunes_' + str(itunes) + '.pdf'
                        itunes=itunes+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'coursera':
                        pdfname = 'coursera_' + str(coursera) + '.pdf'
                        coursera=coursera+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'treogrephia':
                        pdfname = 'treogrephia_' + str(treogrephia) + '.pdf'
                        treogrephia=treogrephia+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'esquire':
                        pdfname = 'esquire_' + str(esquire) + '.pdf'
                        esquire=esquire+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'синхронизация':
                        pdfname = 'sync_' + str(sync) + '.pdf'
                        sync=sync+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'миф':
                        pdfname = 'myph_' + str(myph) + '.pdf'
                        myph=myph+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'storytell':
                        pdfname = 'storytell_' + str(storytell) + '.pdf'
                        storytell=storytell+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'bookmate':
                        pdfname = 'bookmate_' + str(bookmate) + '.pdf'
                        bookmate=bookmate+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'литрес':
                        pdfname = 'litress_' + str(litress) + '.pdf'
                        litress=litress+1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'okko':
                        pdfname = 'okko_' + str(okko) + '.pdf'
                        okko = okko + 1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')
                    if f == 'амедиатека':
                        pdfname = 'amediateka_' + str(amediateka) + '.pdf'
                        amediateka = amediateka + 1
                        # open the file in bynary
                        binary_pdf = open(pdfname, 'rb')

                        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                        # payload = MIMEBase('application', 'pdf', Name=pdfname)
                        payload.set_payload((binary_pdf).read())

                        # enconding the binary into base64
                        encoders.encode_base64(payload)

                        # add header with pdf name
                        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                        message.attach(payload)

                        # use gmail with port
                        session = smtplib.SMTP('smtp.gmail.com', 587)

                        # enable security
                        session.starttls()

                        # login with mail_id and password
                        session.login(sender, password)

                        text = message.as_string()
                        session.sendmail(sender, receiver, text)
                        session.quit()
                        print('Mail Sent')




