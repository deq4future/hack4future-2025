import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Adventure con Preguntas de Python")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Fuentes
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 48)

# Reloj para FPS
clock = pygame.time.Clock()

# Clases
class Player:
    def __init__(self):
        self.width = 40
        self.height = 60
        self.x = WIDTH // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 5
        self.lives = 3
        self.color = GREEN
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        self.x += dx * self.speed
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Enemy:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(2, 4)
        self.color = RED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Función para mostrar texto en pantalla
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Preguntas de ejemplo
questions = [
    {
        "question": "¿Cómo se escribe un ciclo for en Python?",
        "answer": "for i in range(5):"
    },
    {
        "question": "¿Cómo se define una función en Python?",
        "answer": "def mi_funcion():"
    },
    {
        "question": "¿Cómo se crea una lista en Python?",
        "answer": "mi_lista = []"
    }
]

# Función para obtener una pregunta aleatoria
def get_random_question():
    return random.choice(questions)

# Variables de juego
player = Player()
enemies = []
spawn_timer = 0
spawn_interval = 90  # frames

# Estado del juego
game_over = False
current_question = None
player_input = ""
show_question = False
score = 0

# Función para mostrar la pregunta y recibir respuesta
def ask_question(question_data):
    global show_question, player_input
    show_question = True
    player_input = ""
    return question_data

# Loop principal
running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if show_question:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]
                elif event.key == pygame.K_RETURN:
                    # Verificar respuesta
                    correct_answer = current_question['answer'].strip()
                    if player_input.strip() == correct_answer:
                        score += 1
                        # Eliminar enemigo si existe
                        for enemy in enemies:
                            if enemy.rect.colliderect(player.rect):
                                enemies.remove(enemy)
                                break
                    else:
                        player.lives -= 1
                        if player.lives <= 0:
                            game_over = True
                    show_question = False
                else:
                    player_input += event.unicode

    keys = pygame.key.get_pressed()
    if not show_question and not game_over:
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)

    # Spawnear enemigos
    if not show_question and not game_over:
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            enemies.append(Enemy())

    # Actualizar enemigos
    if not show_question and not game_over:
        for enemy in enemies:
            enemy.update()
            if enemy.rect.colliderect(player.rect):
                # Cuando un enemigo toca al jugador, hacerle una pregunta
                current_question = ask_question(get_random_question())
                enemies.remove(enemy)
            elif enemy.y > HEIGHT:
                enemies.remove(enemy)

    # Dibujar todo
    if not game_over:
        player.draw()

        for enemy in enemies:
            enemy.draw()

        # Mostrar vidas
        draw_text(f"Vidas: {player.lives}", font, BLACK, 10, 10)
        # Mostrar puntuación
        draw_text(f"Puntaje: {score}", font, BLACK, 10, 50)

        # Mostrar pregunta si es momento
        if show_question:
            # Dibujar cuadro de pregunta
            question_box = pygame.Rect(50, 150, WIDTH - 100, 200)
            pygame.draw.rect(screen, WHITE, question_box)
            pygame.draw.rect(screen, BLACK, question_box, 2)

            # Mostrar la pregunta
            draw_text("Respuesta:", font, BLACK, question_box.x + 10, question_box.y + 10)
            draw_text(current_question['question'], font, BLACK, question_box.x + 10, question_box.y + 50)

            # Mostrar la respuesta del jugador
            draw_text("Respuesta: " + player_input, font, BLACK, question_box.x + 10, question_box.y + 100)

    else:
        # Fin del juego
        draw_text("Juego Terminado", large_font, RED, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        draw_text(f"Tu puntaje: {score}", font, BLACK, WIDTH // 2 - 80, HEIGHT // 2 + 10)

    pygame.display.flip()

pygame.quit()
sys.exit()
