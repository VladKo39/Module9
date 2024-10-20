''''''
'''
Домашнее задание по теме "Итераторы"

Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__. 
Закрепить навык создания и выбрасывания исключений.

Задача "Range - это просто":


Пример результата выполнения программы:
Пример выполняемого кода:
try:
iter1 = Iterator(100, 200, 0)
for i in iter1:
print(i, end=' ')
except StepValueError:
print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
print(i, end=' ')
print()
for i in iter3:
print(i, end=' ')
print()
for i in iter4:
print(i, end=' ')
print()
for i in iter5:
print(i, end=' ')
print()

Вывод на консоль:
Шаг указан неверно
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1

Примечания:
Особое внимание уделите методу __next__ и условиям в нём.
Файл module_9_5.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''


class StepValueError(Exception):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step: int = 1):
        '''
        При инициализации принимает
        :param start: int значение старта
        :param stop: int  конец итерации
        :param step: int =1 шаг
        if step == 0 exception StepValueError(f'Шаг не может быть равен 0')
        '''
        self.start = start
        self.stop = stop
        self.step = step

        if step == 0:
            raise StepValueError(f'Шаг не может быть равен 0')

    def __iter__(self):
        '''
        метод сбрасывает значение pointer на start и
        :return:  возвращает сам объект итератора.
        '''
        self.pointer = self.start
        return self

    def __next__(self):
        '''
        метод увеличивающий атрибут pointer на step.
        В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop,
        # либо меньше stop
        :return: следующий элемент интератора range_element
        '''
        inter_element = self.pointer
        #'следующий элемент
        self.pointer += self.step
        #перемещаем элемент на указанный шаг
        if ((self.step > 0 and inter_element > self.stop) or
                (self.step < 0 and inter_element < self.stop)):
            raise StopIteration()
            #вызов прекращения интерации

        return inter_element
        #возврат текущего элемента

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except (StepValueError):
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')

print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
