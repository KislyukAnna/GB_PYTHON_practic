import time

s = 12
p = 27

prg1_start = time.time()
# Введите ваше решение ниже

x, y = 0, 0

for x in range(s):
    y = s - x
    if x > y:
        break
    if x * y == p and x <= y:
        print(x, y)
        break

prg1_stop = time.time()

prg2_start = time.time()

x, y = 0, 0

for y in range(1000):
    for x in range(1000):
        if x > y:
            break
        if x + y == s and x * y == p:
            print(x, y)

prg2_stop = time.time()

prg3_start = time.time()

s = 12
p = 27
d = []
for i in range(1,p+1):
    if p%i == 0:
        d += [i]

for i in range(len(d)):
    for j in range(i,len(d)):
        if d[i]+d[j] == s:
            print(d[i],d[j])

prg3_stop = time.time()

res1 = (prg1_stop - prg1_start) * 1000
res2 = (prg2_stop - prg2_start) * 1000
res3 = (prg3_stop - prg3_start) * 1000

print(f'Программа 1 выполнена за {res1} мс\nПрограмма 2 выполнена за {res2} мс\nПрограмма 3 выполнена за {res3} мс')

s = 12
p = 27

i = 1
half_s = s/2
i = 0
while i <= half_s:
    if i * (s-i) == p:
        print(i, s-i)
        
    else:
        i += i
