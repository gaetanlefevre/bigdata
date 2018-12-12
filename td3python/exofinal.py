import random

motCible = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

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
    return (valeurDistance, distanceMin)

def init_generation(nbre_indiv, long_mot):
    population = []
    for i in range(nbre_indiv):
        individu = []
        for y in range(long_mot):
            individu.append(random.randint(0,255))
        population.append(''.join(chr(w) for w in individu))
    return population

def mutate(mot_apres_croisement):
    # frequence : 0 - 1
    frequence = 0.75
    # force : cb de characteres a changer (0 - 1) soit len(mot) * force = nb de charac a changer
    force = 0.25
    if (random.randrange(0.0, 1.0) <= frequence):
        charToChange = []
        for i in range(int(len(mot_apres_croisement) * force)):
            charToChange.append(random.randint(0, len(mot_apres_croisement)))
        word = ""
        for i in range(len(mot_apres_croisement)):
            if(i in charToChange):
                word += chr(random.randint(0,255))
            else:
                word+=mot_apres_croisement[i]
        return word
    else:
        return mot_apres_croisement

def croisement(mot1 ,mot2):
    idx = random.randint(0 , len(mot1)-1)
    out = ""
    for i in range(len(mot1)):
        if (i >= idx):
            out+=mot2[i]
        else:
            out+=mot1[i]
    return out

def new_generation(liste_mots, meilleur_mot):
    nouvelleGeneration = [meilleur_mot]
    indexBestWord = liste_mots.index(meilleur_mot)
    for i in range(len(liste_mots)):
        if (i != indexBestWord):
            nouvelIndividu = croisement(liste_mots[i], liste_mots[random.randint(0, len(liste_mots) - 1)])
            nouvelIndividu = mutate(nouvelIndividu)
            nouvelleGeneration.append(nouvelIndividu)
    return nouvelleGeneration

def init_new_generation(liste_mots, meilleur_mot):
    nouvelleGeneration = [meilleur_mot]
    for i in range(len(liste_mots)):
        nouvelIndividu = croisement(liste_mots[i], liste_mots[random.randint(0, len(liste_mots) - 1)])
        nouvelIndividu = mutate(nouvelIndividu)
        nouvelleGeneration.append(nouvelIndividu)
    result_get_best = get_best(nouvelleGeneration, motCible)
    while(result_get_best[1] > 0):
        nouvelleGeneration = new_generation(nouvelleGeneration, result_get_best[0])
        print(result_get_best[0], get_distance(result_get_best[0], motCible))
        result_get_best = get_best(nouvelleGeneration, motCible)
    return nouvelleGeneration

randGeneration = init_generation(5, len(motCible))
result_get_best1 = get_best(randGeneration, motCible)
print init_new_generation(randGeneration, result_get_best1[0])