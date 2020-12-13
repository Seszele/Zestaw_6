# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

def is_prime(n):
    if n < 1:
        return False
    if n < 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True


def bin_to_dec(n):
    result = 0
    for i in range(len(n)):
        result += int(n[len(n)-i-1]) * (2 ** i)
    return result


def all_bin_count(a, b):
    count = 0

    def bin_rec(A, B, res=''):
        nonlocal count
        if A == 0 and B == 0:
            if is_prime(bin_to_dec('1'+res)) == False:
                count += 1
                print('1'+res)
            return

        if A > 0 and B > 0:
            bin_rec(A, B-1, res+'0')
            bin_rec(A-1, B, res+'1')
        elif A > 0 and B == 0:
            bin_rec(A-1, B, res+'1')
        elif A == 0 and B > 0:
            bin_rec(A, B-1, res+'0')

    bin_rec(a-1, b)
    return count


print(all_bin_count(2, 3))
