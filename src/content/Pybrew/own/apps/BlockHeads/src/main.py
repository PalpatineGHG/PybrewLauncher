# Benötigte Module importieren
import pygame
import random
from modules.settings import Settings
from modules.highscore_manager import HighscoreManager as HighM
from modules.temporary_manager import TemporaryManager as TempM

# Pygame initialisieren
pygame.init()

# Schwierigkeitsgrad festlegen
difficulty = 1.8

# Highscore-Manager initialisieren
HighscoreManager = HighM()

# Temporary-Manager initialisieren
TemporaryManager = TempM()

# Höhe und breite festlegen
display_info = pygame.display.Info()
device_width = display_info.current_w
device_height = display_info.current_h
display_width = Settings.Res.width
display_height = Settings.Res.height

# Gegner Spawn-Radius festlagen
enemy_spawn_range_height = display_info.current_h - 400
enemy_spawn_range_width = display_info.current_w

# Vollbildmodus, Name und Icon initialisieren
window = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
background = (50, 50, 50)
pygame.display.set_caption('Mein erstes PyGame Spiel :D')
pygame.display.set_icon(pygame.image.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\img\\python_icon.ico'))

# Spielschleife auf True setzen
running = True

# Spieluhr setzen
clock = pygame.time.Clock()
fps = Settings.Frames.fps

# Spieler initialisieren
player = pygame.image.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\img\\player.png')
player_rect = player.get_rect()
player_x = display_width / 2 - player_rect.width / 2
player_y = display_height / 2 - player_rect.height / 2
player_alive = True

# Gegner initialisieren
enemy = pygame.image.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\img\\enemy.png')
enemy_rect = enemy.get_rect()
enemy_x = 100
enemy_y = 100

# Kugeln initialisieren
bullet_image = pygame.image.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\img\\bullet.png')
bullets = []

# Gegner-Kugel initialisieren
enemy_bullet_image = pygame.image.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\img\\enemy_bullet.png')
enemy_bullets = []

# Hintergrundmusik initialisieren
pygame.mixer.music.load('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\sound\\background_music.wav')
pygame.mixer.music.set_volume(Settings.Vol.music)
pygame.mixer.music.play()

# Andere Sounds initialisieren
shoot_sound = pygame.mixer.Sound('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\sound\\shoot_sound.wav')
shoot_sound.set_volume(Settings.Vol.sfx - 0.25)
death_sound = pygame.mixer.Sound('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\sound\\player_death_sound.wav')
death_sound.set_volume(Settings.Vol.music + 1.0)
enemy_death_sound = pygame.mixer.Sound('C:\\Users\\minec\\Documents\\Dev\\Projekte\\Python\\Projekte\\BlockHeads\\src\\sound\\enemy_death_sound.wav')
enemy_death_sound.set_volume(Settings.Vol.sfx)

# Punktestand initialisieren
score = 0

# Schriftart initialisieren
font = pygame.font.Font(None, 40)
fps_font = pygame.font.Font(None, 20)

# Gegner-Bewegungsvariablen hinzufügen
enemy_speed = difficulty + difficulty * 2.5
enemy_direction = 1

# Gegner-Schieß variablen hinzufügen
enemy_shoot_frequency = 60
enemy_shoot_timer = 0

# Pausenstatus initialisieren
paused = False


# Funktion zum Speichern des Highscores definieren
def save_highscore():
    if score > HighscoreManager.get_highscore():
        HighscoreManager.set_highscore(score)
        HighscoreManager.save_highscore()


# Funktion zum Speichern des Scores der letzten Runde definieren
def save_last_score():
    TemporaryManager.set_last_session_score(score)
    TemporaryManager.save_last_session_score(score)


# Funktion zum Zurücksetzen des Spiels definieren
def reset_game():
    save_last_score()
    save_highscore()
    global player_x, player_y, player_alive, bullets, enemy_bullets, score, enemy_x, enemy_y, enemy_direction, enemy_shoot_timer, font
    death_sound.stop()
    font = pygame.font.Font(None, 40)
    player_x = display_width / 2 - player_rect.width / 2
    player_y = display_height / 2 - player_rect.height / 2
    player_alive = True
    bullets = []
    enemy_bullets = []
    score = 0
    enemy_x = 100
    enemy_y = 100
    enemy_direction = 1
    enemy_shoot_timer = 0
    pygame.mixer.music.play(-1)


# Spielschleife
while running:

    for event in pygame.event.get():
        # Beenden-Ereignis
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        # Schießen-Ereignis
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
            if player_alive and not paused:
                shoot_sound.play()
                bullet_rect = bullet_image.get_rect(center=(player_x + player_rect.width // 2, player_y))
                bullets.append(bullet_rect)
        # Spiel neu starten
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not player_alive:
                reset_game()
        # Spiel pausieren
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            paused = not paused

    if not paused:
        keys = pygame.key.get_pressed()

        # Spieler-Steuerung
        if player_alive:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player_x -= 5
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player_x += 5
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                player_y -= 5
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player_y += 5

        # Sicherstellen, dass der Spieler innerhalb der Bildschirmgrenzen bleibt
        player_x = max(0, min(player_x, device_width - player_rect.width))
        player_y = max(0, min(player_y, device_height - player_rect.height))

        # Spieler-Rechteck aktualisieren
        player_rect.x = player_x
        player_rect.y = player_y

        # Kugeln aktualisieren
        for bullet in bullets[:]:
            bullet.y -= 10  # Kugel nach oben bewegen
            if bullet.y < 0:
                bullets.remove(bullet)
            elif bullet.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemy_death_sound.play()
                score += 1
                enemy_x = random.randint(0, enemy_spawn_range_width - enemy_rect.width)
                enemy_y = random.randint(0, enemy_spawn_range_height - enemy_rect.height)
                enemy_rect.x = enemy_x
                enemy_rect.y = enemy_y

        # Gegner-Kugeln aktualisieren
        for enemy_bullet in enemy_bullets[:]:
            enemy_bullet.y += 10  # Kugel nach unten bewegen
            if enemy_bullet.y > device_height:
                enemy_bullets.remove(enemy_bullet)
            elif enemy_bullet.colliderect(player_rect):
                enemy_bullets.remove(enemy_bullet)
                pygame.mixer.music.stop()
                death_sound.play()
                player_alive = False
                score_sin = 'Punkt'
                score_plu = 'Punkte'

                if score < 1:
                    print(f'Du hast {score} {score_plu} erreicht')
                elif score < 2:
                    print(f'Du hast {score} {score_sin} erreicht')
                else:
                    print(f'Du hast {score} {score_plu} erreicht')

        if player_alive:
            # Gegner-Bewegungslogik
            enemy_x += enemy_speed * enemy_direction
        
        # Richtung umkehren, wenn der Gegner die Grenzen erreicht
        if enemy_x <= 0 or enemy_x >= device_width - enemy_rect.width:
            enemy_direction *= -1

        # Schießlogik des Gegners
        enemy_shoot_timer += 1
        if enemy_shoot_timer >= enemy_shoot_frequency:
            enemy_shoot_timer = 0
            if player_alive:
                enemy_bullet_rect = enemy_bullet_image.get_rect(center=(enemy_x + enemy_rect.width // 2, enemy_y + enemy_rect.height))
                enemy_bullets.append(enemy_bullet_rect)

        # Sicherstellen, dass der Gegner innerhalb der Bildschirmgrenzen bleibt
        enemy_x = max(0, min(enemy_x, device_width - enemy_rect.width))
        enemy_y = max(0, min(enemy_y, device_height - enemy_rect.height))

        # Gegner-Rechteck aktualisieren
        enemy_rect.x = enemy_x
        enemy_rect.y = enemy_y

        # Kollision zwischen Spieler und Gegner überprüfen
        if player_alive and player_rect.colliderect(enemy_rect):
            pygame.mixer.music.stop()
            death_sound.play()
            player_alive = False

    # Bildschirm leeren
    window.fill(background)

    # GUI rendern
    show_fps = clock.get_fps()
    show_fps_text = fps_font.render(f'FPS: {round(show_fps, 0)}', True, (0, 255, 0))
    show_fps_text_rect = show_fps_text.get_rect(center=(100, 10))
    window.blit(show_fps_text, show_fps_text_rect)
    highscore = HighscoreManager.get_highscore()
    last_score = TemporaryManager.get_last_session_score()
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    text_rect = score_text.get_rect(center=(device_width / 2, 50))
    hs_text = font.render(f'Highscore: {highscore}', True, (255, 255, 255))
    last_score_text = font.render(f'Last Score: {last_score}', True, (255, 255, 255))
    last_score_text_rect = last_score_text.get_rect(center=(device_width / 2, 150))
    if score > highscore:
        hs_text = font.render(f'Highscore: {score}', True, (255, 255, 255))
    hs_text_rect = hs_text.get_rect(center=(device_width / 2, 100))
    if player_alive:
        window.blit(last_score_text, last_score_text_rect)
        window.blit(score_text, text_rect)
        window.blit(hs_text, hs_text_rect)
    else:
        font = pygame.font.Font(None, 75)
        go_text = font.render(f'Game Over', True, (255, 255, 255))
        res_text = font.render(f'Press Space to restart', True, (255, 255, 255))
        go_text_rect = go_text.get_rect(center=(device_width / 2, device_height / 2 - 50))
        res_text_rect = res_text.get_rect(center=(device_width / 2, device_height / 2 + 50))
        window.blit(go_text, go_text_rect)
        window.blit(res_text, res_text_rect)

    if paused:
        pause_font = pygame.font.Font(None, 75)
        pause_text = pause_font.render(f'Paused', True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(device_width / 2, device_height / 2))
        window.blit(pause_text, pause_text_rect)

    # Gegner an der neuen Position zeichnen
    window.blit(enemy, (enemy_x, enemy_y))

    # Spieler an der neuen Position zeichnen, wenn er lebt
    if player_alive:
        window.blit(player, (player_x, player_y))

    # Kugeln zeichnen
    for bullet in bullets:
        window.blit(bullet_image, bullet.topleft)

    for enemy_bullet in enemy_bullets:
        window.blit(enemy_bullet_image, enemy_bullet.topleft)

    # Anzeige aktualisieren, jedes Mal, wenn ein neuer Frame gerendert wird
    pygame.display.update()
    clock.tick(fps)

# Punktestand ausgeben, letzten Score und Highscore speichern und Spiel beenden
score_sin = 'Punkt'
score_plu = 'Punkte'

if score < 1:
    print(f'Du hast {score} {score_plu} erreicht')
elif score < 2:
    print(f'Du hast {score} {score_sin} erreicht')
else:
    print(f'Du hast {score} {score_plu} erreicht')

save_last_score()
save_highscore()

pygame.quit()
