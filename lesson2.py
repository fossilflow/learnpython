# if задание 1
age=int(input('Введите ваш возраст:'))
if age < 7:
    print('Вы ходите в детский сад')
elif 7 <= age < 16:
    print('Вы учитесь в школе')
elif 16 <= age < 23:
    print('Вы учитесь в институте')
else:
    print('Вы работаете') 

# if задание 2, сравнение 2 строк
def comparator(a, b):
    if a is not str or b is not str:
        return 0 
    if a is b:
        return 1
    elif len(a) <len (b):
        return 2 
    elif a is not b and b=='learn':
        return 3
    else:
        return 'comparison not possible'

#while
def ask_user():
    answers={"привет": "И тебе привет!",
 "как дела": "Лучше всех", 
 "пока": "Увидимся"}
    while True:
        answer = input("Как дела?")
        if answer == "Хорошо!":
            break
        else:
            try:
                print(answers[answer])
            except KeyError:
                pass
            except KeyboardInterrupt:
                print ("Пока")
                break

#exceptions
def get_summ(num_one, num_two):
    try:
        summ = int(num_one)+int(num_two)
    except ValueError:
        return("It's not a numbers")                


# цикл for,практика
list=[1, 2, 3, 4, 5, 6, 7, 8, 11, 17, ]
for num in list:
	print(num + 1)

string=str(input())
for s in string: 
	print(s)

# цикл for задание
list=[{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '5a', 'scores': [5,4,4,5,4]}, ]

def average_score(scores):
    return float(sum(scores)/len(scores))

# computation of average scores in class
for class_ in list:
    print("Средняя оценка в классе {} {} ".format(class_['school_class'], 
   average_score(class_['scores'])))

# computation of average scores in school
all_scores=[]
for class_ in list:
    for score in class_['scores']:
        all_scores.append(score)
print("Средняя оценка в школе {} ".format(average_score(all_scores)))


answers={"привет": "И тебе привет!",
 "как дела": "Лучше всех", 
 "пока": "Увидимся"}


def get_answer(question, answers):
    try:
        return(answers[question])
    except KeyError:
    	return ("Не знаю, что ответить.")
    except KeyboardInterrupt:
        return ("Пока")

def asc_users(answers):
    while True:
        user_input = input("Скажи что-нибудь:")
        answer = get_answer(user_input, answers)
        print(answer)
        if user_input == "пока":
            break

asc_users(answers)
