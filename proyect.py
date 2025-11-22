import pygame
import sys

pygame.init()

# --- Ventana ---
ANCHO, ALTO = 800, 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Quiz V/F - Pygame")

# --- Colores ---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)

# --- Fuente ---
fuente = pygame.font.SysFont("Arial", 32)

# --- Preguntas (texto, respuesta_correcta) ---
preguntas = [
    ("Python fue creado antes que Java. (V/F)", "F"),
    ("La unidad básica de información es el bit. (V/F)", "V"),
    ("Pygame sirve para hacer páginas web. (V/F)", "F"),
    ("La suma de 2+2 es 4. (V/F)", "V")
]

indice = 0
puntuacion = 0
mostrar_feedback = False
feedback_texto = ""
feedback_color = NEGRO
tiempo_feedback = 0

clock = pygame.time.Clock()


def dibujar_texto(texto, color, x, y):
    render = fuente.render(texto, True, color)
    ventana.blit(render, (x, y))


running = True
while running:
    ventana.fill(BLANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Teclas para responder ---
        if evento.type == pygame.KEYDOWN and not mostrar_feedback:
            if evento.key == pygame.K_v:
                respuesta = "V"
            elif evento.key == pygame.K_f:
                respuesta = "F"
            else:
                respuesta = None

            if respuesta:
                correcta = preguntas[indice][1]
                if respuesta == correcta:
                    feedback_texto = "¡Correcto!"
                    feedback_color = VERDE
                    puntuacion += 1
                else:
                    feedback_texto = "Incorrecto"
                    feedback_color = ROJO

                mostrar_feedback = True
                tiempo_feedback = pygame.time.get_ticks()

    # --- Mostrar pregunta o resultado ---
    if indice < len(preguntas):

        # Si no hay feedback, mostrar pregunta normal
        if not mostrar_feedback:
            dibujar_texto(f"Pregunta {indice+1}/{len(preguntas)}:", NEGRO, 50, 80)
            dibujar_texto(preguntas[indice][0], NEGRO, 50, 150)
            dibujar_texto("Presiona V (Verdadero) o F (Falso)", NEGRO, 50, 350)

        else:
            # Mostrar mensaje por 1.5 segundos
            dibujar_texto(feedback_texto, feedback_color, 50, 200)

            if pygame.time.get_ticks() - tiempo_feedback > 1500:
                mostrar_feedback = False
                indice += 1

    else:
        # FIN DEL QUIZ
        dibujar_texto("¡Quiz finalizado!", NEGRO, 50, 150)
        dibujar_texto(f"Puntaje total: {puntuacion} / {len(preguntas)}", NEGRO, 50, 230)
        dibujar_texto("Presiona ESC para salir", NEGRO, 50, 300)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
