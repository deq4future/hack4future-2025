import random
import urllib.request
import json
from datetime import datetime

def unidecode(c):
    return (
        c.replace("à", "a").replace("á", "a").replace("â", "a").replace("ä", "a")
         .replace("è", "e").replace("é", "e").replace("ê", "e").replace("ë", "e")
         .replace("í", "i").replace("ï", "i").replace("î", "i")
         .replace("ò", "o").replace("ó", "o").replace("ô", "o").replace("ö", "o")
         .replace("ù", "u").replace("ú", "u").replace("ü", "u").replace("û", "u")
         .replace("ç", "c").replace("ñ", "n")
    )

def inicia_partida():
    url = "https://fun.codelearn.cat/hackathon/game/new"
    try:
        with urllib.request.urlopen(url) as resposta:
            dades = json.load(resposta)
            game_id = dades.get("game_id")
            seed = dades.get("seed")
            if game_id and seed:
                print("🎮 Partida iniciada correctament!")
                return game_id, seed
            else:
                print("⚠️ La resposta no conté 'game_id' o 'seed'.")
    except Exception as e:
        print("❌ Error en la petició:", e)
    return None, None

def notifica_partida(game_id, lletra, intents, puntuacio):
    url = "https://fun.codelearn.cat/hackathon/game/new"
    dades = {
        "game_id": game_id,
        "lletra": lletra,
        "intents": intents,
        "puntuacio": puntuacio
    }
    try:
        # Codificar les dades en format JSON
        dades_codificades = json.dumps(dades).encode('utf-8')

        # Realitzar la petició POST
        req = urllib.request.Request(url, data=dades_codificades, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as resposta:
            resposta_json = json.load(resposta)
            print(f"Resposta del servidor: {resposta_json}")
    except Exception as e:
        print(f"Error en la petició POST: {e}")

def finalitza_partida(game_id, puntuacio):
    url = "https://fun.codelearn.cat/hackathon/game/finalize"
    data = {
        "game_id": game_id,
        "data": datetime.now().isoformat(),
        "score": puntuacio
    }
    try:
        # Codificar les dades en format JSON
        dades_codificades = json.dumps(data).encode('utf-8')

        # Realitzar la petició POST per finalitzar el joc
        req = urllib.request.Request(url, data=dades_codificades, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as resposta:
            resposta_json = json.load(resposta)
            print(f"Resposta del servidor (finalització): {resposta_json}")
    except Exception as e:
        print(f"Error en la petició POST de finalització: {e}")

penjat_dibuix = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

temes = {
    "animals": ["gat", "gos", "elefant", "cavall", "lloro", "tigre"],
    "fruites": ["poma", "plàtan", "maduixa", "kiwi", "raïm", "síndria"],
    "tecnologia": ["ordinador", "internet", "pantalla", "teclat", "programació"],
    "esports": ["futbol", "bàsquet", "tennis", "natació", "atletisme"],
}

llista_temes = list(temes.keys())

print("🎮 Benvingut/da al joc del penjat amb temes, dificultat i puntuació!")
print("Pots escriure el número o el nom del tema:")
for i, t in enumerate(llista_temes, 1):
    print(f"{i}. {t.capitalize()}")

tema = ""
while True:
    entrada = input("Escull un tema (número o nom): ").lower()
    if entrada.isdigit():
        index = int(entrada) - 1
        if 0 <= index < len(llista_temes):
            tema = llista_temes[index]
            break
    elif entrada in temes:
        tema = entrada
        break
    print("Entrada no vàlida. Torna-ho a provar.")

print("\nTria dificultat:")
print("1. Fàcil (10 intents, -3 punts per error)")
print("2. Mitjà (6 intents, -5 punts per error)")
print("3. Difícil (4 intents, -8 punts per error)")

intents_max = 6
penalitzacio_fallada = 5

while True:
    dif = input("Escull dificultat (1, 2 o 3): ")
    if dif == "1":
        intents_max = 10
        penalitzacio_fallada = 3
        break
    elif dif == "2":
        intents_max = 6
        penalitzacio_fallada = 5
        break
    elif dif == "3":
        intents_max = 4
        penalitzacio_fallada = 8
        break
    else:
        print("Dificultat no vàlida, torna-ho a provar.")
game_id, seed = inicia_partida()
random.seed(seed)
paraula = random.choice(temes[tema])
paraula_sense_accents = unidecode(paraula)
lletres_endevinades = []
intents = intents_max
puntuacio = 0

print(f"\nTema seleccionat: {tema.capitalize()} | Dificultat: {dif}")
print("Pots escriure 'rendició' per abandonar o intentar endevinar tota la paraula.")
print("__ " * len(paraula))

while intents > 0:
    index_penjat = min(intents_max - intents, len(penjat_dibuix) - 1)
    print(penjat_dibuix[index_penjat])

    paraula_actual = ""
    lletres_endevinades_normalitzades = [unidecode(x) for x in lletres_endevinades]

    for i, l in enumerate(paraula):
        if unidecode(l) in lletres_endevinades_normalitzades:
            paraula_actual += l + " "
        else:
            paraula_actual += "__ "

    print("Paraula:", paraula_actual)
    print(f"Puntuació actual: {puntuacio}")
    print(f"Intents restants: {intents}")

    if "__" not in paraula_actual:
        print(f"🎉 Felicitats! Has completat correctament la paraula: {paraula}")
        puntuacio += 50
        break

    entrada = input("Escriu una lletra, la paraula sencera o 'rendició': ").lower()

    if unidecode(entrada) == "rendicio":
        print(penjat_dibuix[-1])
        print("\n🚪 T'has rendit.")
        print(f"La paraula era: {paraula}")
        break

    if not entrada.isalpha():
        print("⚠️ Entrada invàlida. Escriu només lletres.")
        continue

    entrada_normalitzada = unidecode(entrada)

    if len(entrada) > 1:
        if entrada_normalitzada == paraula_sense_accents:
            puntuacio += 50
            print("🎉 Has encertat la paraula sencera! Molt bé!")
            break
        else:
            intents -= 1
            puntuacio -= 20
            print(f"❌ No és la paraula correcta. Et queden {intents} intents.")
            continue

    lletra_normalitzada = entrada_normalitzada
    if lletra_normalitzada in lletres_endevinades_normalitzades:
        print("ℹ️ Ja has provat aquesta lletra.")
        continue

    lletres_endevinades.append(entrada)

    if lletra_normalitzada in paraula_sense_accents:
        puntuacio += 10
        print("✅ Bona! +10 punts.")
    else:
        intents -= 1
        puntuacio -= penalitzacio_fallada
        print(f"❌ La lletra no és a la paraula. Et queden {intents} intents. -{penalitzacio_fallada} punts.")

    puntuacio = max(0, puntuacio)

    # Notificar el servidor després de cada intent
    notifica_partida(game_id, entrada, intents, puntuacio)

    if intents == 0:
        print(penjat_dibuix[-1])
        print(f"💀 Has perdut! La paraula era: {paraula}")
        break

# Notificar al final de la partida
finalitza_partida(game_id, puntuacio)

print(f"🎯 Puntuació final: {puntuacio}")
print(f"🔐 Game ID: {game_id} | Seed: {seed}")
print("Gràcies per jugar! Fins la propera!")
