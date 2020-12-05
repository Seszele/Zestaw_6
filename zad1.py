# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.
# 17113 17 13 11 113

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def twoDigitPrime(num):
    if num < 3:
        print('invalid argument')
        return False

    results = set()

    def f(num):
        for i in range(1, len(str(num))):
            temp = num
            # usun i cyfre
            a = temp//(10**i)
            b = temp % 10**i

            if a-10 > 0 and isPrime(a):
                # print(a)
                results.add(a)
                pass
            if b-10 > 0 and isPrime(b):
                # print(b)
                results.add(b)
                pass
            if a - 10 > 0:
                f(a)
            if b - 10 > 0:
                f(b)
            #print(a, b)

    f(num)
    print(results)


twoDigitPrime(17113)
