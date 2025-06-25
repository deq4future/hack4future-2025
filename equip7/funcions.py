score = 0 
def problema1():
    global score
    print("La meitat del doble de 12, més 8, dividit per 4.")
    resposta = input("Resposta: ")
    if resposta == "5":
        print("Molt bé, ho has aconseguit!")
        score += 3
    else:
        while resposta != "5":
            print("Torna a intentar!")
            print("La meitat del doble de 12, més 8, dividit per 4.")
            resposta = input("Resposta: ")
        print("Molt Bé")
        score += 1
    print("Passes a la següent sala")

import random

def problema2():
    global score
    print("En aquesta segona sala hauràs de descobrir quina és la paraula amagada")
    pistes = [
        "Comença amb la lletra 'o'.",
        "Té la lletra 'b' al mig.",
        "Acaba amb la lletra 'a'.",
        "Es relaciona amb la llum i la foscor.",    
    ]
    print("Sóc una paraula de 5 lletres.")
    print("Si treus la primera lletra, encara so com abans.")
    print("Si treus la segona lletra, també.")
    print("Fins i tot si només queda una lletra, la paraula segueix sent la mateixa.")
    print("Quina paraula sóc?")
    
    resposta = input("Resposta: ")
    intents = 1
    while resposta.lower() != "ombra":
        if len(pistes) > 0:
            pista = random.choice(pistes)
            print("Pista:", pista)
            pistes.remove(pista)
        else:
            print("No hi ha més pistes disponibles")
        resposta = input("Resposta: ")
        intents += 1

    if intents == 1:
        print("Molt bé, a la primera!")
        score += 3
    else:
        print("Molt bé, passes a la següent sala!")
        score += 1

def problema3():
    global score
    print("Heu entrat a la sala d'història")
    
    resposta = input("Sabeu quin any es ve descobrir Amèrica, quin? ")
    intents = 1
    while resposta != "1492":
        print("Torna a intentar!")
        resposta = input("Resposta: ")
        intents += 1
    if intents == 1:
        print("Tu no seràs un expert en història, no?")
        score += 3
    else:
        print("Molt Bé")
        score += 1
    respostaf = input("Quin any va ser la revolució francesa? ")
    intents = 1
    while respostaf != "1789":
        print("Torna a intentar!")
        respostaf = input("Resposta: ")
        intents += 1
    if intents == 1:
        print("Fàcil?")
        score += 3
    else:
        print("Molt Bé")
        score += 1
    print("Ara passaràs a la següent sala")

def problema4():
    global score
    print("Quin gas és el més abundant a l’atmosfera terrestre?")
    resposta = input("Resposta: ")
    if resposta in ["nitrogen", "Nitrogen", "NITROGEN"]:
        print("Mare meva que bo!")
        score += 3
        print("Passes a la ultima sala")
    else:
        while resposta not in ["nitrogen", "Nitrogen", "NITROGEN"]:
            print("Torna a intentar!")
            resposta = input("Resposta: ")
        print("Molt Bé")
        print("Passes a la última sala")
        score += 1


def problema5():
    global score
    print("Quin planeta és conegut com el planeta vermell?")
    resposta = input("Resposta: ")
    if resposta in ["mart", "Mart", "MART"]:
        print("Super Bè")
        print("Has aconseguit escapar")
        score += 3
    else:
        while resposta not in ["Mart", "MART", "mart"]:
            print("Torna a intentar!")
            resposta = input("Resposta: ")
        print("Molt Bé")
        print("Has aconseguit escapar!")
        score += 1
