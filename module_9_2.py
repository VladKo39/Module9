''''''
'''
Домашнее задание по теме "Списковые, словарные сборки"
Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.

Задача:
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

Пример результата выполнения программы:
Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
Вывод на консоль:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
Файл module_9_2.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result=[len(line) for line in first_strings if len(line)>=5 ]
# В first_result запиcь списка созданный сборкой из длин строк списка first_strings,
#  при условии, что длина строк не менее 5 символов.


second_result=[(word_first,word_second) for word_first in first_strings for word_second in second_strings
               if len(word_first)==len(word_second)]
#В second_result запись списка созданный сборкой из пар слов(кортежей) одинаковой длины.
#Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

third_strings=first_strings+second_strings
#Jбъединённые списки first_strings и second_strings.
third_result={word_third:len(word_third) for word_third in third_strings if not len(word_third)%2}
# В third_result запиcь словаря созданный сборкой где парой ключ-значение будет строка-длина строки.
# Условие записи пары в словарь - чётная длина строки.
print(first_result)
print(second_result)
print(third_result)
