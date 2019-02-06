# Hw04-part2
# Islam Goktan Selcuk
# 141044071

s = "itwasthebestoftimes"

dict = {'it' : True,
        'was' : True,
        'were' : False,
        'the' : True,
        'best' : True, 
        'of' : True,
        'ads': False,
        'times' : True}

# Verilen dictionary'ye gore string'in valid kelimeler ile
# kurulan bir cumle olup olmadigi kontrol edilir.
def isSentenceValid(sentence, dict):
    n = len(sentence)
    # Sentence icerisindeki kelimelerin son
    # indeksi listenin aynı indeksine True olarak kaydedilir.
    validIndexes = [False] * (n)

    # String'in ilk valid kelimesi bulunarak,
    # bulundugu indeks True olarak isaretlenir.
    for i in range(0, n):   
        if s[:i+1] in dict:
            if dict[s[:i+1]]:
                validIndexes[i] = True

    for i in range(0, n):
        for j in range(0, i):
            if s[j+1:i+1] in dict:
                # Sentence'in j indeksine kadar olan kisminin valid olup
                # olmadigi ve j ile i arasindaki string'in dictionary'de olup
                # olmadigi kontrol edilir.
                if validIndexes[j] and dict[s[j+1:i+1]]:
                    # Eger verilen aralikta bir kelime varsa listede True 
                    # olarak isaretlenir.
                    validIndexes[i] = True
    
    print("Words' Last Indexes: ", end=" ")
    
    for i in range(0, n):
        if validIndexes[i] == True:
            print(i, end=" ")
    print()

    if validIndexes[n-1]:
        print("The sentence is valid.")
    else: print("It is not valid!")


isSentenceValid(s, dict)