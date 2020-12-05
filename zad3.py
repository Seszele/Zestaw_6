# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt
# przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie k.
# Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia


def find_shortest_path(t, k):
    global min_val
    min_val = 100000

    def recur_path(t, w, k, val):
        global min_val
        val += t[w][k]
        if w == 7:
            if val <= min_val:
                min_val = val
            return
        if k > 0:  # left
            recur_path(t, w+1, k-1, val)
        if k < 7:  # go right
            recur_path(t, w+1, k+1, val)
        recur_path(t, w+1, k, val)  # go down
    # enddef

    recur_path(t, 0, k, 0)
    return min_val
# enddef


t = [[1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 4, 3, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1],
     [1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1]]
print(find_shortest_path(t, 4))
