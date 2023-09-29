import random

list =[]
print('Name draw')
for n in range(1, 5):
    name = input('Type your name: ')
    list.append(name)
student = random.choice(list)
print(f'The student drawn was: {student}')
