import pickle
import random
s=input('Введите путь к файлу, из которого загружается модель (в нашем случае model.pkl): ')
prefix=input('Введите префикс (если хотите выбрать рандомный, нажмите -1): ')
length=int(input('Введите длину генерируемой последовательности: '))
with open(s, 'rb') as file:
    d=pickle.load(file)
if prefix=='-1':
    l=list(d.keys())
    prefix=random.choice(l)
    print(prefix, end=' ') 
else:
    prefix=tuple(prefix.lower().split())
if prefix in d.keys():
    qw=False
    b=[]
    a=list(d[prefix].keys())
    for i in range(len(a)):
        if d[prefix][a[i]]==max(d[prefix].values()):
            b.append(a[i])
            del a[i]
            length-=1
            break
    while length>0:
        if len(a)>0:
            r=random.randrange(len(a))
            b.append(a[r])
            length-=1
            del a[r]
        else:
            qw=True
            break
    print(*b)
    if qw:
        print('Больше вариантов продолжения нет в базе')
else:
    print('Такого префикса пока нет в базе')
    
