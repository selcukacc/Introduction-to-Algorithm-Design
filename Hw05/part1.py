# Hw05 - Part1
# Islam Goktan Selcuk -- 141044071

# Test inputs
times = [1, 3, 5, 2]
weights = [10, 2, 4, 7]

# Time/weight oranlarini siralamak icin kullanılan 
# merge sort fonksiyonu
def mergeSort(array):    
    n = len(array)
    if n > 1:  
        arr1 = array[0:int(n/2)]
        arr2 = array[int(n/2):n]

        mergeSort(arr1) # Listenin ilk yarisi siralanir.
        mergeSort(arr2) # Listenin ikinci yarisi siralanir.

        n1 = len(arr1)
        n2 = len(arr2)    
        
        i = 0; j = 0; k = 0
        # Siralanan listeler tek bir listede sirali 
        # bir sekilde birlestirilir.
        while i < n1 and j < n2:
            if arr1[i][0] < arr2[j][0]:
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

# Harcanan zamana ve işlerin agirligina gore optimum
# cost'u bulur.
def scheduling(times, weights):
    ratios = [] # times/weights oranini tutar.
    totalCost = 0
    currentTime = 0 # Her cost hesabindan sonra zaman guncellenir.
    
    # Listelerdeki tum oranlar ve bunlarin indeksleri
    # iki boyutlu bir diziye atanir.
    for i in range(0, len(times)):
        x = []
        x.append(times[i] / weights[i])
        x.append(i)
        ratios.append(x)
    
    # Oranlarin ve indekslerin tutuldugu iki boyutlu liste
    # mergesort ile siralanir.
    mergeSort(ratios)
    
    # Artan sirayla siralanan listeden toplam cost bulunur.
    for x in ratios:
        i = x[1] # Ratio listesinden degerin indeksi bulunur.
        # Her defasinda zaman guncellenerek isleme dahil edilir.
        currentTime += times[i]
        totalCost += currentTime * weights[i]
        print("time", i+1, " = ", currentTime, 
              ", weight", i+1, " = ", weights[i], 
              ", cost", i+1, " = ", currentTime * weights[i], sep="")
    
    print("Total cost: ", totalCost)
    
    return totalCost

scheduling(times, weights)