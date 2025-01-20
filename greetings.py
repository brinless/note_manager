from datetime import datetime
#import datetime

username = input('Введите имя пользователя: ')
title = input('Заголовок заметки: ')
content = input('Текст заметки: ')
status = "выполняется"
created_date = datetime.now()
issue_date = input('Укажите дату выполнения в формате: dd-mm-yyyy: ')
issue_date = datetime.strptime(issue_date, "%d/%m/%Y")
print(created_date.date())
print(issue_date)