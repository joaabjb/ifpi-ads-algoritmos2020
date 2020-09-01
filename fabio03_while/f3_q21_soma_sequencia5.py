def main():
    num = 1
    den = 1
    s = 0
    while num <= 99:
        s += num / den
        num += 2
        den += 1
    print(f'A soma da sequência é {s:.3f}')

main()