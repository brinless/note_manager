import datetime

username = input('Введите имя пользователя: ')
title = input('Заголовок заметки: ')
content = input('Текст заметки: ')
status = "выполняется"
created_date = datetime.datetime.now()
issue_date = input('Укажите дату выполнения: ')
print(created_date.date())