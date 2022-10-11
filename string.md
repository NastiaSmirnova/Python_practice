# Strings

+ [Сompress](#compress)


## Сompress

```python

def compress(elems):
    res = ""
    i, j = 0, 0
    count=0
    while i < len(elems):
        while j < len(elems) and elems[i] == elems[j]:
            count+=1
            j+=1
        if count>1:
            res+=str(elems[i])+str(count)
        else:
            res+=str(elems[i])
        print(i,j)
        i=j
        count=0
    return res
```
