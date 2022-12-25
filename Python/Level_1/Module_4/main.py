# Список (list) в Python - упорядоченная изменяемая коллекция объектов

# Создается список с помощью [], либо list()
# Создадим пустой список ("empty list") и проверим его тип
lst = []
print(lst, type(lst))  # [] <class 'list'>

# В списке могут храниться объекты произвольных типов.
# Присвоим переменной lst список с объектами четырех различных типов (integer,
# float, bool, string)
lst = [2, 3.5, True, '2']
print(lst)  # [2, 3.5, True, '2']

# Каждый элемент списка имеет свой индекс, начинающийся с нулевого (0)
# Вызвать элемент можно указав его индекс в списке
lst = ['apple', 'plum', 'cherry']
print(lst[0])    # apple
print(lst[2])    # cherry

# Изменить значение элемента списка можно обратившись к нему по индексу
lst[2] = 'carrot'
print(lst)  # ['apple', 'plum', 'carrot']

# Иногда удобнее использовать отрицательные индексы для вызова элементов
# Отсчет отрицательных индексов идет с конца и начинается с -1
print(lst[-1])  # carrot
print(lst[-3])  # apple

# Списками удобно оперировать с помощью срезов (slice)
# Конструкцию среза можно обозначить тремя английскими S (3S)
# list[start : stop : step]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[:3])    # [0, 1, 2]
print(lst[4:9])   # [4, 5, 6, 7, 8]
print(lst[2::2])  # [2, 4, 6, 8]
print(lst[::])    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Проверить наличие элемента в списке удобно с помощъю операторов IN, NOT IN
pipe = ['а', 'и', 'б']
if 'д' in lst:
    print('"д" тоже сидит на трубе')
elif 'д' not in lst:
    print('"д" нет на трубе')
else:
    print('Как это получилось?')
# Давайте подумаем, что выведет код

# Методы - это функции, вызываемые с использованием точечной нотации.
# Посмотреть методы класса можно с помощью функции dir(), позволяющей увидеть
# атрибуты соответствующего класса. В нашем случае это класс список (list)
lst = ['b', 'c', 'd']
print(dir(lst))  # ['__add__', ..., 'sort']

# Двойным нижним подчеркиванием обозначены так называемые "магические" методы.
# Оставим их пока в стороне. На текущем этапе нас интересуют атрибуты без
# подчеркиваний, также являющиеся методами класса, но уже не "магическими"
# Рассмотрим пример
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')   # 2 | колличество apple в списке
fruits.index('banana')  # 3 | индекс первого пояления banana

# Методы, указанные ниже, изменяют имеющийся список и не создают его копию
lst = ['b', 'c', 'd']
# .append() добавляет элемент в конец списка
lst.append('e')         # ['b', 'c', 'd', 'e']
# .insert() вставляет элемет в указанный индекс
lst.insert(0, 'a')      # ['a', 'b', 'c', 'd', 'e']
# .extend([]) присоединяет один список к другому
lst.extend(['f', 'g'])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# .reverse() разворачивает список в обратном порядке
lst.reverse()           # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
# .remove() удаляет элемент
lst.remove('c')         # ['g', 'f', 'e', 'd', 'b', 'a']
# .pop() удаляет элемент с указанным индексом и при вызове возвращает его
lst.pop(1)              # ['g', 'e', 'd', 'b', 'a']
# .sort() сортирует список по возрастанию
lst.sort()              # ['a', 'b', 'd', 'e', 'g']


# Поскольку список является упорядоченной коллекцией объектов различных типов,
# то в нем можно хранить другие списки

# Например, список с вложенными списками может выглядеть так
lst = [2, 3.5, True, '2', ['list']]
print(lst)  # [2, 3.5, True, '2', ['list']]

# Доступ к элементам вложенного списка можно получить также по индексам,
# не много дополнив обращение еще одним уровнем глубины
# В качестве примера изменим наш список lst, заменив в нем вложенный список
lst[-1] = [3, 4.0, False, '8']
print(lst)  # [2, 3.5, True, '2', [3, 4.0, False, '8']]

# Обратимся к элементам вложенного списка
print(lst[-1][2])   # False
print(lst[-1][1:3])  # [4.0, False]

# Со списками, в том числе и вложенными удобно работать посредством циклов
# Рассмотрим их далее


# Списки можно использовать в связке с FOR and IN
# C помощью цикла FOR можно проитерировать по всем элементам списка и, например,
# получить их сумму
numbers = [1, 2, 3, 4, 5]
summa = 0
for num in numbers:
    summa += num
print(summa)  # 15
# Аналогичный результат можно получить, применив функцию sum()
print(sum(numbers))  # 15

# Если необходимо в задаче оперировать индексами списка, то это удобно делать
# с помощь изученной нами на прошлом занятии функции range().
# В качестве примера разделим список "на первый-второй"
numbers = [2, 4, 5, 7, 49]
lst_first = []
lst_second = []
for idx in range(len(numbers)):
    if idx % 2 == 0:  # индекс элементов второй группы делится на 2 без остатка
        lst_second.append(numbers[idx])
    else:
        lst_first.append(numbers[idx])
print(lst_first, lst_second)  # [4, 7] [2, 5, 49]

# Когда при итерировании по списку необходимо получить и индексы, и значения,
# удобно использовать функцию enumerate()
lst = ['a', 'b', 'c']
for idx, elem in enumerate(lst):
    print(f"Индекс '{elem}' равен {idx}")  # Индекс 'a' равен 0

# Кроме цикла FOR со списками можно работать с помощью WHILE
# Например, выведем на перчать каждый третий элемент списка
lst = ['a', 'b', 'c', 'd']
idx = 2
while idx < len(lst):
    print(lst[idx])  # с
    idx = idx + 3

# Используя цикл FOR можно создавать списки желаемого размера
# Например, мы хотим создать список из 10 элементов
lst =[]
for element in range(10):
    lst.append(element)
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Есть альтернативный способ создания списка, называющийся list comprehenshion
lst = [i for i in range(10)]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list comprehension занимает меньше строк в коде и исполняется быстрее
# также его можно использовать с операторами IF и IF/ELSE

# IF позволяет создавать список, при налисии необходимости соответствия
# елементов итерируемого объекта, используемого для создания списка,
# необходимому условию. Звучит сложно, рассмотрим пример
lst = [i for i in range(10) if i % 2 == 0]
print(lst)  # [0, 2, 4, 6, 8]

# IF/ELSE дает возможность определять какое значение элемента заносить в список
lst = [i if (i % 4 != 0) else f'{i}' for i in range(10)]
print(lst)  # ['0', 1, 2, 3, '4', 5, 6, 7, '8', 9]

# IF и IF/ELSE можно комбинировать
lst = [i if (i % 4 != 0) else f'{i}' for i in range(10)  if i % 2 == 0]
print(lst)  # ['0', 2, '4', 6, '8']

# list comprehension можно использовать для формирования списков с одними
# значениям. Это бывает полезно, при работе с векторными представлениями данных
n = 5
lst = [0 for i in range(n)]
print(lst)  # [0, 0, 0, 0, 0]

# Также можно создать список c равными по величине вложенными списками
col = row = 4
lst = [[0 if (m != n) else 1 for m in range(row)] for n in range(col)]
print(lst)  # [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]