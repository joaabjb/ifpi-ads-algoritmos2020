def main():
    s = 0
    num = 1
    
    for den in range(1, 51):
        s += num / den
        num += 2
    
    print('='*20)
    print(f'A soma é {s:.3f}')
    print('='*20)
        
main()