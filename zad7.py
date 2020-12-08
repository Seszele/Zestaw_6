# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie
# określonej masy. Odważniki można umieszczać tylko na jednej szalce

T = [1, 3, 5, 8, 21]


def can_scale(arr, m, current_m=0, index=0):
    if current_m == m:
        return True
    if index == len(arr):
        return False

    return can_scale(arr, m, current_m+arr[index], index+1) or can_scale(arr, m, current_m, index+1)


print(can_scale(T, 16))
