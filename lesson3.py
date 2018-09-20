#задание 1
import csv
from datetime import datetime, timedelta
now = datetime.now()
delta1 = timedelta(days=1)
print(now)
print(now + delta1)
print(now - delta1)

first_day_of_current_month = now.replace(day=1)
last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
this_day_last_month = now.replace(month = last_day_of_previous_month.month)
print(this_day_last_month)

# задание 2 даты
date_string = '01/01/2017 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S.%f')
print(date_dt)

#work with files
with open(r"referat.txt", 'r') as ref:
    text=ref.read()
    print(len(text))
    words=text.split()
    print(len(words))
    text = text.replace(".", "!")
with open("referat2.txt", "w",  encoding='utf-8') as ref2:
	ref2.write(text)

#csv
dict_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},]

with open('dict_list.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for lines in dict_list:
        writer.writerow(lines)