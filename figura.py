import pygame
import math

class Figura:
    def __init__(self, matriz):
        self.stepTranslation = 30
        self.stepRotation = 15

        self.matriz = matriz
        self.original_vertices = [(x * self.stepTranslation, y * self.stepTranslation) for x, y in matriz]
        self.vertices = list(self.original_vertices)

        # Criar arestas ligando cada vértice ao próximo, e a última aresta ligando o último vértice ao primeiro
        self.arestas = [(i, (i + 1) % len(self.vertices)) for i in range(len(self.vertices))]

        self.translation = [0, 0]
        self.rotation_angle = 0

    def update_vertices(self):
        """ Atualiza os vértices com base na translação e rotação atual. """
        cos_angle = math.cos(math.radians(self.rotation_angle))
        sin_angle = math.sin(math.radians(self.rotation_angle))
        self.vertices = []
        for x, y in self.original_vertices:
            # Aplica rotação
            rotated_x = x * cos_angle - y * sin_angle
            rotated_y = x * sin_angle + y * cos_angle

            # Aplica translação
            translated_x = rotated_x + self.translation[0]
            translated_y = rotated_y + self.translation[1]

            self.vertices.append((translated_x, translated_y))

    def draw_grid(self, screen):
        width, height = screen.get_size()
        center_x, center_y = width // 2, height // 2
        color = (200, 200, 200)  # Cor do grid: cinza claro

        # Desenha linhas verticais e horizontais
        for x in range(0, width // 2, self.stepTranslation):
            pygame.draw.line(screen, color, (center_x + x, 0), (center_x + x, height))
            pygame.draw.line(screen, color, (center_x - x, 0), (center_x - x, height))
        for y in range(0, height // 2, self.stepTranslation):
            pygame.draw.line(screen, color, (0, center_y + y), (width, center_y + y))
            pygame.draw.line(screen, color, (0, center_y - y), (width, center_y - y))

        # Desenha linhas dos eixos principais mais destacadas
        axis_color = (100, 100, 100)
        pygame.draw.line(screen, axis_color, (center_x, 0), (center_x, height))
        pygame.draw.line(screen, axis_color, (0, center_y), (width, center_y))

    def draw(self, screen):
        color = (255, 0, 0)  # Vermelho
        width, height = screen.get_size()
        center_x, center_y = width // 2, height // 2

        for aresta in self.arestas:
            start_pos = (self.vertices[aresta[0]][0] + center_x, self.vertices[aresta[0]][1] + center_y)
            end_pos = (self.vertices[aresta[1]][0] + center_x, self.vertices[aresta[1]][1] + center_y)
            pygame.draw.line(screen, color, start_pos, end_pos, 5)

    def run(self):
        pygame.init()
        width, height = 600, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Desenho de Figura com Grid')
        bg_color = (255, 255, 255)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            self.rotation_angle -= self.stepRotation  # Rotaciona para a esquerda
                        else:
                            self.translation[0] -= self.stepTranslation  # Move para a esquerda
                    elif event.key == pygame.K_RIGHT:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            self.rotation_angle += self.stepRotation  # Rotaciona para a direita
                        else:
                            self.translation[0] += self.stepTranslation  # Move para a direita
                    elif event.key == pygame.K_DOWN:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            self.rotation_angle += self.stepRotation  # Rotaciona para cima
                        else:
                            self.translation[1] += self.stepTranslation  # Move para cima
                    elif event.key == pygame.K_UP:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            self.rotation_angle -= self.stepRotation  # Rotaciona para baixo
                        else:
                            self.translation[1] -= self.stepTranslation  # Move para baixo
                    self.update_vertices()

            screen.fill(bg_color)
            self.draw_grid(screen)
            self.draw(screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()