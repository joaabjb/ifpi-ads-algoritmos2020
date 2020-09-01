for i in range(1, 11):
    print('=-='*10)
    print(f'        TABUADA DO {i}')
    print('=-='*10)
    for j in range(1, 11):
        print(f'{i} + {j} = {i + j}', end='     ')
        print(f'{i} x {j} = {i * j}')