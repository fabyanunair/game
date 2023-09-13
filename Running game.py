
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300)) 
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/audio/jump.mp3')
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_sound.set_volume(0.12)

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1,fly_2]
            y_pos = 200
        else:
            snail_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1,snail_2] 
            y_pos = 300
        self.animation_index = 0


        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        



def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface,obstacle_rect)
            elif obstacle_rect.bottom == 200:
                screen.blit(fly_surf,obstacle_rect)

            

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collison_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]


    

# Basic
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Game Taek')
clock = pygame.time.Clock()
test_font = pygame.font.Font('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/font/Pixeltype.ttf', 50)
test_font2 = pygame.font.Font('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/font/Pixeltype.ttf', 70)
game_active = False
start_time = 0
score = 0


bg_Music = pygame.mixer.Sound('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/audio/music.wav')
bg_Music.play(loops = -1)
bg_Music.set_volume(0.1)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Time
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score :  {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    print(current_time)
    return current_time




# Background
sky_surface = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/ground.png').convert()

# Snail
snail_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/snail/snail2.png').convert_alpha()
snail = [snail_1,snail_2]
snail_index = 0

snail_surface = snail[snail_index]

# Fly
fly_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/fly/fly1.png').convert_alpha()
fly_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/fly/fly2.png').convert_alpha()
fly = [fly_1,fly_2]
fly_index = 0
fly_surf = fly[fly_index]


obstacle_rect_list = []

# Player
player_walk_1 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('D:/Project/vscode/python/Running game/UltimatePygameIntro-main/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) 
player_stand_rect = player_stand.get_rect(center = (400,200))

intro_text1 = test_font2.render('Iki game taek',False,(64,64,64))
text1_rect = intro_text1.get_rect(center = (400,80))
intro_text2 = test_font.render('Peteken space lek arep dolen!', False, (64,64,64))
text2_rect = intro_text2.get_rect(center = (400,330))

# Timer
obstacle_timer = pygame.USEREVENT + 1   
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom >= 300:
                    player_gravity = -20
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),200)))
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surface = snail[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly[fly_index]
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
               
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
              
                start_time = int(pygame.time.get_ticks() / 1000)
        
            
        

            

 # Actual Game       
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        
        score = display_score()

    
        
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collison
        game_active = collison_sprite()

        
        
# Game Over

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        pesan_penyemangat = test_font.render("Cacat cok, gaisok maen.",False,(111,196,169))
        penyemangat_rect = pesan_penyemangat.get_rect(center = (400,330))
        score_message = test_font.render(f'Your score : {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,80))
        if score == 0:
            screen.blit(intro_text1,text1_rect)
            screen.blit(intro_text2,text2_rect)
        else:
            screen.blit(score_message,score_message_rect)
            screen.blit(pesan_penyemangat,penyemangat_rect)
    
    pygame.display.update()
    clock.tick(60)