# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [1,7,3,5,11,2] rozwiązaniem jest liczba 10.


def lowest_R(arr, s=0, i=-1, si=0, low=0):
    if s == si != 0:
        return (low, s)
    if i == len(arr)-1:
        return (len(arr)+1, -1)

    a = lowest_R(arr, s+arr[i+1], i+1, si+i+1, low + 1)
    b = lowest_R(arr, s, i+1, si, low)

    return a if a[0] < b[0] else b


def lowest(arr):
    result = lowest_R(arr)
    if result[1] != -1:
        return result[1]
    return None


#    0  1  2  3  4   5         7 1 1    7 2 1    12 3 4
T = [1, 7, 3, 5, 11, 2]
print(lowest(T))
