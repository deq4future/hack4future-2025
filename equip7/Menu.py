import requests
import os
import json
import time
import threading
import random

NOM_FITXER = "jugador.json"
POST_URL = "https://fun.codelearn.cat/hackathon/game/store_progress"


enviant_progres = False

def mostrar_menu():
    print("\n SCAPE ROOM")
    print("\n MENÚ PRINCIPAL")
    print("1. Nova partida")
    print("2. Continuar")
    print("3. Sortir")

    opcio = input("Selecciona una opció (1-3): ")
    return opcio

def enviar_progress(game_id, dades_partida):
    cos = {
        "game_id": game_id,
        "data": dades_partida
    }
    try:
        resposta = requests.post(POST_URL, json=cos)
        if resposta.status_code == 200:
            print(f"")

    except requests.exceptions.RequestException as e:
        print(f" Error de connexió enviant progrés: {e}")
        

def loop_enviar_progress(game_id):
    
    global enviant_progres
    enviant_progres = True

    while enviant_progres:
        
        if os.path.exists(NOM_FITXER):
            with open(NOM_FITXER, "r") as f:
                dades_partida = json.load(f)
        else:
            dades_partida = {}

        enviar_progress(game_id, dades_partida)

        
        espera = random.randint(5, 10)
        time.sleep(espera)

def iniciar_nova_partida():
    nom = input(" Introdueix el teu nom: ").strip()
    print(f"\n Iniciant nova partida per {nom}...")
    
    

    dades_jugador = {
        "nom": nom,
        "punts": 0,
        "nivell": 1
    }

    
    with open(NOM_FITXER, "w") as f:
        json.dump(dades_jugador, f)

    url = "https://fun.codelearn.cat/hackathon/game/new"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dades = resposta.json()
            print(" Nova partida iniciada correctament.")
            
            mostrar_historia(nom)

            
            game_id = dades.get("game_id")
            if not game_id:
                game_id = 999999

            
            fil = threading.Thread(target=loop_enviar_progress, args=(game_id,), daemon=True)
            fil.start()

             

            
            global enviant_progres
            enviant_progres = False
            fil.join()

        else:
            print(f"Error en iniciar la partida. Codi: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" Error de connexió: {e}")
        

def continuar_partida():
    if not os.path.exists(NOM_FITXER):
        print("No hi ha cap partida guardada. Comença una nova partida primer.")
        return

    with open(NOM_FITXER, "r") as f:
        dades_jugador = json.load(f)

    print(f"\nContinuant partida per {dades_jugador['nom']}...")
    print(f"Punts: {dades_jugador.get('punts', 0)}")
    print(f"Nivell: {dades_jugador.get('nivell', 1)}")

def mostrar_historia(nom):
    historia = f"""
    Un dia {nom} estava acampant amb els seus amics al bosc. Tots van decidir anar a explorar, però  {nom} es va perdre.
    Va trobar una petita casa de fusta i va decidir entra a buscar ajuda.
   Va picar a la porta, però va veure que era oberta.
    Va entrar amb una mica de por.
   Tot era fosc, i just quan va posar els dos peus a dins, la porta es va tancar a la seva esquena.
    I, ara tu tens que ajudar a {nom} a sortir d'aquí. Bona sort! 
    """
    
    print(historia)

def main():
    accio = mostrar_menu()

    if accio == "1":
        iniciar_nova_partida()
    elif accio == "2":
        continuar_partida()
    elif accio == "3":
        print("Fins la propera!")
    else:
        print("Opció no vàlida.")

if __name__ == "__main__":
    main()
