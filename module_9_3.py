''''''
'''
Домашнее задание по теме "Генераторные сборки"
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, 
которая высчитывает разницу длин строк из списков first и second, если их длины не равны. 
В переменную second_result запишите генераторную сборку, 
которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. 
Пример результата выполнения программы:
Пример выполнения кода:
print(list(first_result))
print(list(second_result))
Вывод в консоль:
[1, 2]
[False, False, True]
Примечания:
Это небольшая практика, поэтому важность выполнения каждого условия обязательна.
Файл module_9_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result=(len(first)-len(second) for first,second in zip(first,second) if  len(first)!=len(second))
second_result=(len(first[n])==len(second[n]) for n in range(len(first)))
print(list(first_result))
print(list(second_result))