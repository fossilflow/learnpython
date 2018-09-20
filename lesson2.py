# if задание 1
age=int(input('Введите ваш возраст:'))
if age < 7:
    print('Вы ходите в детский сад')
elif < 16:
    print('Вы учитесь в школе')
elif age < 23:
    print('Вы учитесь в институте')
else:
    print('Вы работаете') 

# if задание 2, сравнение 2 строк
def comparator(a, b):
    if not (isinstance(a, str) and isinstance(b, str)):
        return 0 
    if a == b:
        return 1
    elif len(a) >len (b):
        return 2 
    elif a != b and b =='learn':
        return 3
    else:
        return 'comparison is not possible'

#while
def ask_user():
    answers={"привет": "И тебе привет!",
 "как дела": "Лучше всех", 
 "пока": "Увидимся"}
    try:
        while True:
            answer = input("Как дела?")
            if answer in answers:
                print(answers[answer])
            elif answer == "Хорошо":
                break
    except KeyboardInterrupt:
        print ("Пока")
        return
ask_user()

# for
school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '5a', 'scores': [3,4,2,4,2]}, 
{'school_class': '7a', 'scores': [3,4,4,5,2]},  ]
total_ave_score = 0
total_stud = 0

for class_ in school:
    scores = class_["scores"]
    total_ave_score += sum(scores)
    total_stud += len(scores)
    average_score = (sum(scores)/len(scores))
    print("Средняя оценка класса {} - {} баллов".format(class_["school_class"], average_score))
print("Средняя оценка в школе {}".format(total_ave_score/total_stud))


#exceptions
def get_summ(num_one, num_two):
    try:
        summ = int(num_one)+int(num_two)
    except ValueError:
        return("It's not a numbers")   