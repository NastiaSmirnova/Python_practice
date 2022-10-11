f = open('solution.py')
contents = f.read()
f.close()

splited=contents.split('# ---end----')
characteristics=splited[0]
code =splited[1]
characteristics=characteristics.split('\n')

for i in range (len(characteristics)):
    if characteristics[i].startswith('# title'):
        title=characteristics[i].split('# title')[-1].strip()
    if characteristics[i].startswith('# description'):
        description=characteristics[i].split('# description')[-1].strip()
        
res=[]
res.append('+ [{0}](#{1})'.format(title,'-'.join(title.lower().split())))
res.append('## {}'.format(title))
res.append(description)
res.append('```python')
res.extend(code[1:].split('\n'))
res.append('```')

with open('out.txt', "w") as file:
    for  line in res:
        file.write(line + '\n')