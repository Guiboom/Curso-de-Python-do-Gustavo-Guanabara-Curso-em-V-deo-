import random 
n=5
nums = []

for _ in range(n):
    nums.append(random.randint(1, 10))

tupla1 = tuple(nums)
print(f'Listagem de números: {tupla1}')
print(f'Em ordem: {sorted(tupla1)}')
print(f'Menor:{sorted(tupla1)[0]}')
print(f'Maior:{sorted(tupla1)[-1]}')
