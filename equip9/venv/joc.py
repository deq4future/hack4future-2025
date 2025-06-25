from api import ServidorCodelearn 
import pygame
import random
import sys

pygame.init()
ServidorCodelearn = ServidorCodelearn()
gameid = ServidorCodelearn.iniciar_partida()
# Configuració pantalla
AMPLADA, ALCADA = 1580, 800
pantalla = pygame.display.set_mode((AMPLADA, ALCADA))
pygame.display.set_caption("Quiz de Python amb Pygame")

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
GRIS = (200, 200, 200)
GRIS_FOSC = (50, 50, 50)
BLAU = (0, 120, 215)
ROIG = (255, 0, 0)
BLAU_CLAR = (173, 216, 230)
GRIS_CLAR = (230, 230, 230)
VERD = (0, 180, 0)

# Fonts
font = pygame.font.SysFont(None, 30)
font_gran = pygame.font.SysFont(None, 48)

# Rellotge
rellotge = pygame.time.Clock()

# 100 Preguntes de Python en Català
preguntes = [
 # Preguntes tipus test - Variables i tipus de dades
 {"tipus": "test",
 "pregunta": "Quin és el tipus de dada correcte per emmagatzemar text a Python?",
 "opcions": ["int", "str", "float"],
 "resposta": "str"},

 {"tipus": "test",
 "pregunta": "Com es converteix un número a string a Python?",
 "opcions": ["string()", "str()", "convert()"],
 "resposta": "str()"},

 {"tipus": "test",
 "pregunta": "Quin operador s'usa per comprovar si dos valors són iguals?",
 "opcions": ["=", "==", "!="],
 "resposta": "=="},

 {"tipus": "test",
 "pregunta": "Com s'accedeix al primer element d'una llista a Python?",
 "opcions": ["llista[0]", "llista[1]", "llista.first()"],
 "resposta": "llista[0]"},

 {"tipus": "test",
 "pregunta": "Quin mètode s'usa per afegir un element al final d'una llista?",
 "opcions": ["add()", "append()", "insert()"],
 "resposta": "append()"},

 # Preguntes tipus acabar la línia - Variables
 {"tipus": "acabar",
 "pregunta": "Completa la línia per crear una variable anomenada 'nom' amb el valor 'Joan':",
 "codi_inici": "nom = ",
 "resposta": "'Joan'"},

  {"tipus": "acabar",
 "pregunta": "Que falta per imprimir aixo a la pantalla de sortida?",
 "codi_inici": "_____('Hola mon!')",
 "resposta": "print"},

 {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per crear un color RGB en Pygame?",
    "codi_inici": "color = pygame.Color(____, 255, 0)",
    "resposta": "255"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una classe anomenada 'Jugador' en Python?",
    "codi_inici": "____ Jugador:",
    "resposta": "class"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per carregar un so en Pygame?",
    "codi_inici": "so = pygame.mixer.____('so.wav')",
    "resposta": "Sound"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es concatenen dues cadenes de text en Python?",
    "codi_inici": "text = 'Hola' + ____",
    "resposta": "' món!'"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per reproduir un so en Pygame?",
    "codi_inici": "so.____()",
    "resposta": "play"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es crea un conjunt buit en Python?",
    "codi_inici": "conjunt = ____()",
    "resposta": "set"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per omplir una superfície amb un color en Pygame?",
    "codi_inici": "superficie.____(color)",
    "resposta": "fill"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una condició per comprovar si un valor no és igual a 10?",
    "codi_inici": "if x ____ 10:",
    "resposta": "!="
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció converteix una cadena a un nombre enter en Python?",
    "codi_inici": "nombre = ____('42')",
    "resposta": "int"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es dibuixa una línia en una superfície de Pygame?",
    "codi_inici": "pygame.draw.____(superficie, color, (x1, y1), (x2, y2))",
    "resposta": "line"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina paraula clau s'utilitza per continuar amb la següent iteració d'un bucle?",
    "codi_inici": "____",
    "resposta": "continue"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es crea una superfície nova en Pygame amb mida 200x200?",
    "codi_inici": "superficie = pygame.Surface(____)",
    "resposta": "(200, 200)"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir el valor absolut d'un nombre en Python?",
    "codi_inici": "valor = ____(-5)",
    "resposta": "abs"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es verifica si un esdeveniment és de tipus QUIT en Pygame?",
    "codi_inici": "if esdeveniment.type == pygame.____:",
    "resposta": "QUIT"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per afegir un element al final d'una llista?",
    "codi_inici": "llista.____(element)",
    "resposta": "append"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una constant per al color negre en Pygame?",
    "codi_inici": "NEGRE = ____",
    "resposta": "(0, 0, 0)"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir el temps actual en mil·lisegons en Pygame?",
    "codi_inici": "temps = pygame.time.____()",
    "resposta": "get_ticks"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix un bucle que itera sobre una llista en Python?",
    "codi_inici": "____ element in llista:",
    "resposta": "for"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per mostrar una imatge en una superfície de Pygame?",
    "codi_inici": "superficie.____(imatge, (x, y))",
    "resposta": "blit"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es calcula el mòdul (resta) d'una divisió en Python?",
    "codi_inici": "resta = 10 ____ 3",
    "resposta": "%"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir les dimensions d'una superfície en Pygame?",
    "codi_inici": "ample, alt = superficie.____()",
    "resposta": "get_size"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una variable global dins d'una funció en Python?",
    "codi_inici": "____ variable",
    "resposta": "global"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir un nombre aleatori entre 0 i 1 en Python?",
    "codi_inici": "import random\nx = random.____()",
    "resposta": "random"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es verifica si una tecla específica (per exemple, ESPAI) està premuda en Pygame?",
    "codi_inici": "if esdeveniment.type == pygame.KEYDOWN and esdeveniment.key == pygame.____:",
    "resposta": "K_SPACE"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per eliminar un element d'una llista per índex?",
    "codi_inici": "llista.____(0)",
    "resposta": "pop"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una funció que retorna un valor en Python?",
    "codi_inici": "def funcio():\n    ____ 42",
    "resposta": "return"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per dibuixar un polígon en Pygame?",
    "codi_inici": "pygame.draw.____(superficie, color, [(x1, y1), (x2, y2), (x3, y3)])",
    "resposta": "polygon"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es comprova si un element existeix en una llista?",
    "codi_inici": "if element ____ llista:",
    "resposta": "in"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir la posició actual del ratolí en Pygame?",
    "codi_inici": "x, y = pygame.mouse.____()",
    "resposta": "get_pos"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es converteix un nombre a flotant en Python?",
    "codi_inici": "nombre = ____(42)",
    "resposta": "float"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per aturar tots els sons en reproducció en Pygame?",
    "codi_inici": "pygame.mixer.____()",
    "resposta": "stop"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es crea un diccionari amb una clau 'nom' i valor 'Anna'?",
    "codi_inici": "diccionari = ____",
    "resposta": "{'nom': 'Anna'}"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir el màxim d'una llista de nombres?",
    "codi_inici": "maxim = ____(llista)",
    "resposta": "max"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es verifica si un esdeveniment és un clic del ratolí en Pygame?",
    "codi_inici": "if esdeveniment.type == pygame.____:",
    "resposta": "MOUSEBUTTONDOWN"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir el mínim d'una llista de nombres?",
    "codi_inici": "minim = ____(llista)",
    "resposta": "min"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es defineix una llista amb els valors 1, 2, 3 utilitzant una comprensió de llista?",
    "codi_inici": "llista = [x for x in ____(1, 4)]",
    "resposta": "range"
  },
  {
    "tipus": "acabar",
    "pregunta": "Quina funció s'utilitza per obtenir la font del sistema en Pygame?",
    "codi_inici": "font = pygame.font.____('Arial', 24)",
    "resposta": "SysFont"
  },
  {
    "tipus": "acabar",
    "pregunta": "Com es divideix una cadena en una llista de paraules?",
    "codi_inici": "paraules = 'Hola món'.____()",
    "resposta": "split"
  },

 # Preguntes tipus test - Funcions
 {"tipus": "test",
 "pregunta": "Quina paraula clau s'usa per retornar un valor d'una funció?",
 "opcions": ["give", "return", "output"],
 "resposta": "return"},

 {"tipus": "test",
 "pregunta": "Com s'importa tot el contingut d'un mòdul anomenat 'math'?",
 "opcions": ["import math", "from math import *", "include math"],
 "resposta": "import math"},

 # Preguntes tipus test - Estructures de dades
 {"tipus": "test",
 "pregunta": "Quin mètode s'usa per obtenir totes les claus d'un diccionari?",
 "opcions": ["keys()", "getkeys()", "allkeys()"],
 "resposta": "keys()"},

 {"tipus": "test",
 "pregunta": "Com es comprova si una clau existeix en un diccionari?",
 "opcions": ["key exists dict", "key in dict", "dict.has(key)"],
 "resposta": "key in dict"},

 # Preguntes tipus test - Excepcions
 {"tipus": "test",
 "pregunta": "Quina paraula clau s'usa per capturar excepcions a Python?",
 "opcions": ["catch", "except", "handle"],
 "resposta": "except"},

 {"tipus": "test",
 "pregunta": "Quina paraula clau s'usa per executar codi sempre, independentment de si hi ha errors?",
 "opcions": ["finally", "always", "end"],
 "resposta": "finally"},

]

# Per tenir més preguntes
preguntes.extend(preguntes * 20)
total_preguntes = preguntes.copy()

def escriure_text(text, font, color, x, y, ombra=False):
    if ombra:
        ombra_surf = font.render(text, True, GRIS_FOSC)
        pantalla.blit(ombra_surf, (x + 2, y + 2))
    text_surf = font.render(text, True, color)
    pantalla.blit(text_surf, (x, y))

def boto(text, x, y, w, h, actiu):
    ombra_rect = pygame.Rect(x + 4, y + 4, w, h)
    pygame.draw.rect(pantalla, GRIS_FOSC, ombra_rect, border_radius=8)
    color = BLAU if actiu else GRIS_FOSC
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(pantalla, color, rect, border_radius=8)
    escriure_text(text, font, BLANC, x + 20, y + 12)
    return rect

def dibuixar_heart(x, y, mida, color):
    radius = mida // 4
    pygame.draw.circle(pantalla, color, (x - radius, y), radius)
    pygame.draw.circle(pantalla, color, (x + radius, y), radius)
    punts = [(x - mida//2, y), (x + mida//2, y), (x, y + mida)]
    pygame.draw.polygon(pantalla, color, punts)

def fons_gradient():
    for i in range(ALCADA):
        ratio = i / ALCADA
        r = int(BLAU_CLAR[0] * (1 - ratio) + BLANC[0] * ratio)
        g = int(BLAU_CLAR[1] * (1 - ratio) + BLANC[1] * ratio)
        b = int(BLAU_CLAR[2] * (1 - ratio) + BLANC[2] * ratio)
        pygame.draw.line(pantalla, (r, g, b), (0, i), (AMPLADA, i))

def menu():
    menu_actiu = True
    opcions = ["Jugar", "Manual de Python", "Sortir"]

    while menu_actiu:
        fons_gradient()
        escriure_text("Menú Principal", font_gran, GRIS_FOSC, AMPLADA//2 - 150, 50, ombra=True)
        
        mx, my = pygame.mouse.get_pos()
        for i, opcio in enumerate(opcions):
            rect = pygame.Rect(AMPLADA//2 - 100, 150 + i*100, 200, 50)
            actiu = rect.collidepoint(mx, my)
            boto(opcio, rect.x, rect.y, rect.w, rect.h, actiu)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, opcio in enumerate(opcions):
                    rect = pygame.Rect(AMPLADA//2 - 100, 150 + i*100, 200, 50)
                    if rect.collidepoint(mx, my):
                        if opcio == "Jugar":
                            jugar()
                        elif opcio == "Manual de Python":
                            manual()
                        elif opcio == "Sortir":
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        rellotge.tick(60)

def manual():
    llegint_manual = True
    contingut_manual = [
        "Python és un llenguatge de programació interpretat.",
        "S'utilitzen indentacions per definir blocs de codi.",
        "Variables: mi_variable = 10",
        "Funcions: def mi_funcio():",
        "Comentaris: # Això és un comentari",
        "Llistes: mi_llista = []",
        "Bucle for: for i in range(5):",
        "Condicionals: if x > 0:"
    ]

    while llegint_manual:
        fons_gradient()
        escriure_text("Manual de Python per a Principiants", font_gran, GRIS_FOSC, 50, 20, ombra=True)
        for i, linia in enumerate(contingut_manual):
            escriure_text(linia, font, NEGRE, 50, 80 + i*30)

        rect_tornar = pygame.Rect(AMPLADA -150, ALCADA -70, 120, 50)
        pygame.draw.rect(pantalla, BLAU, rect_tornar, border_radius=8)
        escriure_text("Tornar", font, BLANC, rect_tornar.x + 20, rect_tornar.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if rect_tornar.collidepoint(mx, my):
                    llegint_manual = False

        pygame.display.flip()
        rellotge.tick(60)

def jugar():
    vides = 3
    preguntes_respondre = random.sample(total_preguntes, 15)
    idx_pregunta = 0
    puntuacio = 0
    feedback = ""
    feedback_temps = 0
    espera_resposta = True

    while True:
        if idx_pregunta >= len(preguntes_respondre) or vides <= 0:
            final_joc(vides, puntuacio)
            break
        
        pregunta = preguntes_respondre[idx_pregunta]
        resposta_usuari = ""
        espera_resposta = True

        while espera_resposta:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        resposta_usuari = resposta_usuari[:-1]
                    elif event.key == pygame.K_RETURN:
                        correcte = False
                        if pregunta['tipus'] == 'test':
                            correcte = resposta_usuari.strip().lower() == pregunta['resposta'].lower()
                        elif pregunta['tipus'] == 'acabar':
                            correcte = resposta_usuari.strip() == pregunta['resposta']
                        
                        if correcte:
                            puntuacio += 1
                            feedback = "Correcte!"
                            feedback_temps = pygame.time.get_ticks()
                            idx_pregunta += 1
                            espera_resposta = False
                        else:
                            vides -= 1
                            feedback = "Incorrecte!"
                            feedback_temps = pygame.time.get_ticks()
                            if vides <= 0:
                                espera_resposta = False
                            else:
                                idx_pregunta += 1
                                espera_resposta = False
                        data = {"score": puntuacio, "lives": vides, "num_pregunta": idx_pregunta}
                        resposta = ServidorCodelearn.guardar_progres(data)
                        
                        print(resposta)
                    else:
                        # Permetem només caràcters imprimibles
                        if event.unicode.isprintable():
                            resposta_usuari += event.unicode

            # Dibuixar fons i UI
            fons_gradient()
            escriure_text(f"Pregunta {idx_pregunta + 1} / 15", font, NEGRE, 50, 20)
            escriure_text(pregunta['pregunta'], font_gran, NEGRE, 50, 70)

            if pregunta['tipus'] == "test":
                for i, opcio in enumerate(pregunta['opcions']):
                    escriure_text(f"{i + 1}. {opcio}", font, NEGRE, 80, 150 + i*40)

            elif pregunta['tipus'] == "acabar":
                # Mostrem la línia que s'ha d'acabar
                escriure_text(pregunta['codi_inici'], font_gran, BLAU, 50, 150)
            
            escriure_text("Resposta: " + resposta_usuari, font, NEGRE, 50, 400)

            # Barra de vides
            for i in range(vides):
                dibuixar_heart(1400 + i*60, 700, 50, ROIG)

            # Barra de progrés
            pygame.draw.rect(pantalla, GRIS_CLAR, (50, 550, 700, 25), border_radius=10)
            amplada_progres = int(700 * (idx_pregunta / 15))
            pygame.draw.rect(pantalla, VERD, (50, 550, amplada_progres, 25), border_radius=10)

            # Feedback de la resposta
            if feedback and pygame.time.get_ticks() - feedback_temps < 1500:
                color_feedback = VERD if feedback == "Correcte!" else ROIG
                escriure_text(feedback, font_gran, color_feedback, AMPLADA//2 - 70, 500)
            else:
                feedback = ""

            pygame.display.flip()
            rellotge.tick(60)

def final_joc(vides_restants, puntuacio):
    final = True
    botons = {"Reiniciar": pygame.Rect(AMPLADA//2 - 150, 400, 140, 50),
              "Menú": pygame.Rect(AMPLADA//2 + 10, 400, 140, 50)}
    data = {"PreguntesEncertades": puntuacio, "lives": vides_restants}
    resposta = ServidorCodelearn.finalitzar_partida(data, puntuacio)
    print (resposta)

    while final:
        fons_gradient()
        escriure_text("Fi del Joc", font_gran, ROIG, AMPLADA//2 - 90, 150, ombra=True)
        escriure_text(f"Puntuació: {puntuacio} / 15", font_gran, NEGRE, AMPLADA//2 - 120, 250, ombra=True)
        escriure_text(f"Vides restants: {vides_restants}", font, NEGRE, AMPLADA//2 - 80, 320)

        mx, my = pygame.mouse.get_pos()

        for text_boto, rect_boto in botons.items():
            actiu = rect_boto.collidepoint(mx, my)
            color_boto = BLAU if actiu else GRIS_FOSC
            pygame.draw.rect(pantalla, color_boto, rect_boto, border_radius=8)
            escriure_text(text_boto, font, BLANC, rect_boto.x + 20, rect_boto.y + 12)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botons["Reiniciar"].collidepoint(mx, my):
                    jugar()
                    final = False
                elif botons["Menú"].collidepoint(mx, my):
                    menu()
                    final = False

        pygame.display.flip()
        rellotge.tick(60)

# Iniciem el joc
menu()