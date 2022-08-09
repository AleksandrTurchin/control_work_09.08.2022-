# 1) Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# На экран вывести словарь из 3-х самых часто встречаемых чисел.

string_input = input('Введите в случайной последовательности числа от 0 до 9: ')
number_dict = {int(i): string_input.count(i) for i in string_input}
sorted_num_dict = sorted(number_dict.items(), key=lambda e: e[1])
print(dict(sorted_num_dict[-3:]))


# 2) Дан список содержащий любые значения. Пользователь вводит число.
# С помощью механизма обработки исключений, последовательно делить введенное число на значения из списка.
# В случае возникновения исключения, выводить детали ошибки. В случае деления на ноль, прервать цикл.
try:
    _list = [4, 2, 5, 10, 0]
    a = int(20)
    lst = []
    for i in _list:
        lst.append(a / i)
raise exsept as ex_obj:
    print(lst)
except ZeroDivisionError:
    break




# 3) Имеется файл file.txt с текстом. Напишите программу, которая выводит следующую статистику по тексту:
# количество букв латинского алфавита;
# число строк.

letters_abc = 0
strings = 0
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        strings += 1
        letters_abc += len([i for i in line if i.isalpha()])
    print(strings)
    print(letters_abc)
