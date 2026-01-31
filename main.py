import pygame
from sys import exit
import random

# --- CONFIGURATION & CONSTANTES ---
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 200, 0)
BLUE, GOLD = (0, 191, 255), (255, 215, 0)
GRAVITY = 0.15 

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FRUIT SLICER PRO")
clock = pygame.time.Clock()
font_lg = pygame.font.SysFont("Arial", 50, bold=True)
font_sm = pygame.font.SysFont("Arial", 25)

# --- SUPPORT MULTILINGUE ---
LANGUAGES = {
    "FR": {
        "play": "JOUER", "mode": "Mode: ", "diff": "Diff: ", "high": "Record: ",
        "lang": "Langue: ", "quit": "QUITTER", "gameover": "GAME OVER", 
        "menu": "Retour Menu", "score": "Score: ", "time": "Temps: ", "strikes": "Fautes: "
    },
    "EN": {
        "play": "PLAY", "mode": "Mode: ", "diff": "Diff: ", "high": "High Score: ",
        "lang": "Lang: ", "quit": "QUIT", "gameover": "GAME OVER", 
        "menu": "Back to Menu", "score": "Score: ", "time": "Time: ", "strikes": "Strikes: "
    }
}
current_lang = "FR"

# --- VARIABLES GLOBALES ---
high_score = 0
game_state = "MENU"
difficulty = "Normal"
game_mode = "Classique" 
timer_challenge = 60 * 60 
freeze_timer = 0
score, strikes = 0, 0

class Entity:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.size = 50
        self.rect = pygame.Rect(random.randint(60, SCREEN_WIDTH - 110), SCREEN_HEIGHT + 10, self.size, self.size)
        
        # Ajustement selon difficulté
        mult = 0.7 if difficulty == "Facile" else (1.0 if difficulty == "Normal" else 1.4)
        bombe_chance = 0.05 if difficulty == "Facile" else (0.15 if difficulty == "Normal" else 0.30)

        self.speed_y = random.uniform(-18, -14) * mult 
        self.speed_x = random.uniform(-3, 3)
        
        rand = random.random()
        if rand < bombe_chance: self.type = "bombe"
        elif rand < bombe_chance + 0.1: self.type = "glacon"
        elif rand < bombe_chance + 0.15: self.type = "fruit_or"
        else: self.type = "fruit"

    def update(self):
        global freeze_timer
        current_gravity = GRAVITY if freeze_timer <= 0 else GRAVITY * 0.1
        current_speed_mult = 1 if freeze_timer <= 0 else 0.2

        self.rect.y += self.speed_y * current_speed_mult
        self.rect.x += self.speed_x * current_speed_mult
        self.speed_y += current_gravity

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH: self.speed_x *= -1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y *= -0.5

    def draw(self):
        # Utilisation de couleurs simples au lieu d'images
        color = RED if self.type == "fruit" else (BLACK if self.type == "bombe" else (BLUE if self.type == "glacon" else GOLD))
        pygame.draw.ellipse(window, color, self.rect)

entities = [Entity() for _ in range(4)]

def draw_text_centered(text, font, color, rect_target):
    surf = font.render(text, True, color)
    text_rect = surf.get_rect(center=rect_target.center)
    window.blit(surf, text_rect)

def reset_game():
    global score, strikes, freeze_timer, entities, timer_challenge
    score, strikes, freeze_timer = 0, 0, 0
    timer_challenge = 60 * 60
    entities = [Entity() for _ in range(4)]

# --- BOUCLE PRINCIPALE ---
while True:
    mouse_pos = pygame.mouse.get_pos()
    txt = LANGUAGES[current_lang]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "MENU":
                b_play = pygame.Rect(SCREEN_WIDTH//2-100, 160, 200, 45)
                b_mode = pygame.Rect(SCREEN_WIDTH//2-100, 220, 200, 45)
                b_diff = pygame.Rect(SCREEN_WIDTH//2-100, 280, 200, 45)
                b_lang = pygame.Rect(SCREEN_WIDTH//2-100, 340, 200, 45)
                b_quit = pygame.Rect(SCREEN_WIDTH//2-100, 400, 200, 45)
                
                if b_play.collidepoint(mouse_pos): reset_game(); game_state = "PLAY"
                if b_mode.collidepoint(mouse_pos): game_mode = "Challenge" if game_mode == "Classique" else "Classique"
                if b_diff.collidepoint(mouse_pos):
                    diffs = ["Facile", "Normal", "Difficile"]
                    difficulty = diffs[(diffs.index(difficulty) + 1) % 3]
                if b_lang.collidepoint(mouse_pos): current_lang = "EN" if current_lang == "FR" else "FR"
                if b_quit.collidepoint(mouse_pos): pygame.quit(); exit()
                
            elif game_state == "GAMEOVER": game_state = "MENU"

    window.fill(WHITE)

    if game_state == "MENU":
        draw_text_centered("FRUIT SLICER", font_lg, BLACK, pygame.Rect(0, 40, SCREEN_WIDTH, 100))
        buttons = [
            (pygame.Rect(SCREEN_WIDTH//2-100, 160, 200, 45), GREEN, txt["play"]),
            (pygame.Rect(SCREEN_WIDTH//2-100, 220, 200, 45), WHITE, txt["mode"] + game_mode),
            (pygame.Rect(SCREEN_WIDTH//2-100, 280, 200, 45), WHITE, txt["diff"] + difficulty),
            (pygame.Rect(SCREEN_WIDTH//2-100, 340, 200, 45), WHITE, txt["lang"] + current_lang),
            (pygame.Rect(SCREEN_WIDTH//2-100, 400, 200, 45), RED, txt["quit"])
        ]
        for r, c, t in buttons:
            pygame.draw.rect(window, c, r, border_radius=8)
            pygame.draw.rect(window, BLACK, r, 2, border_radius=8)
            draw_text_centered(t, font_sm, BLACK if c == WHITE else WHITE, r)
        draw_text_centered(f"{txt['high']} {high_score}", font_sm, BLACK, pygame.Rect(0, 500, SCREEN_WIDTH, 30))

    elif game_state == "PLAY":
        if freeze_timer > 0: 
            freeze_timer -= 1
            window.fill((230, 245, 255))
            
        if game_mode == "Challenge":
            timer_challenge -= 1
            if timer_challenge <= 0: game_state = "GAMEOVER"

        mouse_click = pygame.mouse.get_pressed()
        sliced = 0
        for e in entities:
            e.update()
            if mouse_click[0] and e.rect.collidepoint(mouse_pos):
                if e.type == "bombe": game_state = "GAMEOVER"
                elif e.type == "glacon": freeze_timer = 240; e.spawn()
                elif e.type == "fruit_or": score += 5; e.spawn()
                else: sliced += 1; e.spawn()
            if e.rect.y > SCREEN_HEIGHT + 20:
                if e.type in ["fruit", "fruit_or"] and game_mode == "Classique": strikes += 1
                e.spawn()
            e.draw()

        if sliced > 0: score += sliced + (sliced - 1 if sliced > 1 else 0)
        
        window.blit(font_sm.render(f"{txt['score']} {score}", True, BLACK), (20, 20))
        if game_mode == "Classique":
            window.blit(font_sm.render(f"{txt['strikes']} {strikes}", True, RED), (20, 50))
            if strikes >= 3: game_state = "GAMEOVER"
        else:
            window.blit(font_sm.render(f"{txt['time']} {timer_challenge//60}s", True, BLUE), (20, 50))

    elif game_state == "GAMEOVER":
        if score > high_score: high_score = score
        window.fill(BLACK)
        draw_text_centered(txt["gameover"], font_lg, RED, pygame.Rect(0, 200, SCREEN_WIDTH, 50))
        draw_text_centered(f"{txt['score']} {score}", font_sm, WHITE, pygame.Rect(0, 300, SCREEN_WIDTH, 30))
        draw_text_centered(txt["menu"], font_sm, WHITE, pygame.Rect(0, 400, SCREEN_WIDTH, 30))

    pygame.display.update()
    clock.tick(60)