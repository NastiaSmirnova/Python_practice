# Задания с первого семинара

+ [Task 1](#task-1)
+ [Task 2](#task-2)

## Task 1
% 3 == 0 hello, 
% 5 == 0 world, 
и на 3, и на 5, то helloworld

```python
def helloWorld(n):
    for i in range(n):
        if i%3==0:
            print('hello')
        elif i%5==0:
            print('word')
        elif i%3==1 and i%5==0:
            print('helloword')
        else:
            print(i)
```
## Task 2
list, состоящий из 0 и 1. Найти длину максимальной непрерывной подпоследовательности, состоящей из 1. 
Вход: [1,1,0,1,1,1] 
Выход: 3  

```python
def ones(lst):
    max_len_ones=0
    curr_len_ones=0
    for i in range(len(lst)):
        if lst[i]==1:
            curr_len_ones+=1
            
        else:
            if max_len_ones<curr_len_ones:
                max_len_ones=curr_len_ones
            curr_len_ones=0
    if max_len_ones<curr_len_ones:
                max_len_ones=curr_len_ones
    return max_len_ones
```
## Task 3
Вход: nums = [0,1,2,4,5,7] 
Выход: ["0->2","4->5","7"]

Вход: nums = [0,1,2,3,4,5,6,7,8] 
Выход: ["0->8"]

Вход: nums = [0]
Выход: ["0"]


Вход: nums = [0, 2, 4, 6, 8]
Выход: ["0", "2", "4", "6", "8"]

```python
def sumRanges(lst):
    l = 0
    r = 0
    res = []
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            r += 1
        elif l != r:
            res.append(str(lst[l]) + "->" + str(lst[r]))
            r += 1
            l = r
        else:
            res.append(lst[l])
            l = r = i
    else:
        if l == r:
            res.append(lst[l])
        else: res.append(str(lst[l]) + "->" + str(lst[r]))
    return res
```
