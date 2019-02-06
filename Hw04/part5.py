# Hw04-part5
# Islam Goktan Selcuk
# 141044071

variables = ['x1', 'x2', 'x3', 'x4']

constraints = ['x1=x2', 'x2=x3', 'x3=x4', 'x1≠x4']

# Birbirine esit olan degiskenleri bir array'de
# ayni degeri atayarak isaretler
def createUnion(arr, n, i, j):
    temp = arr[i]
    for k in range(0, n):
        if arr[k] == temp:
            arr[k] = arr[j]

# Verilen degiskenlerin verilen esitlikleri saglayip saglamadigi kontrol edilir.
def  isConstraintsSatisfied(constraints, variables):
    n = len(variables)
    arr = [None] * n
    # Degiskenlerin esitliklerini kaydetmek icin bir array olusturulur.
    for i in range(0, n):
        arr[i] = i

    indexes = {}
    j = 0
    # Tum degiskenler'e dictionary kullanilarak bir indeks atanir.
    for x in variables:
        indexes[x] = j
        j += 1

    # Esit olan degiskenler array uzerinden isaretlenir.
    for x in constraints:
        tokens = x.split('=')
        if len(tokens) == 2:
            createUnion(arr, n, indexes[tokens[0]], indexes[tokens[1]])
    # Array'de esit olarak isaretlenen aynı degere sahip olan degiskenler icin
    # esit olmadiklarini iceren bir constraints bulunursa fonkstion false return eder.
    for x in constraints:
        tokens = x.split('≠')
        if len(tokens) == 2:
            if arr[indexes[tokens[0]]] == arr[indexes[tokens[1]]]:
                print("Constraints is not satisfied!")
                return False

    print("Constraints is satisfied.")
    return True

isConstraintsSatisfied(constraints, variables)