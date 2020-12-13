# Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.
T = [[1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 82, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 35, 2],
     [1, 4, 6, 2, 3, 5, 91, 2],
     [1, 4, 6, 82, 3, 5, 24, 2],
     [1, 4, 6, 2, 3, 5, 35, 7],
     [1, 4, 6, 2, 3, 5, 35, 8], ]


def dest_val(w, k):
    global T
    return T[w][k] // 10**(len(str(T[w][k]))-1)


def trip_recursive(w=0, k=0):
    global T
    current_val = T[w][k] % 10

    if w == 7 and k == 7:
        return True
    else:
        # k +1 go w prawo
        if k < 7 and current_val < dest_val(w, k+1):
            if trip_recursive(w, k+1):
                return True
        if w < 7 and k < 7 and current_val < dest_val(w+1, k+1):
            if trip_recursive(w+1, k+1):
                return True
        if w < 7 and current_val < dest_val(w+1, k):
            if trip_recursive(w+1, k):
                return True
        if (7-w)**2+(7-k)**2 >= (6-w)**2+(8-k)**2 and w < 7 and k > 0 and current_val < dest_val(w+1, k-1):
            if trip_recursive(w+1, k-1):
                return True
        return False
    return False


print(trip_recursive())
