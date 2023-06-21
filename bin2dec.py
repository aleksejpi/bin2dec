binary_num = input("Введите двоичное число: ")
decimal_num = int(binary_num, 2)

with open('output.txt', 'w') as f:
    f.write(f'Двоичное число {binary_num} в десятичном виде равно {decimal_num}')
