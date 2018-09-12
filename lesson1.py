#hello.py
name = input("Введите свое имя")
print("Привет, {}".format(name))

#числа
a = 2
b = 4.5 #b такое, что a + b = 6.5
print(a + b) #6.5

v=input('Введите число от 1 до 10:')
print(int(v)+10) # вывод на 10 больше ввода

name=input('Введите ваше имя:')
print('Привет,'+ name.upper() +'!'+'Как дела?') # Привет, Артем! Как дела?

float(1) #1.0
int(2.5) #2
bool(1)  #True
bool(0) #False
bool'' # исключение InvalidSyntax

#сложные типы данных
weather = {"city":"Москва", "temperature":20}
print(weather["city"]) #значение по ключу city
weather["temperature"] = 15 #уменьшение t на 5С
print(weather)
print ("country" in weather)
weather[country] = "Россия"
weather["date"]="27.05.2017"
print(len(weather))

#info.py
user_info={"first_name":"Ekaterina", "last_name":"Shishkova"}
print(user_info["first_name"])

#functions
#задание 1
def get_summ(one, two, delimiter='&'):
    return str.upper(one) + str(delimiter) + str.upper(two)

sum_string = get_summ("Learn", "Python")
print(sum_string)

#задание 2
def format_price(price):
    price = int(price)
    return "Цена: {} рублей".format(price)
display_price = format_price(56.24)
print(display_price)

