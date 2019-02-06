'''
Algoritma her defasinda n'yi m kadar ya da 1 tane azaltır. 
Bu durumda recursive cagri n/m ile n arasinda bir deger kadar yapilmis olur.
Yani algoritmanın calışma zamanı linear olur.
T(n) = O(n)'dir.

'''
def gameOfNim(n, m, move):
    # Eger n m'ye eşit veya kucukse
    # oyunu o sıradaki oyuncu kazanir.
    if n <= m or n == 1:
        return move
    # Kullanici bir sonraki adim kazanmak icin 
    # 1 tane tas alir.
    elif n < 2*m and n > m:
        return gameOfNim(n-1, m, move+1)
    # Aksi durumda m tane tas alir.
    else:
        return gameOfNim(n-m, m, move+1)          
# n: toplam tas sayisi
# m: kullanicinin alabildigi maksimum tas sayisi
def nim(n, m):
    # Toplam hamle sayisina gore kazanan belirlenir.
    total_move = gameOfNim(n, m, 0)
    
    if total_move % 2 == 1:
        print("Winner is Player 2.")
    else:
        print("Winner is Player 1.")
        
nim(5, 3)