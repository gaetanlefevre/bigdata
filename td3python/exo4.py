import random

motCible = 'Hello World'

def get_distance(mot1, mot2):
    asciiMot1 = [ord(x) for x in list(mot1)]
    asciiMot2 = [ord(x) for x in list(mot2)]
    distance = 0
    for i in range(len(asciiMot1)):
        distance += abs(asciiMot1[i] - asciiMot2[i])
    return distance

def get_best(liste, cible):
    distanceMin = get_distance(liste[0], cible)
    valeurDistance = liste[0]
    for mot in liste:
        if distanceMin > get_distance(mot, cible):
            distanceMin = get_distance(mot, cible)
            valeurDistance = mot
    return valeurDistance

def init_generation(nbre_indiv, long_mot):
    population = []
    for i in range(nbre_indiv):
        individu = []
        for y in range(long_mot):
            individu.append(random.randint(65,122))
        population.append(''.join(chr(w) for w in individu))
    return population

def new_generation(liste_mots, meilleur_mot):
    lettres = ''.join(liste_mots)
    lettres+=meilleur_mot
    myList = []
    for char in lettres:
        myList.append(char)
    nouvelleGeneration = []
    for i in range(len(liste_mots)):
        nouvelIndividu = ''
        for y in range(len(liste_mots[0])):
            nouvelIndividu+=random.choice(myList)
        nouvelleGeneration.append(nouvelIndividu)
    return nouvelleGeneration

def init_new_generation(liste_mots, meilleur_mot):
    lettres = ''.join(liste_mots)
    lettres+=meilleur_mot
    myList = []
    for char in lettres:
        myList.append(char)
    nouvelleGeneration = []
    for i in range(len(liste_mots)):
        nouvelIndividu = ''
        for y in range(len(liste_mots[0])):
            nouvelIndividu+=random.choice(myList)
        nouvelleGeneration.append(nouvelIndividu)
    for i in range(200):
        nouvelleGeneration = new_generation(nouvelleGeneration, get_best(nouvelleGeneration, motCible))
        print(get_best(nouvelleGeneration, motCible), get_distance(get_best(nouvelleGeneration, motCible), motCible))
    return nouvelleGeneration


randGeneration = init_generation(5, 11)
print init_new_generation(randGeneration, get_best(randGeneration, motCible))