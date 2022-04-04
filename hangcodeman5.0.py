# A különböző szinteknek megfelelően kevesebb élet, kevesebb stádium a k
# Kiírja a betűket, amik nem voltak megfelelőek, még megvalósítás alatt.

from __future__ import absolute_import
import time
import menu
import os
import random
import display
import final_easy_words
import final_medium_words
import final_hard_words
import anim_intro
import win
import lose
import quit
from playsound import playsound
from threading import Thread


def play():
    def plays():
        playsound("./fullmusic.mp3")

    def playsf():
        playsound("fart.mp3")

    def playskeny():
        playsound("keny_die.mp3")

    def playscq():
        playsound("cartman_quit.mp3")

    def playsw():
        playsound("crash.mp3")

    def playskw():
        playsound("kenywin.mp3")

    def change_diff_words():   # a szavak hosszát lehet vele állítani
        os.system('cls')
        print(menu.menu[0])
        diff_word = input()

        if diff_word == '1':
            word = random.choice(final_easy_words.easy_w)
            print('Your choice is "easy". Words contain 4 letters.')
            return word
        elif diff_word == '2':
            word = random.choice(final_medium_words.medium_w)
            print('Your choice is "medium". Words contain 5-6 letters.')
            return word
        elif diff_word == '3':
            word = random.choice(final_hard_words.hard_w)
            print('Your choice is "hard". Words contain 7-10 letters.')
            return word
        else:
            os.system('cls')
            return change_diff_words()

    def change_diff_lives():  # az életek számát lehet állítani, vele...
        os.system('cls')
        print(menu.menu[1])
        diff_lives = input()

        if diff_lives == '1':
            lives = 12
            print('Your choice is "easy". You have 12 lives.')  # Ha választasz ezt nem printeli ki csak elindul a játék
            return lives
        elif diff_lives == '2':
            lives = 10
            print('Your choice is "medium". You have 10 lives.')  # Ha választasz ezt nem printeli ki csak elindul a
            return lives
        elif diff_lives == '3':
            lives = 8
            print('Your choice is "hard". You have 8 lives.')  # Ha választasz ezt nem printeli ki csak elindul a játék
            return lives
        else:
            os.system('cls')
            return change_diff_lives()

    def intro_anim():
        i = 0
        while i != 32:
            os.system('cls')
            print(anim_intro.anim_intro[i])
            time.sleep(0.6)
            i = i+1

    def ifwin():
        i = 0
        Tkw.start()
        while i != 34:
            if i == 6:
                Tcrash.start()
            if i == 28:
                TKd.start()
            os.system('cls')
            print(win.win[i])
            time.sleep(1)
            i = i+1

    def iflose():
        Tf.start()
        i = 0
        while i != 19:
            os.system('cls')
            print(lose.lose[i])
            time.sleep(0.7)
            i = i+1

    T = Thread(target=plays)  # create thread
    Tf = Thread(target=playsf)
    TKd = Thread(target=playskeny)
    TCQ = Thread(target=playscq)
    Tcrash = Thread(target=playsw)
    Tkw = Thread(target=playskw)
    T.start()
    intro_anim()
    time.sleep(3)
    global reveal
    word = str(change_diff_words())
    reveal = list(len(word)*'_')
    lives = int(change_diff_lives())  # Ide kell meghívni a change_diff_lives függvényt...?
    gameWon = False
    word = word.upper()
    wrongLetter = []

    def check_letter(letter, word):

        for i in range(0, len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if '_' not in reveal:
            return True
        else:
            return False

    def status():
        os.system('cls')
        print(display.display[12-lives])
        print('''                                    ''' + ' '.join([str(e) for e in reveal]).capitalize() + '\n')
        print('''                                    You have''', lives, 'live(s).\n')
        print('''                                    Wrong letters:''', wrongLetter, '\n')

    while gameWon == (False) and lives > 0:
        status()
        guess = input('''                                    Guess a letter or an entire word:''')
        if guess == "quit":  # KILÉPÉS
            os.system('cls')
            print(quit.quit[0])
            time.sleep(5)
            exit()  # KILÉPÉS VÉGE
        guess = guess.upper()

        if guess == word:
            gameWon = True
            reveal = word
        if len(guess) == 1 and guess in word:
            gameWon = check_letter(guess, word)
        else:
            lives -= 1
            wrongLetter.append(guess)
        status()

    if gameWon:
        ifwin()
        res = int(input('''                                  Do you want to try again? 1 - Yes/ 2 - No  '''))
        if res == 1:
            play()
        elif res == 2:
            os.system('cls')
            print(quit.quit[0])
            TCQ.start()
            time.sleep(5)
            exit()

    else:
        iflose()
        res = int(input('''                                  Do you want to try again? 1 - Yes/ 2 - No  '''))
        if res == 1:
            play()
        elif res == 2:
            os.system('cls')
            print(quit.quit[0])
            TCQ.start()
            time.sleep(5)
            exit()


play()
