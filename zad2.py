# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

# _ _ _ | _ _ _ _ _ _ _ _ _ _ _ _ _ _

def weigh_of_num(n):
    count = 0
    already_added = False
    while n % 2 == 0:
        if already_added == False:
            count += 1
            already_added = True
        n //= 2

    for i in range(3, n, 2):
        already_added = False
        while n % i == 0:
            if already_added == False:
                count += 1
                already_added = True
            n //= i

    if n > 2:
        count += 1

    return count


def can_divide(t):
    for i in range(len(t)):
        for j in range(i+1, len(t)-1):
            if sum_list(t, 0, i) == sum_list(t, i+1, j) == sum_list(t, j+1, len(t)-1):
                return True
    return False


def print_list(t, start, end):  # z endem włącznie
    for i in range(start, end+1):
        print(t[i], ",", end='')
    print()


def sum_list(t, start, end):  # z endem włącznie
    result = 0
    for i in range(start, end+1):
        result += weigh_of_num(t[i])
    return result


#t = [2, 3, 1, 64]
t = [30, 6, 6, 6, 30, 6, 6, 6]
#    3   2  2  2   3  2  2  2
# print(weigh_of_num(7))
# print(sum_list([1, 2, 6, 30, 64], 0, 4))
print(can_divide(t))
