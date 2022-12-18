# Comprehension, filter, map

+ [Task 1](#task-1)
+ [Task 2](#task-2)
+ [Task 3](#task-3)
+ [Task 4](#task-4)
+ [Task 5](#task-5)
+ [Task 6](#task-6)
+ [Task 7](#task-7)
+ [Task 8](#task-8)
+ [Task 9](#task-9)
+ [Task 10](#task-10)
+ [Task 11](#task-11)
+ [Task 12](#task-12)
+ [Task 13](#task-13)
+ [Task 14](#task-14)
+ [Task 15](#task-15)
+ [Task 16](#task-16)


## Task 1

Найти все числа от 1 до 1000, которые делятся на 17

```python
out = [i for i in range(1,1001) if i%17==0]
```

## Task 2
Найти все числа от 1 до 1000, которые содержат в себе цифру 2
```python 
out = [i for i in range(1,1001) if '2' in list(str(i))]
```
## Task 3
Найти все числа от 1 до 10000, которые являются палиндромом
```python 
out = [i for i in range(1, 10001) if str(i) == str(i)[::-1]]
```
## Task 4
Посчитать количество пробелов в строке
```python 
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
out = len([i for i in string if i==' '])
```
## Task 5
Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
```python 
string = 'sajfqpeodifweQDFGOSAWEQRYUOCKBXAG'
out = ''.join([i for i in string if i not in 'aeiouAEIOU'])
```
## Task 6
На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
```python 
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
out = [i for i in string.split() if len(i)<=5]
```
## Task 7
На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.
```python 
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
out = {i: len(i) for i in set(string.split())}
```
## Task 8
На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
```python 
string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
out = list(set([i.lower() for i in list(string) if i.lower() in [chr(j) for j in range(97, 123)]]))
```
## Task 9
На входе список чисел, получить список квадратов этих чисел / use map
```python 
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = list(map(lambda x: x*x, digits))
```
## Task 10
На входе список координат. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
```python 
list_of_points=[(1, 1), (2, 3), (5, 3),(1,3)]
out = {i: (i[0]**2 + i[1]**2)**0.5 for i in list_of_points if 5*i[0]-2==i[1]}
```

## Task 11
Возвести в квадрат все четные числа от 2 до 27. На выходе список.
```python 
out = [i**2 for i in range(2, 28) if i%2==0]
```
## Task 12
На входе список из координат точек на плоскости. 
Найти расстояние до самой удаленной точки от начала координат (0, 0) в первой четверти
```python 
list_of_points=[(1, 1), (2, 3), (5, 3),(1,3)]
out = max([(i[0]**2 + i[1]**2)**0.5 for i in list_of_points if i[0]>0 and i[1]>0])
```
## Task 13
На входе два списка чисел. Получить пары сумм и разниц.
```python 
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
out = [(f+s, f-s) for f,s in zip(nums_first, nums_second)]
```
## Task 14
На входе список строк из чисел. 
Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
```python 
list_of_str=['43141', '32441', '431', '4154', '43121']
out = [str(int(i)**2) for i in list_of_str if (int(i)**2)%2 == 0]
```
## Task 15
 Менеджер как обычно придумал свое представление данных, а нам оно не подходит.
 Мы хотим получить нормальную таблицу, чтобы импортировать в csv.
 
```python 
out = [{i.split(',')[0]:i.split(',')[j] for i in input_str.split('\n')} for j in range(1,len(input_str.split('\n')[0].split(',')))]
```
## Task 16
Получить сумму по столбцам у двумерного списка
```python 
a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1],
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
    
out = [sum([r[c] for r in a]) for c in range(len(a[0]))]
```
