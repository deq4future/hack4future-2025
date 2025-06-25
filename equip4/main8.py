import random
import urllib.request
import json
import time
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
                return game_id, seed
    except:
        pass
    return None, None

def notifica_partida(game_id, lletra, intents, puntuacio, lletres_endevinades, lletres_fallades):
    url = "https://fun.codelearn.cat/hackathon/game/store_progress"
    dades = {
        "game_id": game_id,
        "data" : {
            "lletra": lletra,
            "intents": intents,
            "puntuacio": puntuacio,
            "lletres_endevinades": lletres_endevinades,
            "lletres_fallades": lletres_fallades
        }
    }
    try:
        dades_codificades = json.dumps(dades).encode('utf-8')
        req = urllib.request.Request(url, data=dades_codificades, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as resposta:
            pass
    except:
        pass

def finalitza_partida(game_id, puntuacio, lletres_endevinades):
    url = "https://fun.codelearn.cat/hackathon/game/finalize"
    data = {
        "game_id": game_id,
        "data" : {
            "lletres_probades": lletres_endevinades
        },
        "score": puntuacio
    }
    try:
        dades_codificades = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=dades_codificades, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as resposta:
            pass
    except:
        pass

def mostra_penjat(intents_restants, intents_max, dibuix_penjat, textos):
    clear_screen()
    print(f"{Colors.HEADER}{Colors.BOLD}{textos['intents_restants']}: {intents_restants} / {intents_max} {'🔴'*intents_restants}{Colors.ENDC}\n")
    index = min(intents_max - intents_restants, len(dibuix_penjat) - 1)
    print(dibuix_penjat[index])

def mostra_paraula(paraula, lletres_endevinades, textos):
    lletres_norm = [unidecode(l) for l in lletres_endevinades]
    mostrada = ""
    for l in paraula:
        if unidecode(l) in lletres_norm:
            mostrada += f"{Colors.OKGREEN}{Colors.BOLD}{l.upper()}{Colors.ENDC} "
        else:
            mostrada += f"{Colors.WARNING}__{Colors.ENDC} "
    print("\n" + textos["paraula"] + ": " + mostrada + "\n")

def escull_idioma(idiomas, textos):
    print(f"{Colors.BOLD}{Colors.OKCYAN}{textos['idiomas_disponibles']}{Colors.ENDC}")
    llista_idiomes = list(idiomas.keys())
    for i, idi in enumerate(llista_idiomes, 1):
        print(f"  {Colors.OKBLUE}{i}. {idi.capitalize()}{Colors.ENDC}")
    while True:
        entrada = input(f"\n{Colors.BOLD}{textos['escoge_idioma']}{Colors.ENDC}").lower().strip()
        if entrada.isdigit():
            index = int(entrada) - 1
            if 0 <= index < len(llista_idiomes):
                return llista_idiomes[index]
        elif entrada in idiomas:
            return entrada
        print(f"{Colors.FAIL}{textos['entrada_no_valida']}{Colors.ENDC}")

def escull_dificultat(textos):
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}{textos['escoge_dificultad']}{Colors.ENDC}")
    print(f"  {Colors.OKBLUE}1. {textos['facil']}    (10 {textos['intentos']}, -3 {textos['puntos_error']}){Colors.ENDC}")
    print(f"  {Colors.WARNING}2. {textos['medio']}    (6 {textos['intentos']}, -5 {textos['puntos_error']}){Colors.ENDC}")
    print(f"  {Colors.FAIL}3. {textos['dificil']}  (4 {textos['intentos']}, -8 {textos['puntos_error']}){Colors.ENDC}")
    while True:
        dif = input(f"{Colors.BOLD}{textos['selecciona_dificultad']}{Colors.ENDC}")
        if dif == "1":
            return 10, 3, textos['facil']
        elif dif == "2":
            return 6, 5, textos['medio']
        elif dif == "3":
            return 4, 8, textos['dificil']
        else:
            print(f"{Colors.FAIL}{textos['opcion_no_valida']}{Colors.ENDC}")


def main():
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

    idiomas = {
        "català": {
            "animals": ["gat", "gos", "elefant", "cavall", "lloro", "tigre"],
            "fruites": ["poma", "plàtan", "maduixa", "kiwi", "raïm", "síndria"],
            "tecnologia": ["ordinador", "internet", "pantalla", "teclat", "programació"],
            "esports": ["futbol", "bàsquet", "tennis", "natació", "atletisme"],
        },
        "español": {
            "animales": ["gato", "perro", "elefante", "caballo", "loro", "tigre"],
            "frutas": ["manzana", "plátano", "fresa", "kiwi", "uva", "sandía"],
            "tecnología": ["ordenador", "internet", "pantalla", "teclado", "programación"],
            "deportes": ["fútbol", "baloncesto", "tenis", "natación", "atletismo"],
        },
        "english": {
            "animals": ["cat", "dog", "elephant", "horse", "parrot", "tiger"],
            "fruits": ["apple", "banana", "strawberry", "kiwi", "grape", "watermelon"],
            "technology": ["computer", "internet", "screen", "keyboard", "programming"],
            "sports": ["football", "basketball", "tennis", "swimming", "athletics"],
        }
    }

    textos_por_idioma = {
        "català": {
            "intents_restants": "INTENTS RESTANTS",
            "paraula": "PARAULA",
            "idiomas_disponibles": "IDIOMES DISPONIBLES",
            "escoge_idioma": "Escull un idioma (número o nom): ",
            "entrada_no_valida": "Entrada no vàlida, intenta-ho de nou.",
            "escoge_dificultad": "ESCOGE LA DIFICULTAT",
            "facil": "Fàcil",
            "medio": "Mitjà",
            "dificil": "Difícil",
            "intentos": "intents",
            "puntos_error": "punts per error",
            "selecciona_dificultad": "Selecciona dificultat (1, 2 o 3): ",
            "opcion_no_valida": "Opció no vàlida, prova un altre cop.",
            "iniciando_partida": "Iniciant partida...",
            "partida_iniciada": "Partida iniciada correctament! A jugar!",
            "no_pudo_iniciar": "No s'ha pogut iniciar la partida. Sortint...",
            "introduce_letra_palabra": "Introdueix una lletra, la paraula completa o 'rendició': ",
            "ya_probaste": "Ja has provat aquesta lletra, intenta'n una altra.",
            "bien_letra": "Bé! La lletra està a la paraula.",
            "mal_letra": "La lletra no està a la paraula.",
            "ganaste": "Has guanyat! La paraula era",
            "palabra_correcta": "Paraula correcta! Has guanyat!",
            "palabra_incorrecta": "Paraula incorrecta.",
            "rendicion": "Has abandonat. La paraula correcta era:",
            "puntuacion": "Puntuació",
            "gracias": "Gràcies per jugar!",
            "puntuacion_final": "Puntuació final",
        },
        "español": {
            "intents_restants": "INTENTOS RESTANTES",
            "paraula": "PALABRA",
            "idiomas_disponibles": "IDIOMAS DISPONIBLES",
            "escoge_idioma": "Escoge un idioma (número o nombre): ",
            "entrada_no_valida": "Entrada no válida, intenta de nuevo.",
            "escoge_dificultad": "ESCOGE LA DIFICULTAD",
            "facil": "Fácil",
            "medio": "Medio",
            "dificil": "Difícil",
            "intentos": "intentos",
            "puntos_error": "puntos por error",
            "selecciona_dificultad": "Selecciona dificultad (1, 2 o 3): ",
            "opcion_no_valida": "Opción no válida, prueba otra vez.",
            "iniciando_partida": "Iniciando partida...",
            "partida_iniciada": "Partida iniciada correctamente! ¡A jugar!",
            "no_pudo_iniciar": "No se pudo iniciar la partida. Saliendo...",
            "introduce_letra_palabra": "Introduce una letra, la palabra completa o 'rendición': ",
            "ya_probaste": "Ya probaste esta letra, intenta otra.",
            "bien_letra": "¡Bien! La letra está en la palabra.",
            "mal_letra": "La letra no está en la palabra.",
            "ganaste": "¡Has ganado! La palabra era",
            "palabra_correcta": "¡Palabra correcta! ¡Has ganado!",
            "palabra_incorrecta": "Palabra incorrecta.",
            "rendicion": "Has abandonado. La palabra correcta era:",
            "puntuacion": "Puntuación",
            "gracias": "¡Gracias por jugar!",
            "puntuacion_final": "Puntuación final",
        },
        "english": {
            "intents_restants": "REMAINING ATTEMPTS",
            "paraula": "WORD",
            "idiomas_disponibles": "AVAILABLE LANGUAGES",
            "escoge_idioma": "Choose a language (number or name): ",
            "entrada_no_valida": "Invalid input, try again.",
            "escoge_dificultad": "CHOOSE DIFFICULTY",
            "facil": "Easy",
            "medio": "Medium",
            "dificil": "Hard",
            "intentos": "attempts",
            "puntos_error": "points per mistake",
            "selecciona_dificultad": "Select difficulty (1, 2 or 3): ",
            "opcion_no_valida": "Invalid option, try again.",
            "iniciando_partida": "Starting game...",
            "partida_iniciada": "Game started successfully! Let's play!",
            "no_pudo_iniciar": "Couldn't start the game. Exiting...",
            "introduce_letra_palabra": "Enter a letter, the full word or 'give up': ",
            "ya_probaste": "You already tried that letter, try another.",
            "bien_letra": "Good! The letter is in the word.",
            "mal_letra": "The letter is not in the word.",
            "ganaste": "You won! The word was",
            "palabra_correcta": "Correct word! You won!",
            "palabra_incorrecta": "Incorrect word.",
            "rendicion": "You gave up. The correct word was:",
            "puntuacion": "Score",
            "gracias": "Thanks for playing!",
            "puntuacion_final": "Final score",
        }
    }

    clear_screen()
    print(f"{Colors.OKCYAN}{Colors.BOLD}=======================================")
    print("        🎉 HANGMAN GAME / JOC DEL PENJAT 🎉")
    print("=======================================\n" + Colors.ENDC)

    idioma = escull_idioma(idiomas, textos_por_idioma["español"])  # Para el selector idioma siempre en español
    textos = textos_por_idioma[idioma]
    temes = idiomas[idioma]

    print(f"\n{Colors.BOLD}{textos['iniciando_partida']}{Colors.ENDC}")
    time.sleep(1.2)
    game_id, seed = inicia_partida()
    if not game_id or not seed:
        print(f"{Colors.FAIL}{textos['no_pudo_iniciar']}{Colors.ENDC}")
        return

    intents_max, penalitzacio_fallada, dif_nom = escull_dificultat(textos)

    random.seed(seed)
    paraula = random.choice(temes[random.choice(list(temes.keys()))])
    paraula_sense_accents = unidecode(paraula)

    lletres_endevinades = []
    lletres_fallades = []
    intents = intents_max
    puntuacio = 0

    while intents > 0:
        mostra_penjat(intents, intents_max, penjat_dibuix, textos)
        mostra_paraula(paraula, lletres_endevinades, textos)

        print(f"{Colors.BOLD}{textos['puntuacion']}: {puntuacio}{Colors.ENDC}")
        resposta = input(textos["introduce_letra_palabra"]).lower().strip()

        if resposta == "rendició" or resposta == "rendicion" or resposta == "give up":
            print(f"{Colors.FAIL}{textos['rendicion']} {paraula}{Colors.ENDC}")
            finalitza_partida(game_id, puntuacio, lletres_endevinades)
            break

        if len(resposta) == 1:  # letra
            lletra = resposta
            if lletra in lletres_endevinades or lletra in lletres_fallades:
                print(f"{Colors.WARNING}{textos['ya_probaste']}{Colors.ENDC}")
                time.sleep(1.2)
                continue

            if lletra in paraula_sense_accents:
                lletres_endevinades.append(lletra)
                puntuacio += 1
                print(f"{Colors.OKGREEN}{textos['bien_letra']}{Colors.ENDC}")
            else:
                intents -= 1
                puntuacio -= penalitzacio_fallada
                lletres_fallades.append(lletra)
                print(f"{Colors.FAIL}{textos['mal_letra']}{Colors.ENDC}")

            notifica_partida(game_id, lletra, intents, puntuacio, lletres_endevinades, lletres_fallades)
        else:  # intento de palabra completa
            if unidecode(resposta) == paraula_sense_accents:
                print(f"{Colors.OKGREEN}{textos['palabra_correcta']}{Colors.ENDC}")
                puntuacio += 10
                finalitza_partida(game_id, puntuacio, lletres_endevinades)
                break
            else:
                print(f"{Colors.FAIL}{textos['palabra_incorrecta']}{Colors.ENDC}")
                intents -= 1
                puntuacio -= penalitzacio_fallada
                notifica_partida(game_id, None, intents, puntuacio, lletres_endevinades, lletres_fallades)

        # Comprova si ha guanyat (totes les lletres descobertes)
        if all(unidecode(l) in lletres_endevinades for l in paraula):
            print(f"{Colors.OKGREEN}{textos['ganaste']} {paraula}{Colors.ENDC}")
            finalitza_partida(game_id, puntuacio, lletres_endevinades)
            break

        time.sleep(1.1)

    print(f"\n{Colors.BOLD}{Colors.OKCYAN}{textos['puntuacion_final']}: {puntuacio}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}{textos['gracias']}{Colors.ENDC}")

if __name__ == "__main__":
    main()
