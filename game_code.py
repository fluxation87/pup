#Pup Wrangler
from sys import exit
import time
import sys
from random import randrange
from random import randint
from pynput.keyboard import Key, Controller
from pygame import mixer
import pygame as pg



pg.init() # initialize the pygame
win = pg.display.set_mode((1920, 1080)) # create the game window
pg.display.set_caption("Puppy Love")
white = (255,255,255)
black = (0,0,0)


pg.mixer.init()
bark1 = pg.mixer.Sound('bark1.wav')
bark2 = pg.mixer.Sound('bark2.wav')
cook = pg.mixer.Sound('cooking.wav')
geese = pg.mixer.Sound('geese.wav')
lick = pg.mixer.Sound('lick.wav')
pots = pg.mixer.Sound('pots.wav')
snarl = pg.mixer.Sound('snarl.wav')
yelp = pg.mixer.Sound('yelp.wav')
cheer = pg.mixer.Sound('cheer.wav')
stream = pg.mixer.Sound('stream.wav')
yell = pg.mixer.Sound('yell.wav')
bite = pg.mixer.Sound('bite.wav')
cry = pg.mixer.Sound('cry.wav')
fall = pg.mixer.Sound('fall.wav')
endriff = pg.mixer.Sound('endriff.wav')
cooking = pg.mixer.Sound('cooking.wav')



pupname = None
keyboard = Controller()


def getname():
    global pupname
    print(pupname)

def getkidname():
    global kidname
    print(kidname)

def pname():
    global pupname
    pupname = input("\nTEXT")
    #print("Welcome, {}.".format(pupname))

def playername():
    global kidname
    kidname = input("\nTEXT ")
    #print("Welcome, {}.".format(pupname))

class Background(pg.sprite.Sprite):
    def __init__(self):
        pass

    def draw1(self):
        # bg = pg.sprite.Group()
        global img
        img = pg.image.load('barn2.png').convert()#line 1 for bg fill
        win.blit(img,(0,0))
        
        pg.display.flip()

    def draw2(self):
        win.fill(white)
        pg.display.flip()

global bg
bg = Background()

class Scene(object):
    def enter(self):
        print("TEXT.")
        print("TEXT")
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Home')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()



def slowtext(text):

    for c in (text):
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0.0" + str(randrange(3, 6, 3))
        seconds = float(seconds)
        time.sleep(seconds)

class Kid(object):

    def __init__(self,name):
        self.name = name
        self.health = 5

kid = Kid('1')
class Dog (object):

    def __init__(self):
        pass

    def getname(self):
        global pupname
        print(pupname)

    def bark(self):
        kid.health -= 2
        print(f"\nYou were barked at! {pupname} now has {kid.health} affection towards you.")
        bark2.play()
        if kid.health < 1:
            dog.run()
        else:
            pass


    def cry(self):
        kid.health -= 2
        cry.play()
        if kid.health < 1:
            dog.run()

    def bite(self):
        kid.health -= 2
        bite.play()
        print(f"You got bit! {pupname} now has {kid.health} affection towards you.")
        if kid.health < 1:
            dog.run()
            
        else:
            pass

    def lick(self):
        kid.health += 2
        lick.play()
        #time.sleep(0.5)
        #lick.play()
        print(f"\n{pupname} licked you! He now has {kid.health} affection towards you.")
        if kid.health == 10:
            return 'home'
        else:
            pass

    def run(self):
        endriff.play()
        time.sleep(1)
        print(f"\n{pupname} grew tired of you and ran away. You are heartbroken and return home alone.")
        exit(1)
        #return dead #USE_THIS_ONE_TO_END_THE_GAME.
dog = Dog()

class Naming(Scene):

    #bg.draw1()

    def enter(self):
        bg.draw1()
        #img = pg.image.load('barn.png').convert()#line 1 for bg fill
        # # window.blit(img,(0,0))#line 2 and final for bg fill
        # pg.display.flip()
        music = pg.mixer.music.load('riff.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)
        playername()

        print("*"*100)
        intro1= f"\nWelcome to this heartfelt journey, {kidname}.\n\n"

        intro2 = """TEXT .
"""
        slowtext(intro1)
        slowtext(intro2)
        cry.play()
        pname() #GLOBAL variable works in this instance!!!
        #pupname = input('>>>')
        instruct = f"\nTEXT"
        slowtext(instruct)
        pg.mixer.music.fadeout(2)
        return 'barn'

class Barn(Scene):

    def enter(self):

        bg.draw2()
        pg.display.flip()
        music = pg.mixer.music.load('barnriff.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

        quest1= f"""
        \nATEXT
"""
        slowtext(quest1)
        choice = input('What will you do? ')
        if choice == '1':
            c1 = "\nTEXT."
            c2 = f"\nTEXT\n"
            slowtext(c1)
            slowtext(c2)
            dog.bark()
            return 'barn'

        elif choice == '2':
            c3 = f"\TEXT."
            c4 = " TEXT\n"
            slowtext(c3)
            slowtext(c4)
            dog.bite()
            return 'barn'
        elif choice == '3':
            c5 = f"""\nTEXT"""
            slowtext(c5)
            dog.cry()
            return 'barn'

        elif choice == '4':
            c6 = f"""\n
TEXT\n"""
            slowtext(c6)
            dog.lick()
            a = f"""
\nTEXT
"""
            slowtext(a)
            return 'field'
        else:
            e = "TEXT."
            return 'barn'


            # info = "\nHave you played been on this journey before? Press '1' for Yes and '2' for no."
            #
            # j = input('\n>>>')
            # if j == '1':
            #     print("Then, let us continue with the story.")
            # else:
            #     print(f"\n{pupname}'s emotional responses to your actions will change your affection level. You start with {kid.health} affection.")
            #     print("\nIf you reach 10 affection, the pup will follow you home.")
            #     print("If you reach 0 affection, the pup will run away.\n")


class Field(Scene):

    def enter(self):
        music = pg.mixer.music.load('fieldriff.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)
        f1 = f"""
TEXT
"""
        slowtext(f1)
        goodpath = randint(1,2)
        guess = input('>>>')
        if int(guess) == goodpath:
            gp = f"""
TEXT
"""
            slowtext(gp)
            dog.lick()
            pondd = f"""
TEXT"""
            slowtext(pondd)
            return 'pond'
        else:
            bp = f"""
TEXT"""
            slowtext(bp)
            dog.bark()
            return 'field'


class Pond(Scene):  #NEED_TO_FIGURE_OUT_text TIME_DELAY_ISSUE

    def enter(self):
        #pg.mixer.Sound('stream.wav')
        music = pg.mixer.music.load('stream.wav')
        pg.mixer.music.set_volume(5)
        pg.mixer.music.play(-1)
        p = f"""
TEXT"""
        slowtext(p)
        geese.play()
        time.sleep(5)
        geese.play()
        o = """
TEXT"""
        slowtext(o)
        print("""
\nWhat will you do?
TEXT""")
        chce = input(">>>")

        if chce == '1':
            one = f"""
TEXT."""
            slowtext(one)
            fall.play()
            time.sleep(2)
            dog.bark()
            return 'pond'

        elif chce == '2':
            two = f"""
TEXT """
            slowtext(two)
            dog.run()

        elif chce == '3':
            three = f"""
TEXT ."""
            slowtext(three)
            dog.bark()
            return 'pond'

        else:
            chce == '4'
            four1 = f"""
TEXT!
"""

            yell.play()
            time.sleep(2)
            bark1.play()
            time.sleep(.5)
            cry.play()
            slowtext(four1)
            four2 = f"""
TEXT"""
            slowtext(four2)
            dog.lick()

            return 'livroom'

class LivRoom(Scene):

    def enter(self):
        music = pg.mixer.music.load('livroomriff.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)
        e = f"""
TEXT
1: 25 minutes
2: 35 minutes
3: 45 minutes
4: 55 minutes\n"""
        slowtext(e)
        a = input(">>>")
        if a == '1':
            one = "You obviously don't excel at math...\n"
            slowtext(one)
            return 'livroom'
        elif a == '2':
            two = "Maybe go pick up a math book...\n"
            slowtext(two)
            return 'livroom'
        elif a == '3':
            three = f"""
TEXT"""
            pots.play()
            time.sleep(2)
            cooking.play()
            time.sleep(2)
            slowtext(three)
            three1 = f"""
TEXT"""
            slowtext(three1)
            dog.lick()
            return 'home'

        elif a == '4':
            four = "TEXT"
            slowtext(four)
            return 'livroom'


class Home(Scene):

    def enter(self):
        music = pg.mixer.music.load('homeriff.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)


        hometext = f"""
TEXT
"""
        slowtext(hometext)
        time.sleep(1)
        cheer.play()
        time.sleep(2)
        cheer.play()
        print("~"*100)
        print(f"                      {kidname},Your final affecting score is: {kid.health}.")
        print("                     You have completed the game. Congratulations!")
        print("~"*100)
        time.sleep(5)
        exit(1)


class GameMap(object):
    scenes = {'naming': Naming(), 'barn': Barn(), 'field': Field(), 'pond': Pond(), 'livroom': LivRoom(), 'home': Home(),}

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = GameMap.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


main = True
while main == True:

    input("")

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    if current_scene == Scene1():
        win.fill(blue)
    elif current_scene == Scene2():
        win.fill(white)
    elif current_scene == Scene2():
        win.fill(black)

start_map = GameMap('naming')
start_game = Engine(start_map)
start_game.play()
pg.quit()
