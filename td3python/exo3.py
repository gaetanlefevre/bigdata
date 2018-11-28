import random

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
    print('Distance du mot le plus proche', distanceMin)
    print('Valeur du mot le plus proche', valeurDistance)

def init_generation(nbre_indiv, long_mot):
    population = []
    for i in range(nbre_indiv):
        individu = []
        for y in range(long_mot):
            individu.append(random.randint(65,122))
        population.append(''.join(chr(w) for w in individu))
    return get_best(population, 'Hello World')

init_generation(5, 11)

