import pygame,sys,random,time
import pygame.event as GAME_EVENT
import pygame.locals as GAME_LOCALS
pygame.init()
pygame.font.init()

###########################################

#window size
window_width = 1024
window_height = 720
font_w = window_width/2 - 250
font_h = window_height - 200
font_x = 300
font_y = 30
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Hangman')
start_image = pygame.image.load("start.jpg")
game_title = pygame.image.load("HANGMAN.PNG")
level_1 = pygame.image.load("1level.jpg")
level_2 = pygame.image.load("2level.jpg")
level_3 = pygame.image.load("3level.jpg")
level_4 = pygame.image.load("4level.jpg")
#level_5 = pygame.image.load("level5.jpg")
chance_1 = 0
count = 0 #to check whether word is complete or not
start = False
stop = False
sp = 50

#############################################

#################################################
st = ['Stage 1 || Press Space to Continue', 'stage 2 || Press Space to Continue',
      'stage 3 || Press Space to Continue', 'stage 4 || Press Space to Continue',
      'stage 5 || Press Space to Continue']
def stage(i):
    global st
    run = True
    while run:
        window.fill((255, 255, 255))
        font = pygame.font.SysFont("arial", 40)
        text = font.render(st[i], True, (0, 0, 0))
        window.blit(text, (200, 300))
        for event in GAME_EVENT.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#animated lines
def lines():
    pygame.draw.lines(window, (0, 0, 0), False, [(150, 80),(150, 450)], 7)
    pygame.draw.lines(window, (0, 0, 0), False, [(100, 450), (400, 450)], 10)
    pygame.draw.lines(window, (0, 0, 0), False, [(150, 80), (300, 80)], 8)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 80), (230, 150)],6)

################################################

word = ['algorithm', 'name', 'country', 'stream', 'mean',
            'witch', 'dialogue', 'background', 'filter', 'products',
        'aftershock', 'abolishment', 'copyright', 'computer', 'mobile']
txt = random.choice(word)
guess = []
for letters in txt:
    guess += letters
for blanks in range(len(guess)):
    guess += ['_']

def select_word():

    global sp,txt,guess,count
    l_txt = len(txt)
    l_guess = len(guess)
    for i in range(l_txt,l_guess):
        font = pygame.font.SysFont("arial", 50)
        text = font.render(guess[i], True, (0, 180,255))
        window.blit(text,(font_w+sp,font_h))
        sp += 50


####################################################

def restart_game():
    font = pygame.font.SysFont("arial", 50)
    text = font.render('GAME OVER. Press Space to restart...', True, (255, 0, 0))
    window.blit(text, (window_width / 10, window_height / 2))

####################################################

def body(ch):
    global chance_1,stop
    if ch == 1:
        pygame.draw.circle(window,(0,0,0),(230,170),30,0)
    if ch == 2:
        pygame.draw.lines(window, (0, 0, 0), False, [(230, 170), (230, 300)], 5)
    if ch == 3:
        pygame.draw.lines(window, (0, 0, 0), False, [(230, 220), (290, 250)], 5)
    if ch == 4:
        pygame.draw.lines(window, (0, 0, 0), False, [(230, 220), (170, 250)], 5)
    if ch == 5:
        pygame.draw.lines(window, (0, 0, 0), False, [(230, 300), (280, 350)], 5)
    if ch == 6:
        pygame.draw.lines(window, (0, 0, 0), False, [(230, 300), (180, 350)], 5)
    if ch > 6:
        stop = True
        restart_game()

######################################################

def word_search(check1):
    global chance_1, txt,guess,sp,count
    status = False
    num_0 = len(guess)
    num = len(txt)
    num_1 = len(txt) # for print letter at right blank
    sp = 50
    for ltr_n in range(num):
        if guess[ltr_n] == check1 and check1 not in guess[num:num_0]: #letters will not duplicate
            status = True
            guess[num_1] = check1
            select_word()
            count += 1
        num_1 += 1

    if status == False and check1 not in guess[num:num_0]:
        chance_1 += 1
        body(chance_1)

        
##########################################################
def load_start_image():
    run = True
    while run:
        window.blit(start_image,(0,0))
        window.blit(game_title,(window_width/2 - 380,window_height/2 - 100))
        font = pygame.font.SysFont("arial", 50)
        text = font.render('', True, (255, 255, 255))
        window.blit(text, (window_width / 10, window_height / 2))
        for event in GAME_EVENT.get():
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
            pygame.display.update()

#level 1 main loop
def level_1_fun():
    global start,chance_1,stop,txt,guess
    run = True
    while run:
        if start == False:  # for game start
            window.blit(level_1, (0, 0))
            lines()
            select_word()
        start = True  # game running
        for event in GAME_EVENT.get():
            if event.type == pygame.KEYDOWN:
                if stop == False:  # to restart the game if over
                    if event.key == pygame.K_a:
                        char = 'a'
                        word_search(char)
                    if event.key == pygame.K_b:
                        char = 'b'
                        word_search(char)
                    if event.key == pygame.K_c:
                        char = 'c'
                        word_search(char)
                    if event.key == pygame.K_d:
                        char = 'd'
                        word_search(char)
                    if event.key == pygame.K_e:
                        char = 'e'
                        word_search(char)
                    if event.key == pygame.K_f:
                        char = 'f'
                        word_search(char)
                    if event.key == pygame.K_g:
                        char = 'g'
                        word_search(char)
                    if event.key == pygame.K_h:
                        char = 'h'
                        word_search(char)
                    if event.key == pygame.K_i:
                        char = 'i'
                        word_search(char)
                    if event.key == pygame.K_j:
                        char = 'j'
                        word_search(char)
                    if event.key == pygame.K_k:
                        char = 'k'
                        word_search(char)
                    if event.key == pygame.K_l:
                        char = 'l'
                        word_search(char)
                    if event.key == pygame.K_m:
                        char = 'm'
                        word_search(char)
                    if event.key == pygame.K_n:
                        char = 'n'
                        word_search(char)
                    if event.key == pygame.K_o:
                        char = 'o'
                        word_search(char)
                    if event.key == pygame.K_p:
                        char = 'p'
                        word_search(char)
                    if event.key == pygame.K_q:
                        char = 'q'
                        word_search(char)
                    if event.key == pygame.K_r:
                        char = 'r'
                        word_search(char)
                    if event.key == pygame.K_s:
                        char = 's'
                        word_search(char)
                    if event.key == pygame.K_t:
                        char = 't'
                        word_search(char)
                    if event.key == pygame.K_u:
                        char = 'u'
                        word_search(char)
                    if event.key == pygame.K_v:
                        char = 'v'
                        word_search(char)
                    if event.key == pygame.K_w:
                        char = 'w'
                        word_search(char)
                    if event.key == pygame.K_x:
                        char = 'x'
                        word_search(char)
                    if event.key == pygame.K_y:
                        char = 'y'
                        word_search(char)
                    if event.key == pygame.K_z:
                        char = 'z'
                        word_search(char)
                if event.key == pygame.K_SPACE and chance_1 > 6:  # letter won't print after game over
                    txt = random.choice(word)
                    guess = []
                    for letters in txt:
                        guess += letters
                    for blanks in range(len(guess)):
                        guess += ['_']
                    stop = False
                    chance_1 = 0
                    start = False
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
        if count == len(txt):
            run = False

        pygame.display.update()

#############################################################################################
#############################################################################################
#############################################################################################


phrase = ['cricket is played with (SIZE)', '___ rises in the east', 'find square shape',
          'Broken cryons still ______(All Colors)']
sentence_display = random.choice(phrase)
def select_phrase():
    global sentence_display
    font = pygame.font.SysFont("arial", 30)
    text = font.render(sentence_display, True, (60, 20, 60))
    window.blit(text, (font_x, font_y))

######################################################

x_pos = 10
y_pos = 600
inc = [100,300,500,700]
addition = random.choice(inc) #shapes will not overlap
space = 100

def body_2():
    global stop,x_pos,y_pos,addition,space,inc
    pygame.draw.circle(window, (0, 0, 0), (230, 170), 30, 0)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 170), (230, 300)], 5)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 220), (290, 250)], 5)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 220), (170, 250)], 5)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 300), (280, 350)], 5)
    pygame.draw.lines(window, (0, 0, 0), False, [(230, 300), (180, 350)], 5)
    stop = True
    restart_game()

def options():
    global sentence_display,phrase, inc,addition,space,x_pos,y_pos

    if sentence_display == phrase[0]:
        pygame.draw.circle(window,(0,255,180),(x_pos+addition,y_pos),30,0)
        for n1 in range(3):
            rad = random.randrange(40,80)
            red = random.randrange(50, 255)
            green = random.randrange(0, 50)
            blue = random.randrange(50, 255)
            if space == addition:
                space += 200
            pygame.draw.circle(window,(red,green,blue),(x_pos + space,y_pos),rad,0)
            space += 200

    if sentence_display == phrase[1]:
        pygame.draw.circle(window,(255,200,0),(x_pos+addition , y_pos),50,0)
        for n1 in range(3):
            s_red = random.randrange(0, 50)
            s_green = random.randrange(60, 255)
            s_blue = random.randrange(60, 255)
            if space == addition:
                space += 200
            pygame.draw.circle(window,(s_red,s_green,s_blue),(x_pos + space,y_pos),random.randrange(60,100),0)
            space += 200

    if sentence_display == phrase[2]:
        pygame.draw.rect(window,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),
                         (x_pos+addition , y_pos,80,80))
        for n1 in range(3):
            w = random.randrange(30, 70)
            h = random.randrange(80, 150)
            red = random.randrange(50, 255)
            green = random.randrange(0, 50)
            blue = random.randrange(50, 255)
            if space == addition:
                space += 200
            pygame.draw.rect(window, (red, green, blue), (x_pos+space , y_pos, w, h))
            space += 200


    if sentence_display == phrase[3]:
        size = random.randrange(40,80)
        pygame.draw.rect(window,(255,255,255),(x_pos+addition, y_pos,size,size))
        for n1 in range(3):
            w = random.randrange(30, 70)
            h = random.randrange(80, 150)
            red = random.randrange(50, 255)
            green = random.randrange(0, 50)
            blue = random.randrange(50, 255)
            if space == addition:
                space += 200
            pygame.draw.rect(window, (red, green, blue), (x_pos+space , y_pos, w, h))
            space += 200

def level_2_fun():
    global addition,stop,sentence_display,phrase,x_pos,y_pos,inc, space
    run = True
    start_2 = False
    stop = False
    while run:
        if start_2 == False:
            window.blit(level_2, (0, 0))
            lines()
            select_phrase()
            options()
        start_2 = True
        for event in GAME_EVENT.get():
            if event.type == pygame.KEYDOWN:
                if stop == False:
                    if event.key == pygame.K_1:
                        num = 100
                        if num == addition:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_2:
                        num = 300
                        if num == addition:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_3:
                        num = 500
                        if num == addition:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_4:
                        num = 700
                        if num == addition:
                            run = False
                        else:
                            body_2()
                if event.key == pygame.K_SPACE:
                    x_pos = 10
                    y_pos = 600
                    inc = [100, 300, 500, 700]
                    addition = random.choice(inc) # shapes will not overlap
                    sentence_display = random.choice(phrase)
                    space = 100
                    start_2 = False
                    stop = False
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


########################################################################
########################################################################
########################################################################

question = ['5x + 7x - 3 = 33', '1 meter = ___ centimeter', '10 million has ___ digits',
            'Hexagon has ___ sides', 'right triangle is always of ___ degree']
select_question = random.choice(question)
def question_selection():
    global select_question
    font = pygame.font.SysFont("arial", 30)
    text = font.render(select_question, True, (200, 200, 255))
    window.blit(text, (font_x, font_y))


x = 10
y = 600
increment = [100,300,500,700]
adding = random.choice(increment) #shapes will not overlap
space_added = 100

def quesion_options():
    global select_question, question, x, y, addiing,space_added
    if select_question == question[0]:
        font = pygame.font.SysFont("arial", 50)
        text = font.render('3', True, (200, 200, 255))
        window.blit(text, (x+adding, y))
        for n in range(3):
            if space_added == adding:
                space_added += 200
            num = random.randrange(4,100)
            font = pygame.font.SysFont("arial", 50)
            text = font.render(str(num), True, (200, 200, 255))
            window.blit(text, (x+space_added, y))
            space_added += 200

    if select_question == question[1]:
        font = pygame.font.SysFont("arial", 50)
        text = font.render('100', True, (200, 200, 255))
        window.blit(text, (x+adding, y))
        for n in range(3):
            if space_added == adding:
                space_added += 200
            num = random.randrange(200,1000)
            font = pygame.font.SysFont("arial", 50)
            text = font.render(str(num), True, (200, 200, 255))
            window.blit(text, (x+space_added, y))
            space_added += 200

    if select_question == question[2]:
        font = pygame.font.SysFont("arial", 50)
        text = font.render('7', True, (200, 200, 255))
        window.blit(text, (x+adding, y))
        for n in range(3):
            if space_added == adding:
                space_added += 200
            num = random.randrange(8,20)
            font = pygame.font.SysFont("arial", 50)
            text = font.render(str(num), True, (200, 200, 255))
            window.blit(text, (x+space_added, y))
            space_added += 200

    if select_question == question[3]:
        font = pygame.font.SysFont("arial", 50)
        text = font.render('16', True, (200, 200, 255))
        window.blit(text, (x+adding, y))
        for n in range(3):
            if space_added == adding:
                space_added += 200
            num = random.randrange(1,15)
            font = pygame.font.SysFont("arial", 50)
            text = font.render(str(num), True, (200, 200, 255))
            window.blit(text, (x+space_added, y))
            space_added += 200

    if select_question == question[4]:
        font = pygame.font.SysFont("arial", 50)
        text = font.render('90', True, (200, 200, 255))
        window.blit(text, (x+adding, y))
        for n in range(3):
            if space_added == adding:
                space_added += 200
            num = random.randrange(1,89)
            font = pygame.font.SysFont("arial", 50)
            text = font.render(str(num), True, (200, 200, 255))
            window.blit(text, (x+space_added, y))
            space_added += 200

def level_3_fun():
    global addition, stop, select_question, question, x, y, inc, space_added
    global adding
    run = True
    stop = False
    start_3 = False
    while run:
        if start_3 == False:
            window.blit(level_3, (0, 0))
            lines()
            question_selection()
            quesion_options()
        start_3 = True
        for event in GAME_EVENT.get():
            if event.type == pygame.KEYDOWN:
                if stop == False:
                    if event.key == pygame.K_1:
                        num = 100
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_2:
                        num = 300
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_3:
                        num = 500
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_4:
                        num = 700
                        if num == adding:
                            run = False
                        else:
                            body_2()
                if event.key == pygame.K_SPACE:
                    x = 10
                    y = 600
                    increment = [100, 300, 500, 700]
                    adding = random.choice(increment)  # shapes will not overlap
                    select_question = random.choice(question)
                    space_added = 100
                    start_3 = False
                    stop = False

            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#############################################################################
#############################################################################
#############################################################################

x4 = 10
y4 = 700
pictures = [pygame.image.load("1.jpg"), pygame.image.load("2.jpg"),pygame.image.load("3.jpg"),
            pygame.image.load("4.jpg"),pygame.image.load("5.jpg")]
select_picture = random.choice(pictures)
word_space = 100
list_of_statues = ['Moai', 'Rio, de Janeiro', 'Little Mermaid','The Thinker', 'David Statue',
                   'Terrace of the Lion', 'Statue of unity', 'Mount Nemrut', 'Great Sphinx', 'Buddha',
                   'Venus Di Milo', 'Lion-Man', 'Christ Blesing', 'Christ of Abyss', 'Maitrya',
                   'Veiled Virgin', 'Chrst of Ozerks', 'Pepilos Kore', 'Sala Keoku', 'Statue of Freedom']
def picture_selection():
    global select_picture
    window.blit(select_picture,(500,50))

def picture_options():
    global select_picture,pictures,adding,word_space,list_of_statues
    if select_picture == pictures[0]:
        font = pygame.font.SysFont("arial", 18)
        text = font.render('Statue of liberty', True, (200, 200, 255))
        window.blit(text, (x4 + adding, y4))
        for n in range(3):
            n = random.randrange(0,19)
            if word_space == adding:
                word_space += 200
            font = pygame.font.SysFont("arial", 18)
            text = font.render(list_of_statues[n], True, (200, 200, 255))
            window.blit(text, (x4+word_space, y4))
            word_space += 200

    if select_picture == pictures[1]:
        font = pygame.font.SysFont("arial", 18)
        text = font.render('Burj Khalifa', True, (200, 200, 255))
        window.blit(text, (x4 + adding, y4))
        for n in range(3):
            n = random.randrange(0, 19)
            if word_space == adding:
                word_space += 200
            font = pygame.font.SysFont("arial", 18)
            text = font.render(list_of_statues[n], True, (200, 200, 255))
            window.blit(text, (x4 + word_space, y4))
            word_space += 200

    if select_picture == pictures[2]:
        font = pygame.font.SysFont("arial", 18)
        text = font.render('Eiffil Tower', True, (200, 200, 255))
        window.blit(text, (x4 + adding, y4))
        for n in range(3):
            n = random.randrange(0, 19)
            if word_space == adding:
                word_space += 200
            font = pygame.font.SysFont("arial", 18)
            text = font.render(list_of_statues[n], True, (200, 200, 255))
            window.blit(text, (x4 + word_space, y4))
            word_space += 200

    if select_picture == pictures[3]:
        font = pygame.font.SysFont("arial", 18)
        text = font.render('Big Ben', True, (200, 200, 255))
        window.blit(text, (x4 + adding, y4))
        for n in range(3):
            n = random.randrange(0, 19)
            if word_space == adding:
                word_space += 200
            font = pygame.font.SysFont("arial", 18)
            text = font.render(list_of_statues[n], True, (200, 200, 255))
            window.blit(text, (x4 + word_space, y4))
            word_space += 200

    if select_picture == pictures[4]:
        font = pygame.font.SysFont("arial", 18)
        text = font.render('Taj Mahal', True, (200, 200, 255))
        window.blit(text, (x4 + adding, y4))
        for n in range(3):
            n = random.randrange(0, 19)
            if word_space == adding:
                word_space += 200
            font = pygame.font.SysFont("arial", 18)
            text = font.render(list_of_statues[n], True, (200, 200, 255))
            window.blit(text, (x4 + word_space, y4))
            word_space += 200

def level_4_fun():
    global stop, select_picture, pictures, x4, y4, word_space,list_of_statues,increment
    global adding
    run = True
    start_4 = False
    while run:
        if start_4 == False:
            window.blit(level_4, (0, 0))
            lines()
            picture_selection()
            picture_options()
        start_4 = True
        for event in GAME_EVENT.get():
            if event.type == pygame.KEYDOWN:
                if stop == False:
                    if event.key == pygame.K_1:
                        num = 100
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_2:
                        num = 300
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_3:
                        num = 500
                        if num == adding:
                            run = False
                        else:
                            body_2()
                    if event.key == pygame.K_4:
                        num = 700
                        if num == adding:
                            run = False
                        else:
                            body_2()
                if event.key == pygame.K_SPACE:
                    x4 = 10
                    y4 = 700
                    pictures = [pygame.image.load("1.jpg"), pygame.image.load("2.jpg"), pygame.image.load("3.jpg"),
                                pygame.image.load("4.jpg"), pygame.image.load("5.jpg")]
                    select_picture = random.choice(pictures)
                    word_space = 100
                    list_of_statues = ['Moai', 'Rio, de Janeiro', 'Little Mermaid', 'The Thinker', 'David Statue',
                                       'Terrace of the Lion', 'Statue of unity', 'Mount Nemrut', 'Great Sphinx',
                                       'Buddha',
                                       'Venus Di Milo', 'Lion-Man', 'Christ Blesing', 'Christ of Abyss', 'Maitrya',
                                       'Veiled Virgin', 'Chrst of Ozerks', 'Pepilos Kore', 'Sala Keoku',
                                       'Statue of Freedom']
                    adding = random.choice(increment)
                    start_4 = False
                    stop = False
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

##############################################################
##############################################################
##############################################################

list_1 = []
def maze():
    global list_1
    pygame.draw.lines(window,(255,255,255),False,[(100,100),(500,100),(500,500),
                                                  (100,500),(100,100)],3)
    pygame.draw.lines(window,(255,255,255),False,[(150,300),(150,150),(300,150),],3)
    pygame.draw.lines(window,(255,255,255),False,[(350,100),(350,200),(200,200),(200,350)],3)
    pygame.draw.lines(window,(255,255,255),False,[(100,400),(250,400)],3)
    pygame.draw.lines(window, (255, 255, 255), False, [(150,500),(150,450)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(250,500),(250,450)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(400, 500), (400, 450),(450,450)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(500,350),(400,350),(400,300),(450,300)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(500,250),(350,250),(350,450)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(350, 425),(150, 425),(200,425),(200,470)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(100, 400), (250, 400)], 3)
    pygame.draw.lines(window, (255, 255, 255), False, [(460,100),(460,220),(270,220),(270,400),(300,400)], 3)


    for n1 in range(100,501):
        list_1.append((n1,100))
        list_1.append((100,n1))
        list_1.append((n1,500))
        list_1.append((500,n1))
    for n2 in range(150,301):
        list_1.append((150,n2))
        list_1.append((n2, 150))
    for n3 in range(100,201):
        list_1.append((350, n3))
    for n4 in range(200,351):
        list_1.append((200, n4))

Player_x = 150
Player_y = 200
Player_vel = 1
def level_5_fun():
    global Player_y, Player_x,Player_vel
    start = False
    run = True
    move = False
    move_1 = False
    while run:
        window.fill((0, 0, 0))
        maze()
        pygame.draw.circle(window, (255, 0, 0), (Player_x, Player_y), 6)
        start = True
        for event in GAME_EVENT.get():
            if event.type == GAME_LOCALS.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            Player_y -= Player_vel
        if keys[pygame.K_DOWN]:
            Player_y += Player_vel
        if keys[pygame.K_LEFT]:
            Player_x -= Player_vel
        if keys[pygame.K_RIGHT]:
            Player_x += Player_vel
        pygame.display.update()

def player():
    global player_x, player_y





load_start_image()

stage(0)
level_1_fun()
time.sleep(1)

stage(1)
for numbers in range(3):
    level_2_fun()
    time.sleep(1)
    x_pos = 10
    y_pos = 600
    inc = [100, 300, 500, 700]
    addition = random.choice(inc)  # shapes will not overlap
    space = 100
    sentence_display = random.choice(phrase)

stage(2)
for numbers_1 in range(3):
    level_3_fun()
    time.sleep(1)
    x = 10
    y = 600
    increment = [100, 300, 500, 700]
    adding = random.choice(increment)  # shapes will not overlap
    space_added = 100
    select_question = random.choice(question)

stage(3)
for numbers_2 in range(3):
    level_4_fun()
    time.sleep(1)
    x4 = 10
    y4 = 700
    adding = random.choice(increment)
    select_picture = random.choice(pictures)
    word_space = 100


stage(4)
level_5_fun()























