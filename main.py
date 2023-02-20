import colorama
import time
import numpy as np
from colorama import init
from colorama import Fore

init()

number = 0

print(Fore.RED+'loading...')

for i in range(11):
	print('%:',number,'/10')
	number = number + 1
	time.sleep(0.5)


x = int(input('1 нейрон-'))
y = int(input('2 нейрон-'))
u = int(input('3 нейрон-'))

w1 = int(input('вес 1 нейрона-'))
w2 = int(input('вес 2 нейрона-'))
w3 = int(input('вес 3 нейрона-'))

neuro = np.array([x * w1,y * w2,u * w3])

input('нажмите enter чтобы начался поединок')

if neuro[0] > neuro[1] & neuro[2]:
	print('1 нейронка выиграла!!!')
elif neuro[1] > neuro[2] & neuro[0]:
	print('2 нейронка выиграла')
elif neuro[2] > neuro[1] & neuro[0]:
	print('3 нейронка выиграла')
else:
	print('ничья')