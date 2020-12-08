# Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

T = [1, 3, 5, 8, 21]


def can_scale(arr, m, current_m=0, index=0):
    if current_m == m:
        return True
    if index == len(arr):
        return False

    return can_scale(arr, m, current_m+arr[index], index+1) or can_scale(arr, m, current_m, index+1)\
        or can_scale(arr, m, current_m-arr[index], index+1)


print(can_scale(T, 16))
