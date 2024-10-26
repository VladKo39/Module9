''''''
'''
Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом 
и "Составное" в противном случае.

Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11
Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''

from math import sqrt


def is_prime(func):
    '''
    Функция декоратор определяет является ли число простым или составным
    :param func: sum_three function
    :return: wrapper function
    '''

    def wrapper(*args, **kwargs):
        '''
        :param args: param sum_three(()
        :param kwargs: None
        :return: wrapper function (myself)
        '''
        sum_args = func(*args, **kwargs)
        # результат работы функции func c параметрами sum_three(*args)
        num_nn = 0
        # счётчик подсчёта аргументов, которые без остатка
        # проверяем, является ли вводимое число больше 1(простые и составные числа >1)
        if not sum_args > 1:
            # если результата суммы аргументов (sum_args) не больше 1
            print(f'{sum_args}  Данное число не относится ни к простым ни к составным числам ')
            # вывод сообщения
        else:
            i = 2
            # 2 - первое число из ряда чисел на которое будем делить квадратный корень аргумента
            while i <= sqrt(sum_args):
                # цикл с условием, работает, пока делитель меньше или равен квадратному кореню аргумента
                if sum_args % i == 0:
                    # если аргумент делиться на i без остатка
                    print(f'{sum_args} Составное число')
                    # вывод сообщения
                    break
                    # завершение цикла
                i += 1
                # увеличиваем делитель на 1
            else:
                # иначе
                print(f'{sum_args} Простое число')
                # вывод сообщения
        return sum_args
        # возврат результата sum_three(*args)
        # (sum_three(*args)>is_prime(func)>wrapper(*args, **kwargs)>sum_args = func(*args, **kwargs)

    return wrapper
    # возврат функции wrapper(*args, **kwargs)


@is_prime  # декорируем sum_three()
def sum_three(*args):
    '''
    Подсчёт суммы вводимых аргументов
    :param args: list arguments(args)
    :return: sum arguments (sum_num)
    '''
    sum_num = 0
    for number in args:
        sum_num += number
    return sum_num


result = sum_three(2, 3, 6)
print(result)
