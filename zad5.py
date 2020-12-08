# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.


def binary_to_decimal(b):
    result = 0
    for i in range(0, len(b)):
        result += b[len(b)-1-i] * (2**i)
    return result


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i < n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def subsequence(n, start=1):
    if is_prime(binary_to_decimal(n)) and start != 0:
        return True
    if len(n) <= 1:  # jesli nie jest prime i ma jeden digit to false
        return False

    # split to a and b
    for i in range(start, min(30, len(n))):
        a = n[:i]
        b = n[i:]
        print('a:', a, 'b:', b)
        if subsequence(a) and subsequence(b):
            return True

    return False


T = [1, 1, 0, 1, 0, 0]
print(subsequence(T, 0))
