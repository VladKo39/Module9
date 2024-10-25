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
        #результат работы функции func c параметрами sum_three(*args)
        num_nn = 0
        # счётчик подсчёта аргументов, которые без остатка
        for nn in range(sum_args):
            #задаем цикл от 0 до результата суммы аргументов (sum_args)
            if nn > 0 and sum_args % nn == 0:
            #если элемент порядка > 0 и делится без остатка
                num_nn += 1
                #увеличиваем счётчик на 1
        if num_nn <= 2:
            #если счётчик подсчёта аргументов num_nn<=2 (1- делится на 1,2- делится на 1 и на себя)
            print(f'{sum_args} - Это простое число')
            #печать Сумму элементов и Вывод по данным
        else:
            print(f'{sum_args} - Это составное число')
            # печать Сумму элементов и Вывод по данным
        return sum_args
        #возврат результата sum_three(*args)
        # (sum_three(*args)>is_prime(func)>wrapper(*args, **kwargs)>sum_args = func(*args, **kwargs)
    return wrapper
    #возврат функции wrapper(*args, **kwargs)

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
