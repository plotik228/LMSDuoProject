import pygame
import sys
import random
import time
import os

from pygame.examples.aliens import load_image
from pygame.examples.cursors import image


def terminate():
    pygame.quit()
    sys.exit()

def draw(screen, width, height):
    for i in range(2222):
        screen.fill(pygame.Color((160, 160, 160)),
                    (random.random() * width,
                     random.random() * height, 1, 1))


def zastavka(screen, width, height):
    global font
    font = pygame.font.Font(None, 70)
    global text
    text = font.render("PLAY", True, (255, 255, 255))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1600, 720
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw(screen, width, height)
        font = pygame.font.Font(None, 70)
        text = font.render("PLAY", True, (255, 255, 255))
        tw = width // 2 - text.get_width() // 2
        th = height // 2 - text.get_height() // 2
        screen.blit(text, (tw, th))

        if (pygame.mouse.get_pos()[0] >= tw and pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2 and
                pygame.mouse.get_pos()[1] >= th and pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
            text = font.render("PLAY", True, (128, 128, 128))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        else:
            text = font.render("PLAY", True, (255, 255, 255))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= width // 2 - text.get_width() // 2 and
                        pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2 and
                        pygame.mouse.get_pos()[1] >= height // 2 - text.get_height() // 2 and
                        pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
                    screen.fill((0, 0, 0))
                    running = False

            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()

clock = pygame.time.Clock()
start_time = time.time()

def rules_render(screen, rule, y, cnt):
    if cnt == 0:
        font = pygame.font.SysFont('Consolas', 20)
        x = 100
        for i in rule:
            for l in i:
                text = font.render(l, True, (255, 255, 255))
                screen.blit(text, (x, y))
                clock.tick(600)
                pygame.display.flip()
                x += 10
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
            pygame.time.wait(300)
            y += 30
            x = 100
        cnt += 1
    else:
        return

rules_1 = ["Алло, алло?", "",
                   "Эм, я решил записать для тебя сообщение, чтобы помочь тебе освоиться в первую ночь. Вообще, я работал в этом офисе ещё до тебя.",
                   "Я как раз заканчиваю свою последнюю неделю. Я знаю, что ты немного взволнован, но беспокоиться вовсе не о чем, всё будет отлично. ",
                   "Так что давай сосредоточимся на том, что я помогу тебе пройти первый день. Договорились?"]

rules_2 = ["Ну, сначала я должен прочитать вступительное приветствие от компании. Юридическая ерунда, сам знаешь: «Добро пожаловать в «Freddy Fazbear's Pizza». ",
                   "Волшебное место для детей и взрослых, где оживают фантазии и веселье. Компания Fazbear Entertainment не несет ответственности ",
                   "за ущерб имуществу или людям. ",
                   "В случае обнаружения ущерба или смерти, заявление о пропаже подаётся в течение 90 дней, или после тщательной очистки имущества ",
                   "и всех помещений, и замены ковровых покрытий.»"]

rules_3 = ["Бла-бла-бла, звучит паршиво, я знаю, но волноваться не о чем. Ну, здешние аниматроники немного странно себя ведут по ночам, но разве я их виню? Нет. ",
           "Если бы меня заставляли петь одни и те же дурацкие песенки в течение двадцати лет и не давали бы сходить в душ, то я был бы тоже раздражителен. ",
           "Так что, помни, эти персонажи занимают особое место в сердцах детей, и нужно проявить к ним немного уважения, верно? Хорошо."]

rules_4 = ["Так что, просто знай, эти персонажи могут ходить сами по себе. Их оставляют в каком-то «режиме свободного передвижения» по ночам. ",
           "Вроде из-за того, что их сервоприводы блокируются, если они будут выключены слишком долго. Раньше им разрешалось ходить и днем. ",
           "Но в 87-м произошёл инцидент с укусом. Поразительно, что человеческое тело может жить без лобной доли, да?"]

rules_5 = ["Эм, касательно безопасности - единственный реальный риск для тебя как ночного охранника здесь, если он вообще есть, это то, что эти персонажи, ",
           "эм, если они увидят тебя в нерабочее время, то они, вероятно, не распознают в тебе человека. ",
           "Они, скорее всего, увидят в тебе металлический эндоскелет без костюма. Так как это противоречит правилам в пиццерии Фредди Фазбера, ",
           "они, вероятно, попытаются... насильно затолкать тебя в костюм Фредди Фазбера. Вроде и нет в этом ничего страшного, если б сами костюмы",
           "не были заполнены траверсами, проводами и ",
           "прочими аниматронными механизмами, особенно вокруг лицевой части. Так что, попробуй представить, как твою голову с силой вдавливают туда, ",
           "и это причиняет тебе небольшой дискомфорт... и смерть. Белый свет увидят лишь твои глаза и зубы, которые выскочат из передней части маски, хех."]

rules_6 = ["Да-да, они не сказали тебе об этом при регистрации. Но, эй, первый день - легче лёгкого. Я поговорю с тобой завтра. ",
           "Проверяй камеры и закрывай двери только в случае крайней необходимости. Нужно экономить энергию. Ладно, спокойной ночи."]
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0

rules = [rules_1, rules_2, rules_3, rules_4, rules_5, rules_6]
cnts = [cnt1, cnt2, cnt3, cnt4, cnt5, cnt6]

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1600, 720
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 60)
        text = font.render('12:00 AM', True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        elapsed_time = time.time() - start_time
        if elapsed_time >= 4:
            screen.fill((0, 0, 0))
            y = 50
            for i in range(len(rules)):
                if rules[i] == rules_4:
                    screen.fill((0, 0, 0))
                    y = 50
                # pygame.time.wait(1000)
                rules_render(screen, rules[i], y, cnts[i])
                y += (len(rules[i]) + 1) * 30 + 30
                cnts[i] = 1

            text = font.render('12:00 AM', True, (0, 0, 0))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 70)
            text = font.render("НАЧАТЬ ИГРУ", True, (255, 255, 255))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pos()[0] >= width // 2 - text.get_width() // 2 and
                            pygame.mouse.get_pos()[0] <= width // 2 + text.get_width() // 2 and
                            pygame.mouse.get_pos()[1] >= height // 2 - text.get_height() // 2 and
                            pygame.mouse.get_pos()[1] <= height // 2 + text.get_height() // 2):
                        running = False
            pygame.display.flip()
        pygame.display.flip()

    pygame.quit()

def load_image(name, colorkey=None):
    fullname = os.path.join('fnaf', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def fnaf_button_monitor(screen):
    button = load_image("fnaf_button_monitor.png")
    screen.blit(button, (335, 650))

def security(screen):
    sec = load_image("sec1.png")
    screen.blit(sec, (0, 0))


class Vents(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for i in range(1 ,4):
            image = load_image(f"vent{i}.png")
            self.images.append(image)
        self.cur_frame = 0
        self.image = self.images[self.cur_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_frame_time = 0
        self.frame_delay = 10

    def update(self):
        cur_time = pygame.time.get_ticks()
        if cur_time - self.last_frame_time >= self.frame_delay:
            self.cur_frame = (self.cur_frame + 1) % len(self.images)
            self.image = self.images[self.cur_frame]
            self.last_frame_time = cur_time


class MonitorUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.image = pygame.Surface((0, 0))
        self.images.append(self.image)
        for i in range(1, 11):
            image = load_image(f"mon{i}.png")
            image = pygame.transform.scale(image, (1600, 720))
            self.images.append(image)
        self.cur_frame = 0
        self.image = self.images[self.cur_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_frame_time = 0
        self.frame_delay = 10
        self.animated_finish = False

    def update(self, animated_playing, animated_finished):
        if animated_playing:
            cur_time = pygame.time.get_ticks()
            if cur_time - self.last_frame_time >= self.frame_delay:
                self.cur_frame = self.cur_frame + 1
                if self.cur_frame < len(self.images):
                    self.image = self.images[self.cur_frame]
                    self.last_frame_time = cur_time
                else:
                    animated_playing = False
                    animated_finished = True


def buttondown():
    if (pygame.mouse.get_pos()[0] >= 335 and pygame.mouse.get_pos()[0] <= 935
            and pygame.mouse.get_pos()[1] >= 650 and pygame.mouse.get_pos()[1] <= 710):
       return True
    else:
        return False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1600, 720
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    all_vents = pygame.sprite.GroupSingle()
    vents = Vents(780, 303)
    all_vents.add(vents)

    all_mon_up = pygame.sprite.GroupSingle()
    monitors = MonitorUp(0, 0)
    all_mon_up.add(monitors)

    animated_finished = False
    animated_playing = False
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not animated_finished and buttondown():  # Запускаем анимацию, только если она не завершена
                    animated_playing = True
                    last_frame_time = pygame.time.get_ticks()

        security(screen)
        fnaf_button_monitor(screen)

        all_vents.update()
        all_vents.draw(screen)

        all_mon_up.draw(screen)
        all_mon_up.update(animated_playing, animated_finished)

        pygame.display.flip()

    pygame.quit()

#Я НЕ ЗНАЮ КАК СДЕЛАТЬ ЭТО ВОНЮЧЕЕ СВОРАЧИВАНИЕ МОНИТОРА И ВОНЮЧЕЕ ВСЕ И ВОНЮЧИЕ КАМЕРЫ
