# Мatrices

+ [Diagonal sum](#diagonal-sum)

## Diagonal sum
Вывести сумму элементов на диагоналях. Матрица всегда квадратная

```python

def diagonalSum(mat):
    sum=0
    for i,j in enumerate(mat):
        if i!=len(mat)-i-1:
            sum+=j[-(i+1)]
            sum+=j[i]
        else:
            sum+=j[i]
    return sum
