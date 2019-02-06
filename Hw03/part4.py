'''
max_sub_arr() fonksiyonunun çalışma zamanını Master Theorem ile bulabiliriz.

T(n) = 2T(n/2) + n     -->     a = 2, b = 2, d = 1 olur.

a = b^d,  2 = 2^1 --> T(n) = nlog(n)
'''


import sys
arr = [-10, 10, 22, -8, 12, -5, -1]

# Array içerisindeki maximum toplamı içeren 
# dizinin toplamını return eder.
def max_sub_arr(arr, first, last):
# Base case: Eger fonksiyona gonderilen array'in
#            boyutu bir ise deger dondurulur.
    if first == last:
        return arr[first]
    
    # Ortanca indeks bulunur.
    middle = (first + last) // 2

    # Array'in ilk yarısı icin fonk calistirilir.
    first_part = max_sub_arr(arr, first, middle)
    # Array'in ikinci yarısı icin fonk calistirilir.
    second_part = max_sub_arr(arr, middle + 1, last)
    # Iki dizinin kesisimi icin fonk calistirilir.
    intersection_part = intersection_sum(arr, first, middle, last)
    
    max_val = max(first_part, second_part, intersection_part) 
    return max_val
    
def intersection_sum(arr, first, middle, last):
    sum = 0
    # Daha sonra max deger karsilastirmasi icin minimum deger atanir.
    left_sum = -sys.maxsize

    # Ortanca indeksten first indeksine kadar
    # degerler toplanir ve sol kisim icin maksimum 
    # deger bulunur.
    for i in range(middle, first-1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
    sum = 0
    # Yukaridaki islemlerin aynısı dizinin sag
    # tarafi icin tekrar edilir.
    right_sum = -sys.maxsize
        
    for i in range(middle + 1, last + 1) : 
        sum += arr[i] 
        if (sum > right_sum) : 
            right_sum = sum 

    # Iki sonucun toplami return edilir.
    return left_sum + right_sum;

x = max_sub_arr(arr, 0, len(arr)-1)
print(x)