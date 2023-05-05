from dataclasses import dataclass
import pygame

pygame.init()


@dataclass
class Lamp:
    pos: pygame.Vector2
    powered: bool


class LampVisualizer:
    lamp_off = pygame.image.load("lamp_visualizer/off.png")
    lamp_on = pygame.image.load("lamp_visualizer/on.png")
    layout = []
    width = None
    height = None

    @staticmethod
    def init(width, height) -> None:
        LampVisualizer.width = width - (width % 16)
        LampVisualizer.height = height - (height % 16)
        for y in range(height // 16):
            LampVisualizer.layout.append([])
            for x in range(width // 16):
                LampVisualizer.layout[y].append(Lamp(pygame.Vector2(x, y), False))

    @staticmethod
    def run() -> None:
        if not LampVisualizer.width:
            raise Exception("Please call LampVisualizer.init(width, height) first")
        size = (LampVisualizer.width, LampVisualizer.height)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Lamp Visualizer")
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for y in range(LampVisualizer.height // 16):
                for x in range(LampVisualizer.width // 16):
                    if LampVisualizer.layout[y][x].powered:
                        screen.blit(LampVisualizer.lamp_on, (x * 16, y * 16))
                    else:
                        screen.blit(LampVisualizer.lamp_off, (x * 16, y * 16))

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    @staticmethod
    def toggle(x, y) -> None:
        LampVisualizer.layout[y][x].powered = not LampVisualizer.layout[y][x].powered
