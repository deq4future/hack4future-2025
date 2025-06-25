import random

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

# Tria tema
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

# Tria dificultat
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

def unidecode(com_vulguis):
    if com_vulguis == "à":
        return "a"
    return com_vulguis

# Inicialització variables
paraula = random.choice(temes[tema])
paraula_sense_accents = unidecode(paraula)
lletres_endevinades = []
intents = intents_max
puntuacio = 0

print(f"\nTema seleccionat: {tema.capitalize()} | Dificultat: {dif}")
print("Pots escriure 'rendició' per abandonar o intentar endevinar tota la paraula.")
print("__ " * len(paraula))

game_id, seed = enviaInici()

while intents > 0:
    index_penjat = intents_max - intents
    index_penjat = min(index_penjat, len(penjat_dibuix) - 1)
    print(penjat_dibuix[index_penjat])

    paraula_actual = ""
    for i, l in enumerate(paraula):
        if unidecode(l) in [unidecode(x) for x in lletres_endevinades]:
            paraula_actual += l + " "
        else:
            paraula_actual += "__ "
    print("Paraula:", paraula_actual)
    print(f"Puntuació actual: {puntuacio}")
    print(f"Intents restants: {intents}")

    if "__" not in paraula_actual:
        print("🎉 Felicitats! Has endevinat la paraula!")
        puntuacio += 50
        break

    entrada = input("Escriu una lletra, la paraula sencera o 'rendició': ").lower()

    if entrada == "rendició":
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

    lletra = entrada
    lletra_normalitzada = unidecode(lletra)

    if lletra_normalitzada in [unidecode(x) for x in lletres_endevinades]:
        print("ℹ️ Ja has provat aquesta lletra.")
        continue

    lletres_endevinades.append(lletra)

    if lletra_normalitzada in paraula_sense_accents:
        puntuacio += 10
        print(f"✅ Bona! +10 punts.")
    else:
        intents -= 1
        puntuacio -= penalitzacio_fallada
        print(f"❌ La lletra no és a la paraula. Et queden {intents} intents. -{penalitzacio_fallada} punts.")

    puntuacio = max(0, puntuacio)  # Evitar puntuació negativa

    if intents == 0:
        print(penjat_dibuix[-1])
        print(f"💀 Has perdut! La paraula era: {paraula}")

print(f"🎯 Puntuació final: {puntuacio}")
