import pygame, time, random, sqlite3, os, sys

conn = sqlite3.connect("high_score.db")
c = conn.cursor()

pygame.init()
win = pygame.display.set_mode((800, 574))
pygame.display.set_caption("Stop the Bots")

bot1x = 115
bot1y = 220
bot2x = 370
bot2y = 210
bot3x = 600
bot3y = 210

background_color = (0, 0, 0)

title_image = pygame.image.load("title.png")
img1 = pygame.image.load("bot1.png")
img2 = pygame.image.load("bot2.png")
img3 = pygame.image.load("bot3.png")
boom = pygame.image.load("boom.png")
heart_small = pygame.image.load("smal_heart.png")
heart = pygame.image.load("heart.png")


def reset(current_high_score):
    c.execute(f"UPDATE score SET high_score = 0 WHERE high_score = {current_high_score};")
    conn.commit()


def rect_draw():
    pygame.draw.rect(win, (background_color), (220, 440, 357, 50))


def rect_draw2(botx):
    pygame.draw.rect(win, (background_color), (botx - 50, 170, 175, 210))


def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def wait():
    continue_time = False
    while continue_time == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    continue_time = True





font0 = pygame.font.Font('freesansbold.ttf', 25)
font1 = pygame.font.Font('freesansbold.ttf', 33)
font2 = pygame.font.Font('freesansbold.ttf', 40)
font3 = pygame.font.Font('freesansbold.ttf', 50)
font4 = pygame.font.Font('freesansbold.ttf', 70)
font5 = pygame.font.Font('freesansbold.ttf', 100)
run = True

c.execute(f"SELECT * FROM score")
ammount = c.fetchone()
for i in ammount:
    highest_score = i
conn.commit()

os.system("clear")
pygame.time.delay(100)
win.fill((background_color))
title_text = font2.render(("Stop the Bots"), True, (255, 160, 59), (background_color))
highest_score_text = font1.render((f"Highest Score: {highest_score}"), True, (255, 160, 59), (background_color))
win.blit((title_image), (240, 40))
win.blit((title_text), (280, 360))
win.blit((highest_score_text), (280, 420))
pygame.display.update()

wait()
win.fill((background_color))


def intro(text, y_num):
    intro = font1.render((text), True, (255, 160, 59), (background_color))
    win.blit((intro), (50, y_num))
    pygame.display.update()


intro(f"Hello Player,", 60)
intro("Destroy the robots ransacking the building.", 160)
intro("Your laser rifle does 100 damage.", 260)
intro("Bots' cannons do 50 damage.", 360)
intro("Press Enter to continue", 460)
wait()

while run:
    O1 = False
    O2 = False
    O3 = False
    score = 0
    win.fill((background_color))
    pygame.display.update()
    win.fill((background_color))
    hp = 400
    E1 = random.randrange(100, 400, 100)
    E2 = random.randrange(100, 600, 100)
    E3 = random.randrange(100, 700, 100)
    if E2 > 400:
        hp += int(100)
    if E3 > 400:
        hp += int(100)

    while hp > 0:
        quit()
        if hp >= 900:
            hp -= 300
        if O1 and O2 and O3 == True:
            if score >= 1:
                background_color = (161, 132, 51)
            if score >= 4:
                background_color = (144, 4, 199)
            if score >= 7:
                background_color = (72, 110, 82)
            if score >= 10:
                background_color = (214, 56, 160)
            if score >= 13:
                background_color = (255, 255, 255)
            if score >= 16:
                background_color = (76, 162, 173)

            score = score + 1
            win.fill((background_color))
            levelup = font5.render(f"Level {score}!", True, (0, 255, 26),(background_color))
            win.blit((levelup), (200, 230))
            pygame.display.update()
            time.sleep(2.4)
            win.fill((background_color))
            hp += 250
            O1 = False
            O2 = False
            O3 = False
            E1 = random.randrange(100, 400, 100)
            E2 = random.randrange(100, 600, 100)
            E3 = random.randrange(100, 700, 100)
            if E2 > 400:
                hp += int(100)
            if E2 > 400:
                hp += int(100)

        who_attack_text = font0.render("Use 1, 2, or 3 keys to shoot", True, (255, 160, 59), (background_color))
        score_num = font2.render(f"Level: {score}", True, (255, 106, 0),(background_color))
        if hp <= 150:
            health = font2.render(f"{str(hp)}", True, (255, 0, 0), (background_color))
        else:
            health = font2.render(f"{str(hp)}", True, (255, 106, 0),(background_color))
        pygame.draw.rect(win, (background_color), (610, 30, 80, 50))
        win.blit((health), (620, 30))
        win.blit((heart), (680, -10))
        win.blit((score_num), (40, 30))
        win.blit((who_attack_text), (227, 454))
        pygame.display.update()

        if O1 == False:
            bot_health_font = font0.render(f"{str(E1)}", True, (255, 106, 0),(background_color))
            bot_type = font0.render("1", True, (255, 106, 0), (background_color))
            win.blit((bot_type), (145, 180))
            win.blit((bot_health_font), (115, 350))
            win.blit((heart_small), (160, 340))
            win.blit((img1), (bot1x, bot1y))
            pygame.display.update()
        if O2 == False:
            bot_health_font = font0.render(f"{str(E2)}", True, (255, 106, 0),(background_color))
            bot_type = font0.render("2", True, (255, 106, 0), (background_color))
            win.blit((bot_type), (390, 175))
            win.blit((bot_health_font), (365, 351))
            win.blit((heart_small), (410, 341))
            win.blit((img2), (bot2x, bot2y))
            pygame.display.update()
        if O3 == False:
            bot_health_font = font0.render(f"{str(E3)}", True, (255, 106, 0),(background_color))
            bot_type = font0.render("3", True, (255, 106, 0), (background_color))
            win.blit((bot_type), (626, 175))
            win.blit((bot_health_font), (592, 353))
            win.blit((heart_small), (640, 343))
            win.blit((img3), (bot3x, bot3y))
            pygame.display.update()

        Opponent = 4
        who_attack = False
        while who_attack == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        Opponent = 1
                        rect_draw()
                        who_attack = True
                    if event.key == pygame.K_2:
                        Opponent = 2
                        rect_draw()
                        who_attack = True
                    if event.key == pygame.K_3:
                        Opponent = 3
                        rect_draw()
                        who_attack = True

        Dmg = int(100)
        Odmg = int(50)
        Omiss = random.randint(1, 3)
        Ocrit = random.randint(1, 12)
        Miss = random.randint(1, 6)
        Crit = random.randint(1, 8)
        misses = False
        if Miss == 6:
            misses = True
        miss_text = font2.render("You missed", True, (255, 0, 0), (background_color))
        omiss_text = font2.render("The bot missed!", True, (0, 255, 26),(background_color))
        crit_text = font2.render("Critical!", True, (0, 255, 26), (background_color))
        bot_dead = font2.render("You killed the Bot!", True, (0, 255, 26),(background_color))

        def crit_miss():
            global Odmg
            global Dmg
            if Ocrit == 12:
                Odmg = int(100)
            if Omiss == 3:
                rect_draw()
                win.blit((omiss_text), (240, 440))
                pygame.display.update()
                time.sleep(0.5)
                rect_draw()
                pygame.display.update()
                Odmg = int(0)
            if Crit == 8 and misses == False:
                rect_draw()
                win.blit((crit_text), (310, 440))
                pygame.display.update()
                time.sleep(0.5)
                rect_draw()
                pygame.display.update()
                Dmg = int(200)
            if Miss == 6:
                rect_draw()
                win.blit((miss_text), (280, 440))
                pygame.display.update()
                time.sleep(0.5)
                rect_draw()
                pygame.display.update()
                Dmg = int(0)

        if Opponent == 1:
            crit_miss()
            hp -= Odmg
            E1 -= Dmg
            if E1 <= int(0):
                rect_draw2(bot1x)
                win.blit((boom), (bot1x - 10, bot1y - 10))
                rect_draw()
                win.blit((bot_dead), (220, 440))
                pygame.display.update()
                time.sleep(0.6)
                rect_draw()
                rect_draw2(bot1x)
                pygame.display.update()
                O1 = True

        if Opponent == 2:
            crit_miss()
            hp -= Odmg
            E2 -= Dmg
            if E2 <= int(0):
                rect_draw2(bot2x)
                win.blit((boom), (bot2x - 20, bot2y + 20))
                rect_draw()
                win.blit((bot_dead), (220, 440))
                pygame.display.update()
                time.sleep(0.6)
                rect_draw()
                rect_draw2(bot2x)
                pygame.display.update()
                O2 = True

        if Opponent == 3:
            crit_miss()
            hp -= Odmg
            E3 -= Dmg
            if E3 <= int(0):
                rect_draw2(bot3x)
                win.blit((boom), (bot3x - 20, bot3y + 20))
                rect_draw()
                win.blit((bot_dead), (220, 440))
                pygame.display.update()
                time.sleep(0.6)
                rect_draw()
                rect_draw2(bot3x)
                pygame.display.update()
                time.sleep(0.2)
                O3 = True

        if hp <= 0:
            you_die = font5.render("Game Over", True, (237, 19, 30),(background_color))
            end_text = font3.render(f"Your final score was {score}", True, (237, 19, 30), (background_color))
            if score > highest_score:
                end_text = font3.render(f"New Highest score: {score}", True, (237, 19, 30), (background_color))

                highest_score_new = score
                c.execute(f"UPDATE score SET high_score = {highest_score_new} WHERE high_score ={highest_score};")
                conn.commit()
                conn.close()

            win.fill((background_color))
            win.blit((you_die), (125, 170))
            win.blit((end_text), (150, 320))
            pygame.display.update()
            while hp <= 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        run = False
