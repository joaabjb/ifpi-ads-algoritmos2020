def main():
    n = 1
    while n <= 10:
        print('='*6,'TABUADA DO',n,'='*6)
        i = 0
        while i <= 10:
            print(f'{n:2} + {i:2} = {n + i:2}    {n:2} x {i:2} = {n * i:2}')
            i += 1
        n += 1
        print()

main()