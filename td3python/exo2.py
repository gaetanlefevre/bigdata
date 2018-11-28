listeDeMots = ['COjsy OfUkp', 'Hemlo Wohld', "Hello Worp"]

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

get_best(listeDeMots, 'Hello World')