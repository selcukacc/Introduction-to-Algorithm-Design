'''
ALGORİTMA ANALİZİ:
Algotitmanın return statement’ında problem iki parçaya bölünür. 

Master Teoremi’nden: T(n) = 2T(n/2) + O(1) --> a = 2, b = 2, d = 0 olur.
            a > b^d, 2 > 2^0  --> T(n) = O(n^(log2)) 
'''

# Test case
arr = [23, 22, 2, 32, -11, 45]

# Tum indekslerdeki elemanları indeks
# numarasiyla karsilastirir.
def find_index_i(arr, first, last):
    # Ortanca indeks bulunur.
    middle = (first + last) // 2
    
    # Eger eleman indeks numarasine esitse
    # true dondurulup, sonuc print edilir.
    if arr[middle] == middle:
        print("There is an index i for ", "arr[", middle, "] = ", middle)
        return True
    # Eger verilen aralikta bir eleman varsa ve
    # o elaman indekse esit degilse sonuc false olur.
    if arr[middle] != middle and first == last:
        return False
    # Problem iki parcaya ayirilarak arama recursive
    # devam eder.
    return (find_index_i(arr, first, middle) or 
            find_index_i(arr, middle+1, last))

def find_i(arr):
    n = len(arr)
    if n <= 0:
        print("There is no such index.")
        return -1
    if find_index_i(arr, 0, n-1) == False:
        print("There is no such index.")        
        return -1

find_i(arr)