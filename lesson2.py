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



