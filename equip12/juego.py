import pygame
import random
import sys
import requests
import threading
import time

# Configuración de la ventana
pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego Matemático 🧠 + Pong Retro 🕹️")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (50, 145, 255)
verde = (0, 200, 0)
rojo = (200, 0, 0)
rosa = (252, 3, 202)
naranja = (255, 115, 0)

# Fuente
fuente = pygame.font.SysFont(None, 60)
peque = pygame.font.SysFont(None, 40)
muypeque = pygame.font.SysFont(None, 30)

# Imagenes
codelearn = pygame.image.load("Codelearn.png")
codelearn = pygame.transform.scale(codelearn, (200, 80))

# Variables del servidor
game_id = None
start_time = None
datos_progreso = []

# Mostrar texto
def mostrar_texto(texto, fuente, color, y, x = None):

    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=(ancho // 2, y))
    ventana.blit(superficie, rect)

# Conexión con el servidor
def iniciar_partida():
    global game_id, start_time
    try:
        respuesta = requests.get("https://fun.codelearn.cat/hackathon/game/new")
        if respuesta.ok:
            datos = respuesta.json()
            game_id = datos["game_id"]
            seed = datos["seed"]
            random.seed(seed)
            start_time = time.time()
            print(f"Partida iniciada. ID: {game_id}, seed: {seed}")
        else:
            print("Error al iniciar la partida:", respuesta.text)
    except Exception as e:
        print("Error de conexión al iniciar partida:", e)

def enviar_progreso_periodico():
    def enviar():
        while game_id:
            try:
                progreso = {
                    "tiempo": int(time.time() - start_time),
                    "eventos": datos_progreso[-10:]
                }
                cuerpo = {"game_id": game_id, "data": progreso}
                r = requests.post("https://fun.codelearn.cat/hackathon/game/store_progress", json=cuerpo)
                if r.ok:
                    print("Progreso enviado.")
                else:
                    print("Error al enviar progreso:", r.json())
            except Exception as e:
                print("Error al enviar progreso:", e)
            time.sleep(10)
    threading.Thread(target=enviar, daemon=True).start()

def finalizar_partida(puntuacion):
    try:
        duracion = int(time.time() - start_time)
        data = {
            "tiempo_total": duracion,
            "eventos": datos_progreso
        }
        cuerpo = {"game_id": game_id, "data": data, "score": puntuacion}
        r = requests.post("https://fun.codelearn.cat/hackathon/game/finalize", json=cuerpo)
        if r.ok:
            print("Partida finalizada correctamente.")
        else:
            print("Error al finalizar partida:", r.json())
    except Exception as e:
        print("Error al finalizar partida:", e)

# Juego
def pedir_rondas():
    texto = ""
    pidiendo = True
    while pidiendo:
        ventana.fill(azul)
        
        # Bordes Pregunta Rondas
        texto_rondas = "¿Cuántas rondas quieres jugar?"
        surf_rondas = fuente.render(texto_rondas, True, blanco)
        rect_rondas = surf_rondas.get_rect(center=(ancho // 2, 200))
        fondo_rondas = rect_rondas.inflate(60, 25)
        pygame.draw.rect(ventana, (100, 0, 150), fondo_rondas, border_radius=12)        # púrpura oscuro
        pygame.draw.rect(ventana, (60, 0, 100), fondo_rondas, width=3, border_radius=12) # borde más oscuro
        ventana.blit(surf_rondas, rect_rondas)

        # Bordes Respuesta1
        surf_respuesta = fuente.render(texto, True, blanco)
        rect_respuesta = surf_respuesta.get_rect(center=(ancho // 2, 300))
        fondo_respuesta = rect_respuesta.inflate(60, 25)
        pygame.draw.rect(ventana, (150, 0, 100), fondo_respuesta, border_radius=12)         # fondo rosa oscuro
        pygame.draw.rect(ventana, (90, 0, 60), fondo_respuesta, width=3, border_radius=12)  # borde más oscuro
        ventana.blit(surf_respuesta, rect_respuesta)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if texto.isdigit() and int(texto) > 0:
                        return int(texto)
                elif evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif evento.unicode.isdigit():
                    texto += evento.unicode

def generar_operacion():
    a = random.randint(1, 500)
    b = random.randint(1, 500)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        resultado = a * b
    else:
        a = random.randint(1, 100)
        b = random.randint(1, 10)
        a = a * b
        resultado = a // b
        op = "/"
    return a, b, op, resultado
def jugar_rondas(total_rondas):
    puntos = 0
    contador_tiempo = 30
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    for ronda in range(1, total_rondas + 1):
        a, b, op, correcto = generar_operacion()
        respuesta = ""
        tiempo_restante = contador_tiempo
        esperando = True

        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.USEREVENT:
                    tiempo_restante -= 1
                    if tiempo_restante <= 0:
                        ventana.fill(azul)
                        
                        # Bordes Tiempo Terminado
                        texto_tt = "¡Tiempo terminado!"
                        surf_tt = fuente.render(texto_tt, True, (255, 255, 255))  # texto blanco para contraste
                        rect_tt = surf_tt.get_rect(center=(ancho // 2, alto // 2))
                        fondo_tt = rect_tt.inflate(60, 30)
                        pygame.draw.rect(ventana, (180, 0, 0), fondo_tt, border_radius=15)       # fondo rojo oscuro
                        pygame.draw.rect(ventana, (100, 0, 0), fondo_tt, width=3, border_radius=15) # borde más oscuro
                        ventana.blit(surf_tt, rect_tt)

                        pygame.display.update()
                        pygame.time.delay(2000)
                        pygame.time.set_timer(pygame.USEREVENT, 0)
                        return puntos
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if respuesta.lstrip('-').isdigit():
                            if int(respuesta) == correcto:
                                puntos += 1
                                datos_progreso.append({"evento": "acierto", "pregunta": f"{a}{op}{b}", "respuesta": int(respuesta)})
                                
                                # Bordes Correc 
                                texto_c = "¡Correcto! :)"
                                surf_c = fuente.render(texto_c, True, (230, 255, 230))  # texto verde claro/blanco
                                rect_c = surf_c.get_rect(center=(ancho // 2, 400))
                                fondo_c = rect_c.inflate(60, 30)
                                pygame.draw.rect(ventana, (0, 120, 0), fondo_c, border_radius=15)        # fondo verde oscuro
                                pygame.draw.rect(ventana, (0, 60, 0), fondo_c, width=3, border_radius=15)  # borde aún más oscuro
                                ventana.blit(surf_c, rect_c)

                            else:
                                datos_progreso.append({"evento": "error", "pregunta": f"{a}{op}{b}", "respuesta": int(respuesta), "correcto": correcto})
                                texto_1 = "Incorrecto :("
                                texto_2 = f"Era {correcto}"

                                surf_1 = fuente.render(texto_1, True, (255, 200, 200))  # texto rojo claro
                                surf_2 = fuente.render(texto_2, True, (255, 200, 200))

                                # Posiciones
                                x_centro = ancho // 2
                                y_1 = 400
                                y_2 = 440

                                # Rectángulos para cada texto, centrados
                                rect_1 = surf_1.get_rect(center=(x_centro, y_1))
                                rect_2 = surf_2.get_rect(center=(x_centro, y_2))

                                # Rectángulo que engloba los dos textos
                                top = rect_1.top
                                bottom = rect_2.bottom
                                width = max(rect_1.width, rect_2.width)
                                height = bottom - top
                                fondo_total = pygame.Rect(0, 0, width + 60, height + 30)  # margen extra
                                fondo_total.center = (x_centro, (y_1 + y_2) // 2)

                                # Dibuja fondo y borde
                                pygame.draw.rect(ventana, (180, 50, 50), fondo_total, border_radius=15)       # fondo rojo oscuro
                                pygame.draw.rect(ventana, (100, 20, 20), fondo_total, width=3, border_radius=15) # borde más oscuro

                                # Pinta los textos encima
                                ventana.blit(surf_1, rect_1)
                                ventana.blit(surf_2, rect_2)

                            pygame.display.update()
                            pygame.time.delay(1500)
                            esperando = False
                    elif evento.key == pygame.K_BACKSPACE:
                        respuesta = respuesta[:-1]
                    elif evento.unicode.isdigit() or (evento.unicode == "-" and len(respuesta) == 0):
                        respuesta += evento.unicode

            ventana.fill(azul)
            
            # Fondo Ronda
            texto_ronda = f"Ronda {ronda}/{total_rondas}"
            surf_ronda = peque.render(texto_ronda, True, blanco)
            rect_ronda = surf_ronda.get_rect(center=(ancho // 2, 50))
            fondo_ronda = rect_ronda.inflate(30, 15)
            pygame.draw.rect(ventana, (0, 80, 160), fondo_ronda, border_radius=12)  # fondo azul oscuro
            pygame.draw.rect(ventana, (0, 50, 100), fondo_ronda, width=3, border_radius=12)  # borde más oscuro
            ventana.blit(surf_ronda, rect_ronda)
            
            # Fondo Puntos
            texto_puntos = f"Puntos = {puntos}"
            surf_puntos = muypeque.render(texto_puntos, True, blanco)
            rect_puntos = surf_puntos.get_rect(center=(ancho // 2, 90))
            fondo_puntos = rect_puntos.inflate(30, 15)
            pygame.draw.rect(ventana, (255, 140, 0), fondo_puntos, border_radius=12)  # fondo naranja oscuro
            pygame.draw.rect(ventana, (180, 90, 0), fondo_puntos, width=3, border_radius=12)  # borde marrón oscuro
            ventana.blit(surf_puntos, rect_puntos)
            
            # Bordes Operacion
            texto_operacion = f"{a} {op} {b} = ?"
            surf_op = fuente.render(texto_operacion, True, blanco)
            rect_op = surf_op.get_rect(center=(ancho // 2, 200))
            fondo_op = rect_op.inflate(40, 20)
            pygame.draw.rect(ventana, (100, 0, 150), fondo_op, border_radius=12)  # púrpura oscuro
            pygame.draw.rect(ventana, (60, 0, 90), fondo_op, width=3, border_radius=12)  # borde más oscuro
            ventana.blit(surf_op, rect_op)

            # Bordes Respuesta
            surf_resp = fuente.render(respuesta, True, blanco)
            rect_resp = surf_resp.get_rect(center=(ancho // 2, 300))
            fondo_resp = rect_resp.inflate(40, 20)
            pygame.draw.rect(ventana, (0, 150, 100), fondo_resp, border_radius=12)  # verde-azulado
            pygame.draw.rect(ventana, (0, 90, 60), fondo_resp, width=3, border_radius=12)  # borde más oscuro
            ventana.blit(surf_resp, rect_resp)

            # Bordes Tiempo
            texto_tiempo = f"Tiempo: {tiempo_restante} s"
            surf_tiempo = fuente.render(texto_tiempo, True, blanco)
            rect_tiempo = surf_tiempo.get_rect(center=(ancho // 2, 550))
            fondo_tiempo = rect_tiempo.inflate(40, 20)
            pygame.draw.rect(ventana, (255, 50, 120), fondo_tiempo, border_radius=12)  # rosa fuerte
            pygame.draw.rect(ventana, (180, 20, 80), fondo_tiempo, width=3, border_radius=12)  # borde oscuro
            ventana.blit(surf_tiempo, rect_tiempo)
            
            
            ventana.blit(codelearn, (ancho - codelearn.get_width() - 10, 10))
            pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT, 0)
    return puntos


def mostrar_resultado(puntos, total):
    ventana.fill(blanco)

    # Título: Victoria o derrota
    if puntos >= total / 2:
        texto1 = "¡Ganaste! :)"
        color_fondo1 = (0, 180, 0)
        color_borde1 = (0, 100, 0)
        color_texto1 = blanco
    else:
        texto1 = "Perdiste :("
        color_fondo1 = (180, 0, 0)
        color_borde1 = (100, 0, 0)
        color_texto1 = blanco

    surf1 = fuente.render(texto1, True, color_texto1)
    rect1 = surf1.get_rect(center=(ancho // 2, 200))
    fondo1 = rect1.inflate(50, 30)
    pygame.draw.rect(ventana, color_fondo1, fondo1, border_radius=12)
    pygame.draw.rect(ventana, color_borde1, fondo1, width=3, border_radius=12)
    ventana.blit(surf1, rect1)

    # Puntos conseguidos
    texto2 = f"Puntos: {puntos} de {total}"
    surf2 = fuente.render(texto2, True, blanco)
    rect2 = surf2.get_rect(center=(ancho // 2, 300))
    fondo2 = rect2.inflate(60, 25)
    pygame.draw.rect(ventana, (0, 120, 200), fondo2, border_radius=12)  # azul oscuro
    pygame.draw.rect(ventana, (0, 70, 130), fondo2, width=3, border_radius=12)
    ventana.blit(surf2, rect2)

    # Mensaje para continuar
    texto3 = "Pulsa ENTER para comenzar el PONG"
    surf3 = muypeque.render(texto3, True, negro)
    rect3 = surf3.get_rect(center=(ancho // 2, 400))
    fondo3 = rect3.inflate(30, 15)
    pygame.draw.rect(ventana, (230, 230, 230), fondo3, border_radius=10)
    pygame.draw.rect(ventana, (180, 180, 180), fondo3, width=2, border_radius=10)
    ventana.blit(surf3, rect3)

    pygame.display.update()


    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False


def pong_retro():
    clock = pygame.time.Clock()
    pelota = pygame.Rect(ancho // 2, alto // 2, 20, 20)
    jugador = pygame.Rect(30, alto // 2 - 60, 10, 120)
    bot = pygame.Rect(ancho - 40, alto // 2 - 60, 10, 120)

    velocidad_pelota = [6, 6]
    velocidad_jugador = 0
    puntuacion_bot = 0
    operacion_mostrada = False

    respuesta = ""
    resolviendo = False
    a, b, op, correcto = 0, 0, "", 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_x:
                    # Al pulsar X salimos del pong y volvemos a la pantalla resultado sin cerrar el programa
                    return False
                if not resolviendo:
                    if evento.key == pygame.K_UP:
                        velocidad_jugador = -7
                    elif evento.key == pygame.K_DOWN:
                        velocidad_jugador = 7
                if resolviendo:
                    if evento.key == pygame.K_RETURN:
                        if respuesta.lstrip('-').isdigit():
                            if int(respuesta) == correcto:
                                puntuacion_bot = max(0, puntuacion_bot - 1)
                                datos_progreso.append({"evento": "pong acierto", "pregunta": f"{a}{op}{b}"})
                            else:
                                datos_progreso.append({"evento": "pong error", "pregunta": f"{a}{op}{b}", "respuesta": int(respuesta)})
                            resolviendo = False
                            operacion_mostrada = False
                            respuesta = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        respuesta = respuesta[:-1]
                    elif evento.unicode.isdigit() or (evento.unicode == "-" and len(respuesta) == 0):
                        respuesta += evento.unicode
            elif evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_UP, pygame.K_DOWN):
                    velocidad_jugador = 0

        if not resolviendo:
            pelota.x += velocidad_pelota[0]
            pelota.y += velocidad_pelota[1]

            jugador.y += velocidad_jugador
            jugador.y = max(min(jugador.y, alto - 120), 0)

            # Bot más lento para que sea más fácil (antes 6, ahora 4)
            if bot.centery < pelota.centery:
                bot.y += 4
            elif bot.centery > pelota.centery:
                bot.y -= 4
            bot.y = max(min(bot.y, alto - 120), 0)

            if pelota.top <= 0 or pelota.bottom >= alto:
                velocidad_pelota[1] *= -1

            if pelota.colliderect(jugador) or pelota.colliderect(bot):
                velocidad_pelota[0] *= -1

            # Evitar que la pelota se quede atrapada al entrar en la pared
            if pelota.left <= 0:
                puntuacion_bot += 1
                pelota = pygame.Rect(ancho // 2, alto // 2, 20, 20)
                # Cambiar dirección aleatoria para evitar quedar atrapada
                velocidad_pelota = [6 * random.choice([-1, 1]), 6 * random.choice([-1, 1])]
                operacion_mostrada = True
                resolviendo = True
                a, b, op, correcto = generar_operacion()

            if pelota.right >= ancho:
                if puntuacion_bot > 0:
                    puntuacion_bot -= 1
                else:
                    puntuacion_bot == 0
                pelota = pygame.Rect(ancho // 2, alto // 2, 20, 20)
                velocidad_pelota = [6 * random.choice([-1, 1]), 6 * random.choice([-1, 1])]

        ventana.fill(negro)
        pygame.draw.rect(ventana, blanco, jugador)
        pygame.draw.rect(ventana, blanco, bot)
        pygame.draw.ellipse(ventana, rosa, pelota)
        pygame.draw.aaline(ventana, blanco, (ancho // 2, 0), (ancho // 2, alto))

        # Bordes Puntuacion Bot
        texto_bot = f"Bot: {puntuacion_bot}"
        surf_bot = peque.render(texto_bot, True, blanco)
        rect_bot = surf_bot.get_rect(center=(ancho // 2, 40))
        fondo_bot = rect_bot.inflate(50, 25)
        pygame.draw.rect(ventana, (160, 40, 40), fondo_bot, border_radius=10)       # rojo oscuro
        pygame.draw.rect(ventana, (100, 0, 0), fondo_bot, width=3, border_radius=10)  # borde más oscuro
        ventana.blit(surf_bot, rect_bot)


        if resolviendo:
            # Bordes Pregunta Pong
            texto_pregunta = f"¿Cuánto es {a} {op} {b}?"
            surf_preg = peque.render(texto_pregunta, True, blanco)
            rect_preg = surf_preg.get_rect(center=(ancho // 2, 200))
            fondo_preg = rect_preg.inflate(60, 30)
            pygame.draw.rect(ventana, (0, 90, 160), fondo_preg, border_radius=12)         # azul oscuro
            pygame.draw.rect(ventana, (0, 50, 100), fondo_preg, width=3, border_radius=12)  # borde más oscuro
            ventana.blit(surf_preg, rect_preg)

            # Bordes Respuesta Pong
            surf_resp = fuente.render(respuesta, True, (255, 180, 220))  # rosa claro
            rect_resp = surf_resp.get_rect(center=(ancho // 2, 300))
            fondo_resp = rect_resp.inflate(60, 30)
            pygame.draw.rect(ventana, (200, 80, 130), fondo_resp, border_radius=15)         # rosa fuerte
            pygame.draw.rect(ventana, (120, 30, 80), fondo_resp, width=3, border_radius=15)  # borde más oscuro
            ventana.blit(surf_resp, rect_resp)
        
        # Bordes Salir Pong
        texto_salir = "Pulsa X para salir"
        surf_salir = peque.render(texto_salir, True, blanco)
        rect_salir = surf_salir.get_rect(center=(ancho // 2, alto - 30))
        fondo_salir = rect_salir.inflate(40, 20)
        pygame.draw.rect(ventana, (50, 50, 50), fondo_salir, border_radius=10)       # gris oscuro
        pygame.draw.rect(ventana, (20, 20, 20), fondo_salir, width=2, border_radius=10)  # borde más oscuro
        ventana.blit(surf_salir, rect_salir)

        

        pygame.display.update()
        clock.tick(60)

# Programa principal
def main():
    iniciar_partida()
    enviar_progreso_periodico()

    rondas = pedir_rondas()
    puntos = jugar_rondas(rondas)

    while True:
        mostrar_resultado(puntos, rondas)
        salir_pong = pong_retro()
        if salir_pong is False:
            # Vuelve a la pantalla resultado sin salir del programa
            continue
        else:
            break

    finalizar_partida(puntos)
    pygame.quit()

if __name__ == "__main__":
    main()
