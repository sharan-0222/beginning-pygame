import pygame 
pygame.init()
SCREEN_W, SCREEN_H = 500, 500
dis_surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("my first project")
bimg=pygame.transform.scale(pygame.image.load("ftftft.jpg").convert(), (SCREEN_W, SCREEN_H))

img=pygame.transform.scale(
    pygame.image.load("ftftft.jpg").convert_alpha(),(200, 200))
img_rect=img.get_rect(center=(SCREEN_W//2, SCREEN_H//2-30))


text=pygame.font.Font(None, 50).render("Hello World", True, pygame.Color("black"))
text_rect=text.get_rect(center=(SCREEN_W//2, SCREEN_H//2+110))
def game_LOOP():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        dis_surface.blit(bimg, (0, 0))
        dis_surface.blit(img, img_rect)
        dis_surface.blit(text, text_rect)
        pygame.display.update()
        clock.tick(60)

game_LOOP()