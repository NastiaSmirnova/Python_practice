# title Merge two sorted arrays
# description На входе есть два отсортированных массива в неубывающем порядке, объединить эти два массива в один отсортированный в неубывающем порядке
# ---end----
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