''''''
'''
Домашнее задание по теме "Введение в функциональное программирование"
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.

Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
Вывод на консоль:
{'max': 20, 'min': 6}
{'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
'''

def apply_all_func(int_list: int or float, *functions):
    '''
    :param int_list: number type int or float
    :param functions: tuple(function sum,len,min,max,sorted.....) user for int or float
    :return: dictionary resuls{name.function:function.number}
    '''
    results={}
    #dictionary
    for func in functions:
        #function in tuple(function)
        results[func.__name__]=func(int_list)
        #append in resuls{name.function:function.number}
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))