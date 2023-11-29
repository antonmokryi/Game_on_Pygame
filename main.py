import pygame

pygame.init()


# Установка назви гри та створення дісплею
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Game for you")

# Установка іконки гри
icon = pygame.image.load('img/iconP.png')
pygame.display.set_icon(icon)

# Запуск проекта
running = True

#Створення об"єкта
# square = pygame.Surface((40, 80))
# square.fill("Blue")

bg_sound = pygame.mixer.Sound("sound/sound1.mp3")
bg_sound.play()

#Створення текста
title = pygame.font.Font('fonts/Oswald-VariableFont_wght.ttf', 30)
title_surface = title.render('Hello World', True, 'Red')

#Додаємо картинку  героя
iconPlayer = pygame.image.load('img/icon_player.png').convert_alpha()

#Додаємо задній фон
bg = pygame.image.load('img/bg.png').convert_alpha()

hero = pygame.image.load("img/player_left/left1.png").convert_alpha()




go_left = [
        pygame.image.load("img/player_left/left1.png").convert_alpha(),
        pygame.image.load("img/player_left/left2.png").convert_alpha(),
        pygame.image.load("img/player_left/left3.png").convert_alpha(),
        pygame.image.load("img/player_left/left4.png").convert_alpha()
    ]
go_right = [
        pygame.image.load("img/player_right/right1.png").convert_alpha(),
        pygame.image.load("img/player_right/right2.png").convert_alpha(),
        pygame.image.load("img/player_right/right3.png").convert_alpha(),
        pygame.image.load("img/player_right/right4.png").convert_alpha()
    ]
anim_count = 0 # Кількість прохходження масиву для зміни анімації

clock = pygame.time.Clock() # регулюємо частоту зміни кадрів анімаціїї




bg_x = 0 # Зміна для заднього фона 
bg_speed = 5 #Скорость удаления заднего фона
bg_x2 = 800


player_speed = 3
player_x = 50

player_y = 350
is_jump = False
jump_count = 7

# ghost = pygame.image.load("/img/ghost.png")  # Створюємо привида 
ghost1 = pygame.image.load("img/ghost.png").convert_alpha()
ghost_x = 800   # Координати откуда буде починати двіженіє

# tuple kortesh



#Додаємо квадрат навколо героя
player_rect = hero.get_rect(topleft=(player_x, player_y))
ghost_rect = ghost1.get_rect(topleft=(ghost_x, 350))

#Створюю таймер для постійного появлення привиду\
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1000)

ghost_list = []

gameplay = True
mouse = pygame.mouse.get_pos()

lose_title = title.render("You lose", False, "Red")
restart_title = title.render("Restart", True, "black" )
restart_rect = restart_title.get_rect(topleft=(355, 180))
 

while running:
    

    # screen.fill((192, 192, 192)) установка постійного фону
    # screen.blit(title_surface, (200, 10) ) # Виводимо надпісь на екран
    # screen.blit(square, (10, 50)) # вивод на кран обєкта
    # pygame.draw.circle(square, "Red", (20, 10), 10)
    #screen.blit(iconPlayer, (150, 150)) # Вивод на екран icon_player

    screen.blit(bg, (bg_x, 0)) #встановлюємо бекграунд
    screen.blit(bg, (bg_x, 0)) #встановлюємо бекграунд який буде двигатись
    
    if gameplay:
        screen.blit(ghost1, (ghost_x, 350))


        keys = pygame.key.get_pressed() # Відобразить на яку кнопку нажав
        if pygame.K_RIGHT:
            screen.blit(go_right[anim_count], (player_x, player_y))
        else:
            screen.blit(go_left[anim_count], (player_x, player_y))
    
        bg_x -= bg_speed
    
        if bg_x == -799:
            bg_x == 0
    # elif bg_x2 == 0:
    #     bg_x2 == 800



        if anim_count == 3 :
            anim_count = 0
        else :
            anim_count += 1



    #####Двигаємо персонажа

        if keys[pygame.K_LEFT] and player_x > 20:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 700:
            player_x += player_speed

    #Прижок  
        if not is_jump:
            if keys[pygame.K_SPACE] :
                is_jump = True
        else:   
            if jump_count >= -7:
                if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7

    #######################

    ######Робота с Привидом####
            ghost_x -= 10
        if ghost_list:
            for (i, el) in enumerate(ghost_list):
                screen.blit(ghost1, el)
                el.x -= 10
                if el.x < -10:
                    ghost_list.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False
                    print("you_lose")
        ###########################
    else:
        screen.fill((234, 157, 149))
        screen.blit(lose_title, (350, 100))
        screen.blit(restart_title, (355, 180))

        
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 50
            ghost_list.clear()


    




    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT()
        # Установка изменения цвета заднего фона одной кнопкой
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((240, 255, 255))
        if event.type == ghost_timer:
            ghost_list.append(ghost1.get_rect(topleft=(800, 350)))
        #_____________________________________________________

    clock.tick(15)  # установлюємо зміну кадрів


