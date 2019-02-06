# Islam Goktan Selcuk
# 141044071

A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]

# Optimum penalty ile hedefe ulasacak path ve penalty degeri bulunur.
def optimal_sequence(arr):
    # Baslangic noktasi icin listenin basina sıfır eklenir.
    arr.insert(0,0)
    n = len(arr)
    
    # Listeler initialize edilir.
    result = [None] * (n) 
    path = [None] * (n)
    path[0] = [0]
    result[0] = 0

    # Her durak icin optimum penalty bulunur ve
    # path ile birlikte kaydedilir.
    for i in range(1, n):
        # 1. durak icin penalty hesabi
        min = result[0] + (200 - (arr[i]-0))**2
        minIndex = 0
        path[i] = []
        # i. durak icin optimum penalty bulunur.
        for j in range(1, i):     
            temp = result[j] + (200 - (arr[i]-arr[j]))**2
            if temp < min:
                min = temp
                minIndex = j
        # i. durak icin path ve penalty kaydedilir.
        temp = path[minIndex]
        path[i] = temp[:]
        path[i].append(i)
        
        result[i] = min
        print("path[", i, "]: ", path[i], " = ", result[i])
   
    return result

print("\nAll distances: ", optimal_sequence(A))