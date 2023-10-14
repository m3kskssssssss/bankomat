from num2words import num2words

def num_to_w(n):
    if 0 <= int(n) <= 100000:
        return num2words(n, lang='ru')
    else:
        print('Неправильный ввод')
def add_rub(num):
   last_num = int(num) % 10
   if last_num == 1 and int(num) != 11:
       return ' рубль'
   elif 1 < last_num < 5 and not 11 < int(num) < 15:
       return ' рубля'
   elif last_num == 0:
       return ' рублей'
   else:
       return ' рублей'

t = 1
while t > 0:
    num = input('Введите число от 0 до 100000: ')
    try:
        if 0 <= int(num) <= 100000 :
            print("Получилось " + str(num_to_w(num)) + str(add_rub(num)) + ".")
            t -= 1
        else:
            print("Число не входит в диапазон.")
    except ValueError:
        print("Введите число, а не буквы.")