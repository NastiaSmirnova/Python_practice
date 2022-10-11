# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge two sorted arrays](#merge-two-sorted-arrays)

## Squares of sorted array

Возвращение отсортированного массива, состоящего из элементов начального массива, возведенных в квадрат за O(n)

```python

def merge(first, second):
    result = []
    count_el = len(first) + len(second)
    for i in range(count_el):
        if first != [] and second != []:
            if first[0] <= second[0]:
                result.append(first.pop(0))
            else:
                result.append(second.pop(0))
        elif not first:
            result.append(second.pop(0))
        elif not second:
            result.append(first.pop(0))
    return result


def merge(first, second):
    res=[]
    i=0
    j=0
    if len(first)==0:
        return second
    elif len(second)==0:
        return first
    else:
        while i<len(first) and j<len(first):
            if first[i]<=second[j]:
                res.append(first[i])
                i+=1
            else:
                res.append(second[j])
                j+=1
        if i==len(first):
            res.extend(second[j:])
        else:
            res.extend(first[i:])
    return res

def squares(s):
    k=0
    while s[k]<0 and k<len(s)-1:
        k+=1
    posit = [j**2 for j in s[k:]]
    neg = [s[j]**2 for j in range(k-1,-1,-1)]
    return merge(posit,neg)

```

## Merge two sorted arrays

```python 

def merge(first, second):
    res=[]
    i=0
    j=0
    if len(first)==0:
        return second
    elif len(second)==0:
        return first
    else:
        while i<len(first) and j<len(first):
            if first[i]<=second[j]:
                res.append(first[i])
                i+=1
            else:
                res.append(second[j])
                j+=1
        if i==len(first):
            res.extend(second[j:])
        else:
            res.extend(first[i:])
    return res

```
