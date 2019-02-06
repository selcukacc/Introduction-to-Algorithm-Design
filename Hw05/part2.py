# Hw05 - Part2
# Islam Goktan Selcuk -- 141044071

# Test inputs
ny = [1,3,20,30] # New York icin harcanan cost'lar
sf = [50,20,2,4] # San Francisco ofisinde harcanan cost'lar
movingCost = 10  # Sehir degistirildiginde harcanan cost

# Iki sehirdeki ofislerde calisarak ve sehirler arasinda
# gecis yapılarak harcanan optimum cost'u bulur.
def costOfOptimalPlan(ny, sf, movingCost):
    n = len(ny)
    totalCost = 0
    if n > 0:
        # Ilk aydaki sehir direkt karsilastirma ile bulunur.
        if sf[0] > ny[0]:
            print("NY in Month 1")
        else: print("SF in Month 1")

        # Her ay icin bulunulan sehir'in cost'u ile 
        # diger sehir'e gecis cost'u ve sehir'in cost'u toplanarak
        # karsilastirilir.
        for i in range(1, n):
            ny[i] += min(ny[i-1], movingCost + sf[i-1])
            sf[i] += min(sf[i-1], movingCost + ny[i-1])        
            # O ay icin optimum cost'un saglandigi sehir print edilir.
            if sf[i] > ny[i]:
                print("NY in Month", i+1)
            else: print("SF in Month", i+1)

        # Son indeksteki minimum cost secilir.
        totalCost = min(sf[n-1], ny[n-1])
        print("Total cost:", totalCost)
    
    return totalCost

costOfOptimalPlan(ny, sf, movingCost)