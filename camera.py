import pygame
Title: str = "Platformer"
X: int = 800
Y: int = 640

class Camera:
    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.state = pygame.Rect(0, 0, width, height)

    def update(self, char):
        self.state = self.getCameraRect(
            self.state.width, self.state.height, char.getX(), char.getY())

    def applyCorrdinatesToObject(self, target):
        return target.rect.move(self.state.topleft)

    def getCameraRect(self, cameraW: int = 0, cameraH: int = 0, heroX: int = 0, heroY: int = 0):
        heroX = max(-(cameraW - X), min(0, X / 2 - heroX))
        heroY = max(-(cameraH - Y), min(0, Y / 2 - heroY))
        return pygame.Rect(heroX, heroY, cameraW, cameraH)
