# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random
n = int(input('Введите количество монет: '))
k = 0
for i in range(n):
      r = random.randint(0,1)
      print(r)
      if r == 1:
        k += 1
print('Минимальное число монет, которые нужно перевернуть')
print(k if k<n/2 else n-k)


