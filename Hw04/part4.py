# Hw04-part4
# Islam Goktan Selcuk
# 141044071

people = ["Alice", "whiteRabbit", "madHatter", "cheshireCat", 
          "Queen", "jabberwock", "mouse", "duck", "king", "violet",
         "lion", "frog", "fawn"]
relations = [
               [ [1, 2], [1, 3], [1, 4], [1, 5], [1, 9], [1, 10] ],
               [ [2, 1], [2, 13], [2, 3] ],
               [ [3, 1], [3, 4], [3, 2], [3, 5], [3, 8] ],
               [ [4, 1], [4, 2], [4, 3], [4, 7], [4, 12] ],                   
               [ [5, 1], [5, 2], [5, 3], [5, 4], [5, 6] ],
               [ [6, 1] ],
               [ [7, 1] ],
               [ [8, 1] ],
               [ [9, 1] ],
               [ [10, 1] ],
               [ [11, 1] ],
               [ [12, 1] ],
               [ [13, 1] ]
            ]

# Insanlarin tanidiklari ve tanimadiklari insan sayisina gore 
# partiye katilacak insanlari belirler.
def planningAParty(people, relations):
    n = len(people)
    friends = [0] * n
    strangers = [0] * n
    invitedList = []

    # Her kisinin kac tane tanidigi ve tanimadigi
    # oldugunu kaydederek listeye ekler.
    for i in range(0, n):
        friends[i] = len(relations[i])
        strangers[i] = n - (friends[i] + 1)
        # Kosulu saglayanlar incitedList'e kaydedilir.
        if friends[i] >= 5 and strangers[i] >= 5:
            invitedList.append(people[i])
        

    print(friends)
    print(strangers)
    print(invitedList)

planningAParty(people, relations)