# Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

T = [1, 3, 5, 8, 21]


def can_scale(arr, m, current_m=0, index=0, res=[]):
    if current_m == m:
        print(res)
        return True
    if index == len(arr):
        return False

    return can_scale(arr, m, current_m+arr[index], index+1, res+[arr[index]])\
        or can_scale(arr, m, current_m, index+1, res)\
        or can_scale(arr, m, current_m-arr[index], index+1, res+[-arr[index]])


print(can_scale(T, 16))
