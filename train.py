from collections import defaultdict
import re
import pickle
import sys

s=input('Введите путь к директории, в которой лежит коллекция документов(если документы вводятся через stdin, нажмите -1): ')
s2=input('Введите путь к файлу, в котором сохраняется модель(в нашем случае model.pkl): ')
try:
    with open(s2, 'rb') as file:
        f=pickle.load(file)
        slovar=defaultdict(dict,f)
except:
    slovar=defaultdict(dict)
if s=='-1':
    result=[c.strip() for c in sys.stdin]
else:
    with open(s, encoding='utf-8') as d:
        q=''
        for c in d:
            q+=c.strip().lower()
        result = re.split(r'\s*[?,!–().;]\s*', q)
for c in result:
    g=re.split(r'''\s*[,:"'»« -]\s*''', c)
    g=list(map(lambda x: x.lower(), g))
    for j in range(len(g)-1):
        for i in range(j+1,len(g)):
            tup=tuple(g[j:i])
            if g[i] in slovar[tup].keys():
                slovar[tup][g[i]]+=1
            else:
                slovar[tup][g[i]]=1
with open(s2, 'wb') as qw:
    slovar=dict(slovar)
    pickle.dump(slovar, qw)
