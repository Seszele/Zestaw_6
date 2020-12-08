# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [1,7,3,5,11,2] rozwiązaniem jest liczba 10.


def lowest_R(arr, smh, s=0, i=-1, si=0, low=0):
    if s == si != 0:
        print(s)
        return True
    if i == len(arr)-1:
        return False
    return lowest_R(arr, smh, s+arr[i+1], i+1, si+i+1, 69) or lowest_R(arr, smh, s, i+1, si, 0)


#    0  1  2  3  4   5         7 1 1    7 2 1    12 3 4
T = [1, 7, 3, 5, 11, 2]
print(lowest_R(T, []))
