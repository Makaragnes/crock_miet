#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import csv
import os
import smtplib
import ssl
import sys
from email.mime.text import MIMEText


def main():

    message="Добрый День! \n "
    gmails=['ivi1@gmail.ru', 'moretv1@gmail.ru','itunes1@gmail.ru','coursera1@gmail.ru','treoogrephia1@gmail.ru','esquire1@gmail.ru','sync1@gmail.ru','myph1@gmail.ru','storytell1@gmail.ru','bookmate1@gmail.ru','litress1@gmail.ru','okko1@gmail.ru','amediateka1@gmail.ru']

    #заглушка, так как 112  почт нет
    gmails2 = ["kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com",
              "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", 'bookmate1@gmail.ru',
              "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com", "kirillbb.baranov2012@gmail.com"]

    indexes=['ivi', 'moretv','iTunes','coursera','treoogrephia','esquire','Sinchronizaciabnbn','Miph','storytell','bookmate','Litres','okko','Amediateka']
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
    with open('/home/riki/Documents/Hakatons/mietDjango/rep/data/account_entities.csv','r',encoding="utf8", errors='ignore') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            for i, f in enumerate(row):
                if i == 18:
                    if f == 'ivi':
                        ivi=ivi+1
                    if f == 'moretv':
                        moretv=moretv+1
                    if f == 'iTunes':
                        itunes=itunes+1
                    if f == 'coursera':
                        coursera=coursera+1
                    if f == 'treogrephia':
                        treogrephia=treogrephia+1
                    if f == 'esquire':
                        esquire=esquire+1
                    if f == 'синхронизация':
                        sync=sync+1
                    if f == 'миф':
                        myph=myph+1
                    if f == 'storytell':
                        storytell=storytell+1
                    if f == 'bookmate':
                        bookmate=bookmate+1
                    if f == 'литрес':
                        litress=litress+1
                    if f == 'okko':
                        okko = okko + 1
                    if f == 'амедиатека':
                        amediateka = amediateka + 1
        #######addd sending  message  part for my dickens

        list_nums =[ivi,moretv,itunes,coursera,treogrephia,esquire,sync,myph,storytell,bookmate,litress,okko,amediateka]
           #  print(b)
        string += str(row)
       #     print("1")
        port = 465  # For SSL
         #   print("2")

        password = 'ping21!@#$%'
         #   print("6")
        i=0
        #####заглушка для той же цели
        my_mail="ddvsfdvsdfvgdfsbv@gmail.com"
        T_mail="kirillbb.baranov2012@gmail.com"
        while i<13:
            substr=indexes[i]
            number=list_nums[i]
            smtp_server = "smtp.gmail.com"
            #   print("3")
            sender_email = my_mail  # Enter your address
            #   print("4")
            receiver_email = gmails2[i] # Enter receiver address
            #   print("5")
            message_template = "Good afternoon! We have coorporative deal for "


            #  message=message_template.format(substr=indexes[i],numb='12')
            message=  message_template + substr+ ', in order '+str(number)
            print(message)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            i += 1

if __name__ == '__main__':
    main()
