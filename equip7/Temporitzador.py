import threading
import time
import sys

temps_acabat = False
resposta_correcta = False
joc_acabat = False
score = 0

def compte_enrere(segs):
    global temps_acabat, joc_acabat
    for i in range(segs, 0, -1):
        if joc_acabat:
            return
        sys.stdout.write(f"\r⏳ Temps restant: {i} segons ")
        sys.stdout.flush()
        time.sleep(1)
    temps_acabat = True
    sys.stdout.write("\r⏰ Temps acabat!               \n")
    sys.stdout.flush()

def problema1():
    global score, temps_acabat, resposta_correcta, joc_acabat

    while True:  # Bucle per poder repetir el problema
        temps_acabat = False
        resposta_correcta = False
        joc_acabat = False

        print("""
Mires al teu voltant.
Les parets són de fusta i, just al teu davant hi ha una pissarra amb operacions matemàtiques i un problema:
Quin és el resultat de fer la meitat del doble de 12, més 8, dividit per 4?
Tens 10 segons per respondre!
""")

        thread_temporitzador = threading.Thread(target=compte_enrere, args=(10,), daemon=True)
        thread_temporitzador.start()

        while not temps_acabat and not resposta_correcta:
            resposta = input("Resposta: ").strip()
            if temps_acabat:
                break
            if resposta == "5":
                print("✅ Molt bé, ho has aconseguit!")
                score += 3
                resposta_correcta = True
                joc_acabat = True
            else:
                print("❌ Incorrecte! Torna-ho a intentar!")

        if resposta_correcta:
            print("Passes a la següent sala")
            break  # surt del bucle i acaba el problema
        else:
            print("❗ Temps exhaurit. No has pogut escapar d’aquesta sala.")
            # Preguntar si vol repetir o sortir
            opcio = input("Vols tornar a començar el problema? (s/n): ").strip().lower()
            if opcio != "s":
                print("Sortint del joc...")
                joc_acabat = True
                break

problema1()
