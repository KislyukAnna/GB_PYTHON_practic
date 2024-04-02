import time


prg1_start = time.time()

prg1_stop = time.time()

prg2_start = time.time()

prg2_stop = time.time()

prg3_start = time.time()



prg3_stop = time.time()

res1 = (prg1_stop - prg1_start) * 1000
res2 = (prg2_stop - prg2_start) * 1000
res3 = (prg3_stop - prg3_start) * 1000

print(f'Программа 1 выполнена за {res1} мс\nПрограмма 2 выполнена за {res2} мс\nПрограмма 3 выполнена за {res3} мс')
