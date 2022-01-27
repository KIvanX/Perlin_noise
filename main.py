import pygame
import time
from dop import generateMap

w, h = 1200, 600

pygame.init()
window = pygame.display.set_mode((w - 600, h - 20))
pygame.display.set_caption("Шум Перлина")

t = time.time()
a1 = generateMap(w, h)
a2 = generateMap(w, h)
t = time.time() - t
print('T =', t, 'sec')

surf1 = pygame.pixelcopy.make_surface(a1)
surf2 = pygame.pixelcopy.make_surface(a2)

i = 0
while True:
    i = i + 1 if i <= 1200 else 1
    window.blit(surf1, (-i, -10))
    window.blit(surf2, (-i + w, -10))
    pygame.display.flip()
    time.sleep(0.01)

    if i % w == 0:
        a = generateMap(w, h)
        new_surf = pygame.pixelcopy.make_surface(a)
        surf1, surf2 = surf2, new_surf
        print('created')

# game = 1
# while game:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game = 0

#
# str1 = pygame.image.tostring(surf, 'RGB')
# str2 = pygame.image.tostring(new_surf, 'RGB')
# str1.join(str2)
# surf = pygame.image.fromstring(str1, (w, h), 'RGB')
