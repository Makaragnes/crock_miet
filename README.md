# crock_miet

В данном проекте реализовано 4 файла с  расширением .py, которые  решают задачи кейса.
1) bot.py - представляет собой реалиацию интеграции dialogflow c телеграм ботом , 
интеграция довольна простая. API telebot.
2) prep_data.py - представляет собой скрипт подготавливающий pdf данные  после того,
как их поместили в папку, (от конкретного подрядчика).
3) manage.py - представляет собой реализацю обработки данных, из таблицы, с  пожеланиями,э
по бонусам. Подсчитывается суммарное колличество сертификатов, от каждого подрядчика,
после чего формируются сообщения, динамическим способом. Сформированные сообщения отправляются подрядчикам.
4) send_serts.py формирует сообщения всем сотрудникам в зависимости от почты полученной в  таблице и от, 
заранее обработанного PDF файла. Отвечает за рассылку сертификатов.
