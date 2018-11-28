def get_distance(mot1, mot2):
    asciiMot1 = [ord(x) for x in list(mot1)]
    asciiMot2 = [ord(x) for x in list(mot2)]
    distance = 0
    for i in range(len(asciiMot1)):
        distance+=abs(asciiMot1[i] - asciiMot2[i])
    print ("distance", distance)


get_distance('COjsy OfUkp', 'Hello World')