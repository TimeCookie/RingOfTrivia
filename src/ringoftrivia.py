
import sys
import pygame
import random
import mainmenu
import mainmenu_indo
import time

'''
Notes:
- 
'''


pygame.init()
screen = pygame.display.set_mode((0,0))
#screen = pygame.display.set_mode((720,480)) #test code for a smaller 16:9
WIDTH, HEIGHT = pygame.display.get_surface().get_size()

answer_A = pygame.Rect(((WIDTH//2)-(WIDTH*9//32),(HEIGHT//2)-35),(WIDTH*9//16,50))
answer_B = pygame.Rect(((WIDTH//2)-(WIDTH*9//32),(HEIGHT//2)+25),(WIDTH*9//16,50))
answer_C = pygame.Rect(((WIDTH//2)-(WIDTH*9//32),(HEIGHT//2)+85),(WIDTH*9//16,50))
answer_D = pygame.Rect(((WIDTH//2)-(WIDTH*9//32),(HEIGHT//2)+150),(WIDTH*9//16,50))

isMuteMusic = False
isMuteSFX = False

font = pygame.font.SysFont(None, 45)

prev_music = 0.6 #default volume for music
prev_sfx = 0.6 #default volume for sfx

curAns = ""

pygame.mixer.init()
bgm = pygame.mixer.music.load("assets/sounds/mainmenu.ogg") 
pygame.mixer.music.play()


# Datas
questions = {'E':[("Who is the most subscribed channel on YouTube as of 2020","B","PewDiePie","T-Series","nigahiga","Markiplier"),
                  ("Which of these awards honor outstanding achievements in television?","A","Emmys","Grammys","Oscars","Tonys"),
                  ("Which of these awards honor outstanding achievements in music recording?","C","Tonys","Emmys","Grammys","Oscars"),
                  ("What is Disney first ever feature animated film?","B","Fantasia","Snow White and The Seven Dwarfs","Bambi","Dumbo"),
                  ("What is the longest running animated TV show still on air?","D","Arthur","Power Rangers","South Park","The Simpsons")],
                 'G':[("Where is the highest point on Earth's surface measured from sea level?","B","Mt. Kilimanjaro","Mt. Everest","Mt. Chimborazo","Mt. Mauna Kea"),
                      ("What is the largest lake in the world?","A","Lake Caspian Sea","Lake Baikal","Lake Victoria","Lake Superior"),
                      ("What is the biggest island in the world?","B","Borneo","Greenland","Madagascar","New Guinea"),
                      ("What is a formation of a single massive rock called?", "D","Canyon","Bluff","Mountain","Monolith"),
                      ("Who was the father of geography?","C","Aristotle","Pythagoras","Eratosthenes","Virgil")],
                 'N':[("What are the scientific name of humans?","A","Homo Sapiens","Homo Erectus","Neanderthals","Australopithecus afarensis"),
                      ("Which of these is used to describe unrenewable energy?","D","Artificial Fuel","Natural Fuel","Bio Fuel","Fossil Fuel"),
                      ("How many gasses are present in the periodic table?","C","4","5","6","7"),
                      ("What continent was first inhabitated by early humans?","B","Asia","Africa","Europe","Australia"),
                      ("Who proposed the Theory of Relativity?","B","Stephen Hawking","Albert Einstein","Issac Newton","Nikola Tesla")],
                 'H':[("What year did World War 2 started, after German forces invaded Poland?","C","1935","1937","1939","1941"),
                      ("From what century did the Renaissance considered lasted?","B","13th-16th Century","14th-17th Century","15th-18th Century","16th-19th Century"),
                      ("What is the most deadly pandemic to ever occur in human history?","B","HIV/AIDS","Bubonic Plague","Spanish Flu","COVID-19"),
                      ("What empire was considered the largest of all time based on continuous land size?","A","Mongol Empire","Russian Empire","Qing Dynasty","British Empire"),
                      ("What civilization is considered the world's oldest civilization according to evidence?","C","Egyptian","Indus Valley","Mesopotamian","Chinese")],
                 'S':[("What sport is considered the biggest sport in the world based on popularity in 2020?","A","Football","Cricket","Tennis","Basketball"),
                      ("What Olympics did world fastest man Usain Bolt first appeared in?","B","Sydney 2000","Athens 2004","Beijing 2008","London 2012"),
                      ("What one athlete has the most Olympic medals of all time?","C","Usain Bolt","Larisa Latynina","Michael Phelps","Marit Bjørgen"),
                      ("Who was the founder of WWF (a.k.a WWE)","C","Roderick J. McMahon","Vincent J. McMahon","Vincent K. McMahon","Shane B. McMahon"),
                      ("Which country has won the most amount of olympic medals?","A","United States of America","Russia","Germany","China")],
                 'A':[("Who is the writer for the book series Call of Cthulu and its mythos?","D","J.K. Rowling","G. R. R. Martin","J. R. R. Tolkien","H. P. Lovecraft"),
                      ("Where was the famous painter Pablo Picasso born?","B","France","Spain","Italy","Portugal"),
                      ("Where is the painting of Mona Lisa by Leonardo Da Vinci currently displayed at?","A","Louvre, Paris","Rijksmuseum, Amsterdam","Gallerie dell’Accademia, Florence","Museum of Natural History, Vienna"),
                      ("Forms of poetry consisting of six stanzas of six lines each.","B","Free verse","Sestina","Sonnet","Epic"),
                      ("Which of these below is the work of H. G. Wells?","A","Time Machine","The Adventures of Huckleberry Finn","Crime and Punishment","The Metamorphosis")]}

picked = {'E':[],
            'G':[],
            'N':[],
            'H':[],
            'S':[],
            'A':[]}

class Characters:
    def __init__(self,posX,posY):
        self.__x = posX
        self.__y = posY
        self.block = 0
    # Setters
    def draw(player,x,y):
        screen.blit(player,(x,y))
    def move(self,velX,velY):
        self.__x += velX
        self.__y += velY
        self.block +=1
    # Getters
    def get_player_x(self):
        return int(self.__x)
    
    def get_player_y(self):
        return int(self.__y)
    def get_player_block(self):
        return self.block


def draw_board():
    board = pygame.image.load("assets/english/bg/ROT-2D.jpg")
    board = pygame.transform.scale(board,(WIDTH,HEIGHT))

    gear = pygame.image.load("assets/english/Extra/Options.png")
    gear = pygame.transform.scale(gear,(int(WIDTH//16),int(HEIGHT//9)))

    screen.blit(board,[0,0])
    screen.blit(gear,(int(10*WIDTH//11),int(HEIGHT//22)))
    
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rectangle = pygame.Rect(rect)
    y = rectangle.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rectangle.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rectangle.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rectangle.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]
    return text


def draw_question_board():
    question_board = pygame.image.load("assets/Questions/Questions_Based.png")
    question_board = pygame.transform.scale(question_board,(WIDTH*9//16,HEIGHT*9//16))
    screen.blit(question_board,((WIDTH//2)-(WIDTH*9//32),(HEIGHT//2)-(HEIGHT*9//32)))

    

def add_question(category,player,question_pack,randomizer):
    global curAns
    
    text = pygame.font.Font("assets/expressway.ttf",19)

    

    category = category.upper()
    player = player.upper()
    
    q_container = pygame.Rect(((WIDTH//2)-280,(HEIGHT//2)-195),((WIDTH*9//16)-200,(HEIGHT*9//16)-280))

    


    #pygame.draw.rect(screen,(255,0,0),answer_A)
    #pygame.draw.rect(screen,(0,255,0),answer_B)
    #pygame.draw.rect(screen,(0,0,255),answer_C)
    #pygame.draw.rect(screen,(0,0,0),answer_D)
        

    # Unpackaging
    question_question = question_pack[0]
    curAns = question_pack[1]
    question_choice_A = question_pack[2]
    question_choice_B = question_pack[3]
    question_choice_C = question_pack[4]
    question_choice_D = question_pack[5]
    if player == "RED":
            
            
        e_question = text.render(str(question_question),True,(255,0,0))
        e_A = text.render(str(question_choice_A),True,(255,0,0))
        e_B = text.render(str(question_choice_B),True,(255,0,0))
        e_C = text.render(str(question_choice_C),True,(255,0,0))
        e_D = text.render(str(question_choice_D),True,(255,0,0))
    elif player == "BLUE":
            
        e_question = text.render(str(question_question),True,(0,0,255))
        e_A = text.render(str(question_choice_A),True,(0,0,255))
        e_B = text.render(str(question_choice_B),True,(0,0,255))
        e_C = text.render(str(question_choice_C),True,(0,0,255))
        e_D = text.render(str(question_choice_D),True,(0,0,255))

        
    e_A_rect = e_A.get_rect()
    e_B_rect = e_B.get_rect()
    e_C_rect = e_C.get_rect()
    e_D_rect = e_D.get_rect()

    e_A_rect = e_A_rect.move((WIDTH//3)-50,(HEIGHT//2)-25)
    e_B_rect = e_B_rect.move((WIDTH//3)-50,(HEIGHT//2)+40)
    e_C_rect = e_C_rect.move((WIDTH//3)-50,(HEIGHT//2)+100)
    e_D_rect = e_D_rect.move((WIDTH//3)-50,(HEIGHT//2)+160)
        
        
    #screen.blit(e_question,q_container)
    if player == "RED":
        drawText(screen,str(question_question),(255,0,0),q_container,text)
        #red_q = text.render(red_q,True,(255,0,0))
    elif player == "BLUE":
        drawText(screen,str(question_question),(0,0,255),q_container,text)
    screen.blit(e_A,e_A_rect)
    screen.blit(e_B,e_B_rect)
    screen.blit(e_C,e_C_rect)
    screen.blit(e_D,e_D_rect)

        
        

    '''
        Do the same for the other categories
    '''
    '''    
    if category == "G":
        pass
    if category == "N":
        pass
    if category == "H":
        pass
    if category == "S":
        pass
    if category == "A":
        pass

    '''
def settings():
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
            #pygame.display.flip()
        elif prev_music == 0.2:
            screen.blit(percent_20,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_20 = font.render('20', 1, (0, 0, 0))
            screen.blit(persen_20, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
            #pygame.display.flip()
        elif prev_music == 0.4:
            screen.blit(percent_40,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_40 = font.render('40', 1, (0, 0, 0))
            screen.blit(persen_40, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
            #pygame.display.flip()
        elif prev_music == 0.6:
            screen.blit(percent_60,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_60 = font.render('60', 1, (0, 0, 0))
            screen.blit(persen_60, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
            #pygame.display.flip()
        elif prev_music == 0.8:
            screen.blit(percent_80,(int(WIDTH//2-40),(int(HEIGHT//2-130))))
            persen_80 = font.render('80', 1, (0, 0, 0))
            screen.blit(persen_80, (int(WIDTH//2+166),(int(HEIGHT//2-108))))
            #pygame.display.flip()
            
        #mute 
        if isMuteMusic == True:
            screen.blit(tick,((int(WIDTH//2-305),(int(HEIGHT//2-120))),(10,10)))
            prev_music = 0
            pygame.mixer.music.set_volume(0.0)
  
        
        if isMuteSFX == True: #Template
            screen.blit(tick,((int(WIDTH//2-305),(int(HEIGHT//2-20))),(10,10)))
    

        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
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
                    #pygame.display.update()

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
                break
 
        pygame.display.update()



#def end_game():
    
def main():
    global isMuteMusic
    # Parameters
    
    turn = 1
    isClicked = False
    firstTurn = True
    running = True

    # Presets
    
    BONVENOCF = pygame.font.Font("assets/bonvenocf.otf",64)
    draw_board()

    category = {'E':[(1,1),(1,7),(2,2),(2,8),(3,4),(3,10),(4,5)], # entertainment
                'G':[(1,2),(1,8),(2,3),(2,9),(3,5),(3,11),(4,6)], # geography
                'N':[(1,3),(1,9),(2,4),(2,10),(3,6),(4,1),(4,7)], # nature and science
                'H':[(1,4),(1,10),(2,5),(3,1),(3,7),(4,2),(4,8)], # history
                'S':[(1,5),(1,11),(2,6),(3,2),(3,8),(4,3),(4,9)], # sports
                'A':[(1,6),(2,1),(2,7),(3,3),(3,9),(4,4),(4,10)]} # art and literature

    
    
    dice_1 = pygame.image.load("assets/dices/Dice_1.png")
    dice_2 = pygame.image.load("assets/dices/Dice_2.png")
    dice_3 = pygame.image.load("assets/dices/Dice_3.png")
    dice_4 = pygame.image.load("assets/dices/Dice_4.png")
    dice_5 = pygame.image.load("assets/dices/Dice_5.png")
    dice_6 = pygame.image.load("assets/dices/Dice_6.png")

    dice_1 = pygame.transform.scale(dice_1,(200,200))
    dice_2 = pygame.transform.scale(dice_2,(200,200))
    dice_3 = pygame.transform.scale(dice_3,(200,200))
    dice_4 = pygame.transform.scale(dice_4,(200,200))
    dice_5 = pygame.transform.scale(dice_5,(200,200))
    dice_6 = pygame.transform.scale(dice_6,(200,200))

    turn_box = pygame.image.load("assets/english/Extra/Timer.png")
    turn_box = pygame.transform.scale(turn_box,(int(WIDTH//6),int(HEIGHT//6)))
    turn_box_cover = pygame.Rect((int(WIDTH//10),int(4*HEIGHT//5)),(200,150))
    pygame.draw.rect(screen,(255,255,255),turn_box_cover)

    setting = pygame.Rect(int(10*WIDTH//11),int(HEIGHT//22),int(WIDTH//16),int(HEIGHT//9))

    turns = BONVENOCF.render(str(turn),True,(0,0,0))
    
    
    screen.blit(turns,turn_box_cover)

    redWin = pygame.image.load("assets/winlose/p1w.png")
    blueWin = pygame.image.load("assets/winlose/p2w.png")

    redWin = pygame.transform.scale(redWin,(int(WIDTH//2),int(HEIGHT//2)))
    blueWin = pygame.transform.scale(blueWin,(int(WIDTH//2),int(HEIGHT//2)))

    draw_game = pygame.image.load("assets/winlose/draw.png")
    draw_game = pygame.transform.scale(draw_game,(int(WIDTH//2),int(HEIGHT//2)))

    red_pawn = pygame.image.load("assets/Pawn/red.png")
    blue_pawn = pygame.image.load("assets/Pawn/blue.png")

    red_pawn = pygame.transform.scale(red_pawn,(int(HEIGHT//10),int(HEIGHT//10)))
    blue_pawn = pygame.transform.scale(blue_pawn,(int(HEIGHT//10),int(HEIGHT//10)))


    redX = int(3/4*WIDTH) - 60
    redY = int(3/4*HEIGHT) + 55

    blueX = int(1/4*WIDTH)-10
    blueY = 10

    redPts = 0
    bluePts = 0

    redPts_text = BONVENOCF.render(str(redPts),True,(0,0,0))
    bluePts_text = BONVENOCF.render(str(bluePts),True,(0,0,0))

    redPts_rect = redPts_text.get_rect()
    bluePts_rect = bluePts_text.get_rect()
    #redX = int(3/4*WIDTH) - 60
    #redY = int(3/4*HEIGHT) + 55

    redPts_rect = redPts_rect.move(redX-54*4.5, redY-53*2.5)
    bluePts_rect = bluePts_rect.move(blueX+60*4.5, blueY+62*2.5)


    player_1 = Characters(redX,redY)
    player_2 = Characters(blueX,blueY)
        
    
    # Dice
    dice = pygame.image.load("assets/dices/dice_Circle.png")
    dice = pygame.transform.scale(dice,(int(WIDTH//7),int(HEIGHT//5.5)))
    dice_pos = pygame.Rect(((int(5/6*WIDTH)),(int(4/5*HEIGHT)-25)),(280,200))


    
    screen.blit(red_pawn,(redX,redY)) # 1080p x-132 (3.5cm), 1366x768 x-94 (2.5cm)
    screen.blit(blue_pawn,(blueX,blueY))

    screen.blit(redPts_text,redPts_rect)
    screen.blit(bluePts_text,bluePts_rect)


    def changeLane(player, checker, remainder, curLane):
        # move to the 11th block first
        player = player.upper()
        if player == "RED":
            if curLane == 1:
                player_1._Characters__x -= checker * 58
            elif curLane == 2:
                player_1._Characters__y -= checker * 58
            elif curLane == 3:
                player_1._Characters__x += checker * 58
            elif curLane == 4:
                player_1._Characters__y += checker * 58

            if curLane == 4:
                curLane = 1
            else:
                curLane += 1

            # then change lane
            if curLane == 1:
                player_1._Characters__x -= remainder * 58
                player_1.block += remainder
            elif curLane == 2:
                player_1._Characters__y -= remainder * 58
                player_1.block += remainder
            elif curLane == 3:
                player_1._Characters__x += remainder * 58
                player_1.block += remainder
            elif curLane == 4:
                player_1._Characters__y += remainder * 58
                player_1.block += remainder
                
        elif player == "BLUE":
            if curLane == 1:
                player_2._Characters__x -= checker * 58
            elif curLane == 2:
                player_2._Characters__y -= checker * 58
            elif curLane == 3:
                player_2._Characters__x += checker * 58
            elif curLane == 4:
                player_2._Characters__y += checker * 58

            if curLane == 4:
                curLane = 1
            else:
                curLane += 1

            # then change lane
            if curLane == 1:
                player_2._Characters__x -= remainder * 58
                player_2.block += remainder
            elif curLane == 2:
                player_2._Characters__y -= remainder * 58
                player_2.block += remainder
            elif curLane == 3:
                player_2._Characters__x += remainder * 58
                player_2.block += remainder
            elif curLane == 4:
                player_2._Characters__y += remainder * 58
                player_2.block += remainder




    '''
    score_container = pygame.Rect((WIDTH//2)-75,(HEIGHT//2)-50,150,100)
    
    
    x1 = y1 = 0
    x2 = WIDTH-100
    y2 = HEIGHT-50

    # Main loop
    while running:
        sixes = 0
        if turn == 4:
                turn = 0
        
        roll_dice = qRNG.randomize(1,6,0) # dice randomizer
        roll_dice = int(roll_dice[0]) # converting the value to integer
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(255,255,255),score_container)
        screen.blit(text,textContainer)

        mouse_x,mouse_y = pygame.mouse.get_pos()

        if textContainer.collidepoint((mouse_x,mouse_y)):
                if isClicked:
                        dice_number = str(roll_dice)
                        diceNumText = font.render(dice_number,True,(0,0,0),(255,255,255))
                        screen.blit(diceNumText,score_container)
    '''
    red_curLane = 1
    blue_curLane = 3
    gameTurn = 0
    
    answer = ""
    redCategory = ""
    blueCategory = ""

    whoseTurn = "RED" # turns (in word)
    showQuestion = False
    while running:
        isClicked = False
                
        if gameTurn > 5:
            showQuestion = False
            

        if turn % 2 == 0:
            whoseTurn = "RED"
        elif turn % 2 != 0:
            whoseTurn = "BLUE"

        
        
        screen.fill((0,0,0)) # Reload


        # Code goes below here


            

        turns = BONVENOCF.render(str(gameTurn),True,(0,0,0))

        redX = player_1.get_player_x()
        redY = player_1.get_player_y()

        blueX = player_2.get_player_x()
        blueY = player_2.get_player_y()

        redPos = player_1.block
        bluePos = player_2.block

        
        
        draw_board()
        # screen.blit(dice,dice_pos)
        # screen.blit(turn_box, (12,int(5*HEIGHT//6)))
        screen.blit(red_pawn,(redX,redY))
        screen.blit(blue_pawn,(blueX,blueY))
        screen.blit(turns,turn_box_cover)

        
        

        roll_dice = random.randint(1,6) # Dice randomizer

        # Checkers
        red_check = 11-(redPos)
        blue_check = 11-(bluePos)
        mx, my = pygame.mouse.get_pos()

        
            

        # Event handler
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        prev_lang = open("curlang.txt","r")
                        curLang = prev_lang.read()
                        prev_lang.close()

                        if curLang == "indonesia":
                            mainmenu_indo.main_menu()
                        elif curLang == "english":
                            mainmenu.main_menu()
                        else:
                            mainmenu.main_menu()
                            
                        running = False
                        sys.exit()
                        break
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            prev_lang = open("curlang.txt","r")
                            curLang = prev_lang.read()
                            prev_lang.close()

                            if curLang == "indonesia":
                                mainmenu_indo.main_menu()
                            elif curLang == "english":
                                mainmenu.main_menu()
                            else:
                                mainmenu.main_menu()
                                
                            running = False
                            sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                isClicked = True

        redPts_text = BONVENOCF.render(str(redPts),True,(0,0,0))
        bluePts_text = BONVENOCF.render(str(bluePts),True,(0,0,0))
        
        screen.blit(redPts_text,redPts_rect)
        screen.blit(bluePts_text,bluePts_rect)
        if showQuestion == True:

            print(whoseTurn)
            print(len(questions['E']))
            print(len(questions['G']))
            print(len(questions['N']))
            print(len(questions['H']))
            print(len(questions['S']))
            print(len(questions['A']))
            if whoseTurn == "BLUE":
                draw_category = blueCategory
                question_pack = blue_question_pack
                draw_player = "blue"
            elif whoseTurn == "RED":
                draw_category = redCategory
                question_pack = red_question_pack
                draw_player = "red"

            draw_question_board()
            add_question(draw_category,draw_player,question_pack,randomizer)

            if answer_A.collidepoint((mx,my)):
                if isClicked:
                    if curAns != "A":
                        print("Wrong!")
                        showQuestion = False
                    elif curAns == "A":
                        print("Correct!")
                        if whoseTurn == "BLUE":
                            bluePts += 1
                        elif whoseTurn == "RED":
                            redPts += 1
                        showQuestion = False
            if answer_B.collidepoint((mx,my)):
                if isClicked:
                    if curAns != "B":
                        print("Wrong!")
                        showQuestion = False
                    elif curAns == "B":
                        print("Correct!")
                        if whoseTurn == "BLUE":
                            bluePts += 1
                        elif whoseTurn == "RED":
                            redPts += 1
                        showQuestion = False
            if answer_C.collidepoint((mx,my)):
                if isClicked:
                    if curAns != "C":
                        print("Wrong!")
                        showQuestion = False
                    elif curAns == "C":
                        print("Correct!")
                        if whoseTurn == "BLUE":
                            bluePts += 1
                        elif whoseTurn == "RED":
                            redPts += 1
                        showQuestion = False
            if answer_D.collidepoint((mx,my)):
                if isClicked:
                    if curAns != "D":
                        print("Wrong!")
                        showQuestion = False
                    elif curAns == "D":
                        print("Correct!")
                        if whoseTurn == "BLUE":
                            bluePts += 1
                        elif whoseTurn == "RED":
                            redPts += 1
                        showQuestion = False
            '''
            if turn-1 % 2 != 0: #Red
                draw_question_board()
                add_question(redCategory,"red",questions)
                if answer_A.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "A":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "A":
                            print("Correct!")
                            showQuestion = False
                            redPts += 1
                        
                        print(redPts)
                        print(curAns)
                        print("Clicked A")
                if answer_B.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "B":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "B":
                            print("Correct!")
                            showQuestion = False
                            redPts += 1
                        
                        print(redPts)
                        print(curAns)
                        print("Clicked B")
                if answer_C.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "C":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "C":
                            print("Correct!")
                            showQuestion = False
                            redPts += 1

                        print(redPts)
                        print(curAns)
                        print("Clicked C")
                if answer_D.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "D":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "D":
                            print("Correct!")
                            showQuestion = False
                            redPts += 1
                        print(redPts)
                        print(curAns)
                        print("Clicked D")
                #print("Red")
            elif turn-1 % 2 == 0: #Blue
                draw_question_board()
                add_question(blueCategory,"blue",questions)
                if answer_A.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "A":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "A":
                            print("Correct!")
                            showQuestion = False
                            bluePts += 1
                        
                        print(redPts)
                        print(curAns)
                        print("Clicked A")
                if answer_B.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "B":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "B":
                            print("Correct!")
                            showQuestion = False
                            bluePts += 1
                        
                        print(redPts)
                        print(curAns)
                        print("Clicked B")
                if answer_C.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "C":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "C":
                            print("Correct!")
                            showQuestion = False
                            bluePts += 1

                        print(redPts)
                        print(curAns)
                        print("Clicked C")
                if answer_D.collidepoint((mx,my)):
                    if isClicked:
                        
                        if curAns != "D":
                            print("Wrong!")
                            showQuestion = False
                        elif curAns == "D":
                            print("Correct!")
                            showQuestion = False
                            bluePts += 1
                        print(redPts)
                        print(curAns)
                        print("Clicked D")
                #print("Blue")
            '''
        elif showQuestion == False:
            pass

        
        if gameTurn > 5:

            prev_lang = open("curlang.txt","r")
            curLang = prev_lang.read()
            prev_lang.close()
            
            if redPts > bluePts:
                print("Red wins")
                screen.blit(redWin,(int(WIDTH//2)-int(WIDTH//4),int(HEIGHT//2)-int(HEIGHT//4)))
                pygame.display.update()
                time.sleep(5)

                if curLang == "indonesia":
                    mainmenu_indo.main_menu()
                elif curLang == "english":
                    mainmenu.main_menu()
                else:
                    mainmenu.main_menu()
                    
                running = False
                break
                
            elif bluePts > redPts:
                print("Blue wins")
                screen.blit(blueWin,(int(WIDTH//2)-int(WIDTH//4),int(HEIGHT//2)-int(HEIGHT)//4))
                pygame.display.update()
                time.sleep(5)

                if curLang == "indonesia":
                    mainmenu_indo.main_menu()
                elif curLang == "english":
                    mainmenu.main_menu()
                else:
                    mainmenu.main_menu()
                    
                running = False
                break
            elif bluePts == redPts:
                print("Draw")
                screen.blit(draw_game,(int(WIDTH//2)-int(WIDTH//4),int(HEIGHT//2)-int(HEIGHT)//4))
                pygame.display.update()
                time.sleep(5)

                if curLang == "indonesia":
                    mainmenu_indo.main_menu()
                elif curLang == "english":
                    mainmenu.main_menu()
                else:
                    mainmenu.main_menu()
                running = False
                break

        
        # 1 block = +/- 68px for lane 1                     
        if dice_pos.collidepoint((mx,my)):
            if showQuestion == True:
                pass
            elif gameTurn > 5:
                continue
            elif isClicked:
                if turn % 2 != 0:
                    gameTurn += 1

                # Draw dice
                if roll_dice == 1:
                    screen.blit(dice_1,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                elif roll_dice == 2:
                    screen.blit(dice_2,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                elif roll_dice == 3:
                    screen.blit(dice_3,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                elif roll_dice == 4:
                    screen.blit(dice_4,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                elif roll_dice == 5:
                    screen.blit(dice_5,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                elif roll_dice == 6:
                    screen.blit(dice_6,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(1)
                    
                if turn % 2 != 0: # red's turn
                    if red_curLane == blue_curLane:
                        if player_1.block == player_2.block:
                            mainmenu.main_menu()
                            running = False
                            sys.exit()
                            
                    if roll_dice > red_check:
                        remainder = roll_dice - red_check
                        player_1.block = 0
                        changeLane("red",red_check,remainder,red_curLane)

                        if red_curLane == 4:
                            red_curLane = 1
                        else:
                            red_curLane += 1
                    
                        
                    else:
                        if red_curLane == 1:
                            player_1._Characters__x -= 58 * roll_dice
                            player_1.block += roll_dice
                        elif red_curLane == 2:
                            player_1._Characters__y -= 58 * roll_dice
                            player_1.block += roll_dice
                        elif red_curLane == 3:
                            player_1._Characters__x += (58 * roll_dice)
                            player_1.block += roll_dice
                        elif red_curLane == 4:
                            player_1._Characters__y += 58 * roll_dice
                            player_1.block += roll_dice
                    

                    currentPos = (red_curLane,int(player_1.block))

                    if currentPos in category['E']:
                        redCategory = "E"
                        print("Red is E")
                    elif currentPos in category['G']:
                        redCategory = "G"
                    elif currentPos in category['N']:
                        redCategory = "N"
                    elif currentPos in category['H']:
                        redCategory = "H"
                    elif currentPos in category['S']:
                        redCategory = "S"
                    elif currentPos in category['A']:
                        redCategory = "A"

                    randomizer = random.randint(0,len(questions[redCategory])-1) #randomize the question
                    red_question_pack = questions[redCategory][randomizer]
                    questions[redCategory].pop(randomizer)

                    pygame.display.update()
                        
                    
                elif turn % 2 == 0:
                    if roll_dice > blue_check:
                        remainder = roll_dice - blue_check
                        player_2.block = 0
                        changeLane("blue",blue_check,remainder,blue_curLane) # doesn't seem to be working when it is executed

                        if blue_curLane == 4:
                            blue_curLane = 1
                        else:
                            blue_curLane += 1
                    else:
                        if blue_curLane == 1:
                            player_2._Characters__x -= 58 * roll_dice
                            player_2.block += roll_dice
                        elif blue_curLane == 2:
                            player_2._Characters__y -= 58 * roll_dice
                            player_2.block += roll_dice
                        elif blue_curLane == 3:
                            player_2._Characters__x += (58 * roll_dice)
                            player_2.block += roll_dice
                        elif blue_curLane == 4:
                            player_2._Characters__y += 58 * roll_dice
                            player_2.block += roll_dice
                    

                    currentPos = (blue_curLane,int(player_2.block))
                    
                    if currentPos in category['E']:
                        blueCategory = "E"
                    elif currentPos in category['G']:
                        blueCategory = "G"
                    elif currentPos in category['N']:
                        blueCategory = "N"
                    elif currentPos in category['H']:
                        blueCategory = "H"
                    elif currentPos in category['S']:
                        blueCategory = "S"
                    elif currentPos in category['A']:
                        blueCategory = "A"

                    randomizer = random.randint(0,len(questions[blueCategory])-1) #randomize the question
                    blue_question_pack = questions[blueCategory][randomizer]
                    questions[blueCategory].pop(randomizer)
                    pygame.display.update()

                showQuestion = True
                # add_question(category,player)

                
                turn+=1
        if setting.collidepoint((mx,my)):
            if isClicked:
                settings()

                        
                        
                        
                '''
                if roll_dice == 1:
                    screen.blit(dice_1,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(2)
                    #character move
                elif roll_dice == 2:
                    screen.blit(dice_2,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()      
                    time.sleep(2)
                    #character move
                elif roll_dice == 3:
                    screen.blit(dice_3,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(2)
                    #character move
                elif roll_dice == 4:
                    screen.blit(dice_4,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(2)
                    #character move
                elif roll_dice == 5:
                    screen.blit(dice_5,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(2)
                    #character move
                elif roll_dice == 6:
                    screen.blit(dice_6,(int(WIDTH//2)-100,int(HEIGHT//2)-175))
                    pygame.display.update()
                    time.sleep(2)
                    #character move
                '''
           
        pygame.display.update()
        


if __name__ == "__main__":
    main()
    # script goes here

"""
Notes:
- 15/11/2020 [AM 12:02] Code rewrite and improved readability <- Marvin
- 15/11/2020 [PM 12:06] Added player class 'Characters' <- Marvin
- 20/11/2020 [PM 4:53] Connected game to main menu <- Marvin
- 22/11/2020 [PM 11:42] Applied design to game <- Marvin
- 23/11/2020 [AM 12:16] Debugging dice system <- Marvin
- 23/11/2020 [PM 2:45] Resolved dice design error <- Marvin
- 25/11/2020 [PM 8:18] Used the random module instead <- Marvin
- 26/11/2020 [AM 12:03] Re-applied new board design <- Marvin
- 27/11/2020 [PM 12:35] Improved responsivity across all 16:9 resolution <- Marvin
- 02/12/2020 [PM 10:48] Added all character movements <- Marvin
- 04/12/2020 [PM 12:05] Fixed player 2's odd movement <- Marvin
- 05/12/2020 [AM 11:49] Added card category's checker <- Marvin
- 08/12/2020 [PM 7:00] Changed board <- Marvin
- 10/12/2020 [PM 9:26] Fixed player 2's score stuck <- Marvin
- 11/12/2020 [PM 1:59] Rearranging some objects' z-indeces, Added question randomizer <- Marvin
- 12/12/2020 [PM 8:19] Questions now auto-removes when already picked, New algorithm to increase code effieciency <- Marvin
"""

"""
Bugs to be fixed:
- AttributeError [Issue resolved]
- Unblittable surface [Issue resolved]
- Unclickable image [Issue resolved]
- Removing blitted images [Issue resolved]
- Character cyclic movement [Issue resolved]
- Player 2's odd movement [Issue resolved]
- Blitting text to question board [Issue resolved]
- Randomizing question [Issue resolved]
"""


"""
Idea to add if time permits:
- Animations
"""
