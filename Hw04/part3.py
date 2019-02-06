# Hw04-part3
# Islam Goktan Selcuk
# 141044071

arrays = [ [1, 7, 12],
           [8 , 13, 14],
           [2, 3, 8] ]

# Verilen array listesini sirali tek bir listeye donusturur.
def sortArrays(arrays):
    numberOfArrays = len(arrays)
    # Eger array sayisi birden fazlaysa isleme devam et.
    if numberOfArrays > 1:
        # 0. ve 1. array'leri birlestirir.
        arrays[0] = mergeArrays(arrays[0], arrays[1])
        # Array'leri birlestirdikten sonra 1. indeksteki array silinir.
        arrays.remove(arrays[1])
        # Array silindikten sonra tekrar fonksiyon cagirilir.
        sortArrays(arrays)
    return arrays[0]

# Verilen iki sirali array'i sirali tek bir array olarak dondurur.
def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)    
        
    i = 0; j = 0; k = 0
    array = [None] * (n1 + n2)
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            array[k] = arr1[i]
            i = i + 1
        else:
            array[k] = arr2[j]
            j = j + 1
        k = k + 1
    
    if i == n1:
        while j < n2:
            array[k] = arr2[j]
            j = j + 1
            k = k + 1
    elif j == n2:
        while i < n1:
            array[k] = arr1[i]
            i = i + 1
            k = k + 1
    return array

print(sortArrays(arrays))