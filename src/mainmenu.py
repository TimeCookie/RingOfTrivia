import pygame
import sys
import os
import ringoftrivia
import math
import mainmenu_indo


#setup

lang_file = open("curlang.txt","w")
lang_file.write("english")
lang_file.close()


mainClock = pygame.time.Clock()
from pygame.locals import *


pygame.init()
pygame.display.set_caption('Ring Of Trivia')
screen = pygame.display.set_mode((0,0))

WIDTH, HEIGHT = pygame.display.get_surface().get_size() # Get the client's screen size
 
font = pygame.font.SysFont(None, 45)

isMuteMusic = False
isMuteSFX = False


prev_music = 0.6 #default volume for music
prev_sfx = 0.6 #default volume for sfx
# Music
pygame.mixer.init()
bgm = pygame.mixer.music.load("assets/sounds/mainmenu.ogg") 
pygame.mixer.music.play()

entry = os.listdir()



    
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#color
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    
def main_menu():
    click = False
    Running = True


    entry = os.listdir()
    if "firsttime.txt" not in entry:
        file = open("firsttime.txt","w")
        file.write(str(hash("This player is not a newcomer! Welcome to Ring of Trivia, hope you enjoy your time here")))
        file.close()
        game_help()
    elif "firsttime.txt" in entry:
        file = open("firsttime.txt","r")
        file_data = file.read()
        if file_data != None:
            file.close()
        

    while Running:

        bg = pygame.image.load('assets/english/bg/ROTMAINMENU.jpg') 
        bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
        
        
        screen.blit(bg,[0,0])
        
 
        mx, my = pygame.mouse.get_pos()

        #LEBAR: (WIDTH//2)-(panjanggambar//2)
        #TINGGI: (HEIGHT//2)//mult

        # Ukuran asli: 748 * 108
        # 560
        rectX = math.floor(WIDTH//2)-225
        rectY = math.floor(HEIGHT//2)
        
        #startbutton
        button_1 = pygame.Rect(rectX, math.floor(rectY//2), 450, 80)
        start_button = pygame.image.load('assets/english/Nbuttons/start.png') 
        start_button = pygame.transform.scale(start_button,(450,80))              
        screen.blit(start_button,(rectX, rectY//2))
        start_button_idle = pygame.image.load('assets/english/Nbuttons/Idle_Start.png')
        start_button_idle = pygame.transform.scale(start_button_idle,(450,80))
        
        #settingbutton
        button_2 = pygame.Rect(rectX, math.floor(rectY//1.35), 450, 80)
        setting_button = pygame.image.load('assets/english/Nbuttons/settings.png') 
        setting_button = pygame.transform.scale(setting_button,(450,80))
        screen.blit(setting_button,(rectX, rectY//1.35))
        setting_button_idle = pygame.image.load('assets/english/Nbuttons/Idle_Settings.png') 
        setting_button_idle = pygame.transform.scale(setting_button_idle,(450,80))
        
        #howtobutton
        button_3 = pygame.Rect(rectX, math.floor(rectY), 450, 80)
        help_button = pygame.image.load('assets/english/Nbuttons/howto.png') 
        help_button = pygame.transform.scale(help_button,(450,80))
        screen.blit(help_button,(rectX, rectY))
        help_button_idle = pygame.image.load('assets/english/Nbuttons/Idle_Help.png')
        help_button_idle = pygame.transform.scale(help_button_idle,(450,80))
        

        #exitbutton
        button_4 = pygame.Rect(rectX, math.floor(rectY//0.8), 450, 80)
        quit_button = pygame.image.load('assets/english/Nbuttons/exit.png') 
        quit_button = pygame.transform.scale(quit_button,(450,80))
        screen.blit(quit_button,(rectX, rectY//(0.8)))
        quit_button_idle = pygame.image.load('assets/english/Nbuttons/Idle_Exit.png')
        quit_button_idle = pygame.transform.scale(quit_button_idle,(450,80))
        
        #indoflag
        button_5 = pygame.Rect((int(10*WIDTH//12-40),(int(10*HEIGHT//11))),(180,80))
        flag_indo = pygame.image.load('assets/Flag/Flag_English.png')
        flag_indo = pygame.transform.scale(flag_indo, (750,80))
        screen.blit(flag_indo, ((int(10*WIDTH//12-320),(int(10*HEIGHT//11)))))
        
        
        
        if button_1.collidepoint((mx, my)):
            screen.blit(start_button_idle, (rectX, rectY//2))
            if click:
                
                start()
                #Running = False
        if button_2.collidepoint((mx, my)):
            screen.blit(setting_button_idle,(rectX, rectY//1.35))

            if click:
                
                setting()
        if button_3.collidepoint((mx, my)):
            
            screen.blit(help_button_idle,(rectX, rectY))
            if click:
                game_help()

        if button_5.collidepoint((mx,my)):
            if click:
                game_lang()
                
        
                
        if button_4.collidepoint((mx, my)):
            screen.blit(quit_button_idle,(rectX, rectY//(0.8)))
            if click:
                game_exit()
            
        
        '''
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        '''
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                pygame.quit()
                break
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def start():
    pygame.mixer.music.stop()
    ringoftrivia.main()
    '''
    click = False
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('START', font, (255, 255, 255), screen, 420, 60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
                    break
        pygame.display.update()
        mainClock.tick(60)
    '''
    
        
def setting():
    global isMuteMusic
    global isMuteSFX

    global prev_music
    global prev_sfx

    temp_music = 0.6    

    BONVENOCF = pygame.font.Font("assets/bonvenocf.otf",32)

    percent_100 = pygame.image.load('assets/english/Settings/Percent/Percent_100.png')
    percent_100 = pygame.transform.scale(percent_100,(126,60))
    percent_80 = pygame.image.load('assets/english/Settings/Percent/Percent_80.png')
    percent_80 = pygame.transform.scale(percent_80,(126,60))
    percent_60 = pygame.image.load('assets/english/Settings/Percent/Percent_60.png')
    percent_60 = pygame.transform.scale(percent_60,(126,60))
    percent_40 = pygame.image.load('assets/english/Settings/Percent/Percent_40.png')
    percent_40 = pygame.transform.scale(percent_40,(126,60))
    percent_20 = pygame.image.load('assets/english/Settings/Percent/Percent_20.png')
    percent_20 = pygame.transform.scale(percent_20,(126,60))

    running = True
    while running:
        click = False
        
        bgs = pygame.image.load('assets/english/Settings/Settings.png') 
        bgs = pygame.transform.scale(bgs,(720,480))
        tick = pygame.image.load('assets/english/Buttons/tick.png') 
        tick = pygame.transform.scale(tick,(50,50))

        musicup = BONVENOCF.render(str(prev_music),True,(0,0,0))
        music_rect = pygame.Rect((int(WIDTH//2+130),(int(HEIGHT//2-104))),(70,60))
        
        screen.blit(bgs,((int(WIDTH//2)-360), (int(HEIGHT//2)-240)))
        close_rect = pygame.Rect((int(WIDTH//2)+260), (int(HEIGHT//2)-240) ,100,100)

        pygame.mixer.music.set_volume(prev_music)
        
           
        # curSFX = pygame.mixer.music.get_volume() 
        
        
        mx, my = pygame.mouse.get_pos()
        
        button_apply = pygame.Rect(50,200,200,50)
        button_exit = pygame.Rect(50,400,200,50)

        music_mute = pygame.Rect((int(WIDTH//2-297),(int(HEIGHT//2-104))),(30,30))
        sfx_mute = pygame.Rect((int(WIDTH//2-297),(int(HEIGHT//2-5))),(30,30))
        mute_all = pygame.Rect((int(WIDTH//2-297),(int(HEIGHT//2+95))),(30,30))

        sfx_up = pygame.Rect((int(WIDTH//2+105),(int(HEIGHT//2-5))),(30,30))
        sfx_down = pygame.Rect((int(WIDTH//2-90),(int(HEIGHT//2-5))),(30,30))

        music_up = pygame.Rect((int(WIDTH//2+105),(int(HEIGHT//2-104))),(30,30))
        music_down = pygame.Rect((int(WIDTH//2-90),(int(HEIGHT//2-104))),(30,30))

        #pygame.draw.rect(screen, (255,0,0), music_mute)
        #pygame.draw.rect(screen, (255,0,0), sfx_mute)
        #pygame.draw.rect(screen, (255,0,0), mute_all)
        #pygame.draw.rect(screen, (255,0,0), sfx_up)
        #pygame.draw.rect(screen, (0,255,255), sfx_down)
        #pygame.draw.rect(screen, (255,0,0), music_up)
        #pygame.draw.rect(screen, (0,255,255), music_down)
        #pygame.draw.rect(screen, (255,255,255), music_rect)

        if prev_music == 1.0:
            screen.blit(percent_100,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_100 = font.render('100', 1, (0, 0, 0))
            screen.blit(persen_100, (int(WIDTH//2+155),(int(HEIGHT//2-108))))
        elif prev_music == 0.2:
            screen.blit(percent_20,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_20 = font.render('20', 1, (0, 0, 0))
            screen.blit(persen_20, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
        elif prev_music == 0.4:
            screen.blit(percent_40,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_40 = font.render('40', 1, (0, 0, 0))
            screen.blit(persen_40, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
        elif prev_music == 0.6:
            screen.blit(percent_60,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_60 = font.render('60', 1, (0, 0, 0))
            screen.blit(persen_60, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
        elif prev_music == 0.8:
            screen.blit(percent_80,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_80 = font.render('80', 1, (0, 0, 0))
            screen.blit(persen_80, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
        elif isMuteMusic == True and isMuteSFX == True:
            screen.blit(tick,((int(WIDTH//2-305),(int(HEIGHT//2+80))),(10,10)))
            pygame.display.flip()

        #mute 
        if isMuteMusic == True:
            screen.blit(tick,((int(WIDTH//2-305),(int(HEIGHT//2-120))),(10,10)))
            pygame.mixer.music.set_volume(0.0)
                  
        if isMuteSFX == True: #Template
            screen.blit(tick,((int(WIDTH//2-305),(int(HEIGHT//2-20))),(10,10)))
        elif isMuteSFX == False:
            pass
            #pygame.mixer.music.set_volume(prev_sfx)
    

        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        if music_mute.collidepoint((mx,my)):
            if click:               
                if isMuteMusic == False:
                    isMuteMusic = True
                    temp_music = prev_music
                    prev_music = 0
                elif isMuteMusic == True:
                    isMuteMusic = False
                    prev_music = temp_music
                    pygame.mixer.music.set_volume(prev_music)
                    pygame.display.update()

        if sfx_mute.collidepoint((mx,my)): #template
            if click: 
                if isMuteSFX == False:
                    isMuteSFX = True
                elif isMuteSFX == True:
                    isMuteSFX = False
        if mute_all.collidepoint((mx,my)):
            if click:
                if isMuteMusic == True and isMuteSFX == True:
                    isMuteMusic = False
                    prev_music = temp_music
                    pygame.mixer.music.set_volume(prev_music)

                    isMuteSFX = False
                else:
                    isMuteMusic = True
                    temp_music = prev_music
                    prev_music = 0
                    
                    isMuteSFX = True

        if music_up.collidepoint((mx,my)):
            if isMuteMusic == True:
                pass
            elif isMuteMusic == False:
                if click:
                    if prev_music >= 0 and prev_music < 1:
                        prev_music += 0.2
                        prev_music = round(prev_music,1)
                    elif prev_music == 1:
                        pass              
            
        if music_down.collidepoint((mx,my)):
            if isMuteMusic == True:
                pass
            elif isMuteMusic == False:
                if click:
                    if prev_music > 0 and prev_music <= 1:
                        prev_music -= 0.2
                        prev_music = round(prev_music,1)
                    elif prev_music == 0:
                        pass
                               

        if close_rect.collidepoint((mx,my)):
            if click:
                running = False
                main_menu()
                break
 
        pygame.display.update()
        mainClock.tick(60)
 
def game_help():
    click = False
    running = True
    
    POG = pygame.image.load('assets/english/howtoplay/parts.png') 
    POG = pygame.transform.scale(POG,(int(WIDTH*3//4),int(HEIGHT*3//4)))
    HTP = pygame.image.load('assets/english/howtoplay/howtoplay.png') 
    HTP = pygame.transform.scale(HTP,(int(WIDTH*3//4),int(HEIGHT*3//4)))

    page = 1
    
    while running:
        click = False

        screen.fill((0,0,0))
        bg = pygame.image.load('assets/english/bg/ROTMAINMENU.jpg') 
        bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
        screen.blit(bg,[0,0])
        rectX = math.floor(WIDTH//2)-225
        rectY = math.floor(HEIGHT//2)
        button_1 = pygame.Rect(rectX, math.floor(rectY//2), 450, 80)
        start_button = pygame.image.load('assets/english/Nbuttons/start.png') 
        start_button = pygame.transform.scale(start_button,(450,80))
        screen.blit(start_button,(rectX, rectY//2))
            
        button_2 = pygame.Rect(rectX, math.floor(rectY//1.35), 450, 80)
        setting_button = pygame.image.load('assets/english/Nbuttons/settings.png') 
        setting_button = pygame.transform.scale(setting_button,(450,80))
        screen.blit(setting_button,(rectX, rectY//1.35))
        
        button_3 = pygame.Rect(rectX, math.floor(rectY), 450, 80)
        help_button = pygame.image.load('assets/english/Nbuttons/howto.png') 
        help_button = pygame.transform.scale(help_button,(450,80))
        screen.blit(help_button,(rectX, rectY))
        
        button_4 = pygame.Rect(rectX, math.floor(rectY//0.8), 450, 80)
        quit_button = pygame.image.load('assets/english/Nbuttons/exit.png') 
        quit_button = pygame.transform.scale(quit_button,(450,80))
        screen.blit(quit_button,(rectX, rectY//(0.8)))

        POG_rect = pygame.Rect(int(WIDTH//2)-int(WIDTH*3//8) + int(WIDTH*3//4)-100,int(HEIGHT//2)-int(HEIGHT*3//8) +  int(HEIGHT*3//4)-100 ,100,100)
        
        HTP_rect = pygame.Rect(int(WIDTH//2)-int(WIDTH*3//8) ,int(HEIGHT//2)-int(HEIGHT*3//8) +  int(HEIGHT*3//4)-100 ,100,100)        

        close_rect = pygame.Rect(int(WIDTH//2)-int(WIDTH*3//8) + int(WIDTH*3//4)-100,int(HEIGHT//2)-int(HEIGHT*3//8) ,100,100)
        
        if page == 1:
            screen.blit(POG,((int(WIDTH//2)-int(WIDTH*3//8)), (int(HEIGHT//2)-int(HEIGHT*3//8))))
            
            
        elif page == 2:
            screen.blit(HTP,((int(WIDTH//2)-int(WIDTH*3//8)), (int(HEIGHT//2)-int(HEIGHT*3//8))))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        mx, my = pygame.mouse.get_pos()
        if POG_rect.collidepoint((mx,my)):
            if click:                   
                page+=1
                     
        elif HTP_rect.collidepoint((mx,my)):
            if click:
                page-=1
        if close_rect.collidepoint((mx,my)):
            if click:
                running = False
                main_menu()
                break
        
        pygame.display.update()
        mainClock.tick(60)

def game_lang():
    
    mainmenu_indo.main_menu()
    

def game_exit():
    running = False
    pygame.quit()
    sys.exit()



# Main 


if __name__ == "__main__":
    main_menu()




"""
Update Notes:
- 14/11/2020 [PM 9:26] Created Repl <- Pangestu
- 15/11/2020 [AM 11:26] Changed help() to game_help() to preserve 
consistency <- Marvin
- 15/11/2020 [PM 9:38] Added Start,Setting,Help Button <= Pangestu
- 15/11/2020 [PM 10:35] Button positioned <- Marvin
- 15/11/2020 [PM 11:16] Removed Red Box <= Pangestu
- 16/11/2020 [PM 9:13] Added "Newcomer checker" <- Marvin
- 17/11/2020 [PM 7:18] Fixed "Newcomer checker" bug and added responsivity for background image <- Marvin
- 20/11/2020 [PM 4:50] Connected main menu to game <- Marvin
- 21/11/2020 [PM 11:03] Updated the Mainmenu BG <- Pangestu
- 23/11/2020 [PM 9:11] Updated main menu buttons <- Pangestu
- 24/11/2020 [PM 4:35] Added BGM to main menu <- Pangestu
- 26/11/2020 [PM 11:59] Added settings, and debugged main menu sounds <- Pangestu
- 28/11/2020 [PM 11:32] MENU NEARLY DONE <- Pangestu
- 13/12/2020 [AM 8:39] Fix blinking tick <- Marvin

"""
"""
Bugs to be fixed:
- Red box [Issue resolved]
"""
