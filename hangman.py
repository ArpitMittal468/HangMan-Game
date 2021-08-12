from os import system
from random import randint
from msvcrt import getwch as gt
from time import sleep
import cursor


def clear():
    system('cls')


def weelcomescreen():
    system("title Hang Man")
    print('\n\n\n\n\n\n')
    print('          ╔═══════════╗')
    print('          ║  HANGMAN  ║')
    print('          ╠═══════════╣')
    print('          ║           ║')
    print('         ═╩═         ═╩═')
    print('\n\n')
    print('          >> WELCOME <<')
    print('\n\n\n\n\n')
    print('      MADE BY: Arpit Mittal')
    sleep(1.5)


def getch():
    return gt()


def disword(ant, cp, w):
    print('       Antonym: ', ant)
    print('         Guess:  ', *cp, sep='')
    print('       Chances: ', 5 - w)


def hangimage(p, al):
    print()
    print('           ≈≈≈≈≈≈≈≈≈≈≈')
    print('             HANGMAN')
    print('           ≈≈≈≈≈≈≈≈≈≈≈')
    print()
    print(f'             ╔═══╕')
    print(f'             ║   {p[0]}')
    print(f'             ║  {p[2]}{p[1]}{p[3]}')
    print(f'             ║  {p[4]} {p[5]}')
    print(f'             ║')
    print(f'          ═══╩═════')
    print()
    print('      ', *al[0:9])
    print('      ', *al[9:18])
    print('      ', *al[18:27])
    print()


def gamemenu():
    cursor.hide()
    count = 0
    tick = ['√', ' ', ' ']
    while True:
        clear()
        print('\n\n\n\n\n\n\n\n\n')
        print(f'       {tick[0]} 1 » PLAY')
        print(f'       {tick[1]} 2 » INSTRUCTION')
        print(f'       {tick[2]} 3 » EXIT')
        t = getch()
        if t in '123':
            for i in [0, 1, 2]:
                if str(i+1) == t:
                    tick[i] = '√'
                    count = i
                else:
                    tick[i] = ' '
        elif t == '\r':
            return count + 1
        else:
            continue


def instructionenu():
    clear()
    print('\n\n')
    print('    >> Welcome to HANGMAN <<')
    print('    ------------------------')
    print('      In this game you will')
    print('      be given an antonym  ')
    print('      of the word to be    ')
    print('      guessed.  \n         ')
    print('      Press single key one ')
    print('      by one to complete   ')
    print('      the word you are     ')
    print('      trying to guess.  \n ')
    print('      You will be provided ')
    print('      5 chances to correct ')
    print('      your wrong guess !!\n')
    print('      You can change the   ')
    print('      the current word by  ')
    print('      pressing 0 ( Zero ). ')
    print('\n')
    print('      << Press any key to  ')
    print('         go to back to main')
    print('         menu... >>')
    getch()

system('mode con: cols=34 lines=26')
system('color f0')
cursor.hide()


words = [('HILL', 'VALLEY'), ('ABROAD', 'HOME'), ('HUMBLE', 'PROUD'), ('ABSENT', 'PRESENT'), ('HUSBAND', 'WIFE'),
         ('ABSENT', 'PRESENT'), ('IN', 'OUT'), ('ACCEPT', 'REFUSE'), ('INCLUDE', 'EXCLUDE'), ('ACTIVE', 'PASSIVE'),
         ('INCREASE', 'DECREASE'), ('ADD', 'SUBTRACT'), ('INCREASE', 'DECREASE'), ('ADMIT', 'DENY'),
         ('INDIFFERENT', 'INTERESTED'), ('ADULT', 'CHILD'), ('INNER', 'OUTER'), ('ALIVE', 'DEAD'),
         ('INSIDE', 'OUTSIDE'), ('ALL', 'NONE'), ('INSULT', 'PRAISE'), ('ALLOW', 'REFUSE'), ('INTERESTED', 'BORED'),
         ('ALWAYS', 'NEVER'), ('INTERESTING', 'DULL'), ('ARRIVE', 'DEPART'), ('JOY', 'SORROW'), ('ASLEEP', 'AWAKE'),
         ('JUNIOR', 'SENIOR'), ('BACK', 'FRONT'), ('KIND', 'CRUEL'), ('BACKWARDS', 'FORWARD'), ('KIND', 'CRUEL'),
         ('BAD', 'GOOD'), ('KNOWLEDGE', 'IGNORANCE'), ('BARREN', 'FERTILE'), ('LAZY', 'INDUSTRIOUS'),
         ('BEAUTIFUL', 'UGLY'), ('LEAD', 'FOLLOW'), ('BEFORE', 'AFTER'), ('LEAST', 'GREATEST'), ('BEGIN', 'END'),
         ('LEAVE', 'ARRIVE'), ('BENT', 'STRAIGHT'), ('LEND', 'BORROW'), ('BEST', 'WORST'), ('LEVEL', 'STEEP'),
         ('BETTER', 'WORSE'), ('LIFE', 'DEATH'), ('BIG', 'SMALL'), ('LIQUID', 'SOLID'), ('BLACK', 'WHITE'),
         ('LONG', 'SHORT'), ('BLAMELESS', 'GUILTY'), ('LOSS', 'GAIN'), ('BLESS', 'CURSE'), ('LOUD', 'SOFT'),
         ('BLUNT', 'SHARP'), ('LOVE', 'HATE'), ('BOLD', 'TIMID'), ('MAJORITY', 'MINORITY'), ('BOLD', 'TIMID'),
         ('MANY', 'FEW'), ('BOSS', 'EMPLOYEE'), ('MASCULINE', 'FEMININE'), ('BRAVERY', 'COWARDICE'),
         ('MASTER', 'SERVANT'), ('BREAK', 'REPAIR'), ('MEAN', 'KIND'), ('BRIDGE', 'TUNNEL'), ('MISER', 'SPENDTHRIFT'),
         ('BRIGHT', 'DULL'), ('MODERN', 'ANCIENT'), ('BROAD', 'NARROW'), ('MOST', 'LEAST'), ('BUSY', 'IDLE'),
         ('MOTORIST', 'PEDESTRIAN'), ('BUY', 'SELL'), ('MOUNTAIN', 'VALLEY'), ('CAPTURE', 'RELEASE'),
         ('NATURAL', 'ARTIFICIAL'), ('CATCH', 'THROW'), ('NEAR', 'FAR'), ('CHEAP', 'DEAR'), ('NEVER', 'ALWAYS'),
         ('CITY', 'COUNTRY'), ('NIECE', 'NEPHEW'), ('CLEAN', 'DIRTY'), ('NOISE', 'SILENCE'), ('CLEVER', 'FOOLISH'),
         ('NOISY', 'QUIET'), ('CLOUDY', 'CLEAR'), ('NORMAL', 'ABNORMAL'), ('CLUMSY', 'GRACEFUL'), ('NORTH', 'SOUTH'),
         ('COARSE', 'FINE'), ('NOTICE', 'IGNORE'), ('COLD', 'HOT'), ('OBEY', 'COMMAND'), ('COME', 'GO'),
         ('OBTAIN', 'GIVE'), ('COMEDY', 'TRAGEDY'), ('OFTEN', 'SELDOM'), ('COMFORT', 'DISTURB'), ('OLD', 'NEW'),
         ('COMMON', 'RARE'), ('OMIT', 'INCLUDE'), ('COMMON', 'UNUSUAL'), ('OPEN', 'CLOSE'), ('CONTRACT', 'EXPAND'),
         ('ORDER', 'CHAOS'), ('COOL', 'WARM'), ('OVERLOOK', 'NOTICE'), ('COWARD', 'HERO'), ('PARDON', 'PUNISH'),
         ('COWARDLY', 'BOLD'), ('PART', 'WHOLE'), ('CREATE', 'DESTROY'), ('PAST', 'FUTURE'), ('CRY', 'LAUGH'),
         ('PEACE', 'WAR'), ('DAILY', 'NIGHTLY'), ('PLURAL', 'SINGULAR'), ('DANGER', 'SAFETY'), ('POLITE', 'RUDE'),
         ('DARK', 'BRIGHT'), ('POLITE', 'RUDE'), ('DAWN', 'DUSK'), ('POOR', 'RICH'), ('DAY', 'NIGHT'),
         ('POWERFUL', 'WEAK'), ('DEEP', 'SHALLOW'), ('PRAISE', 'BLAME'), ('DEPTH', 'HEIGHT'), ('PUBLIC', 'PRIVATE'),
         ('DIE', 'LIVE'), ('PUBLIC', 'PRIVATE'), ('DIFFICULT', 'EASY'), ('PUNISH', 'REWARD'), ('DIM', 'BRIGHT'),
         ('PUPIL', 'TEACHER'), ('DISCOURTEOUS', 'POLITE'), ('PURCHASE', 'SELL'), ('DIVIDE', 'MULTIPLY'),
         ('PUSH', 'PULL'), ('DOCTOR', 'PATIENT'), ('QUESTION', 'ANSWER'), ('DRUNK', 'SOBER'), ('QUICK', 'SLOW'),
         ('DRY', 'WET'), ('RAW', 'COOKED'), ('DWARF', 'GIANT'), ('RAW', 'COOKED'), ('EARLY', 'LATE'),
         ('REAL', 'IMAGINARY'), ('EAST', 'WEST'), ('RIGHT', 'LEFT'), ('EASY', 'DIFFICULT'), ('RISE', 'FALL'),
         ('EBB', 'FLOW'), ('ROUGH', 'SMOOTH'), ('EMPTY', 'FULL'), ('SAD', 'CHEERFUL'), ('ENEMY', 'FRIEND'),
         ('SAFE', 'DANGEROUS'), ('ENJOY', 'DISLIKE'), ('SAFE', 'DANGEROUS'), ('ENTRANCE', 'EXIT'),
         ('SAME', 'DIFFERENT'), ('EVENING', 'MORNING'), ('SEPARATE', 'JOIN'), ('EVER', 'NEVER'), ('SEVERAL', 'FEW'),
         ('EVERYBODY', 'NOBODY'), ('SILLY', 'SERIOUS'), ('EVERYWHERE', 'NOWHERE'), ('SIMILAR', 'DIFFERENT'),
         ('EXIT', 'ENTRANCE'), ('SLIM', 'FAT'), ('FACT', 'FICTION'), ('SMILE', 'FROWN'), ('FAILURE', 'SUCCESS'),
         ('SMILE', 'FROWN'), ('FAIR', 'DARK'), ('STRAIGHT', 'CROOKED'), ('FAMOUS', 'UNKNOWN'), ('STRAIGHT', 'CROOKED'),
         ('FANCY', 'PLAIN'), ('STRANGE', 'FAMILIAR'), ('FAR', 'NEAR'), ('STRONG', 'WEAK'), ('FAT', 'THIN'),
         ('SUMMER', 'WINTER'), ('FAT', 'SKINNY'), ('SWEET', 'SOUR'), ('FEW', 'MANY'), ('SWEET', 'SOUR'),
         ('FIND', 'LOSE'), ('TALK', 'LISTEN'), ('FINISH', 'START'), ('TALL', 'SHORT'), ('FIRST', 'LAST'),
         ('TAME', 'WILD'), ('FLATTER', 'INSULT'), ('TEACH', 'LEARN'), ('FOE', 'FRIEND'), ('TEACHER', 'STUDENT'),
         ('FOOLISH', 'WISE'), ('THESE', 'THOSE'), ('FOREIGN', 'LOCAL'), ('THICK', 'THIN'), ('FORGET', 'REMEMBER'),
         ('THIS', 'THAT'), ('FOUND', 'LOST'), ('TIGHT', 'LOOSE'), ('FREEZE', 'THAW'), ('TINY', 'HUGE'),
         ('FRESH', 'STALE'), ('TOP', 'BOTTOM'), ('FRESH', 'STALE'), ('TRAINER', 'TRAINEE'), ('FRIEND', 'ENEMY'),
         ('TRUST', 'DOUBT'), ('FULL', 'VACANT'), ('TRUTH', 'LIE'), ('FUTURE', 'PAST'), ('UNDER', 'OVER'),
         ('GENEROUS', 'SELFISH'), ('UNUSUAL', 'ORDINARY'), ('GIVE', 'RECEIVE'), ('UP', 'DOWN'), ('GIVE', 'TAKE'),
         ('UPSET', 'COMFORT'), ('GRACEFUL', 'AWKWARD'), ('VACANT', 'OCCUPIED'), ('GUILTY', 'INNOCENT'),
         ('VACANT', 'OCCUPIED'), ('GUILTY', 'INNOCENT'), ('VALUABLE', 'WORTHLESS'), ('HAPPY', 'SAD'),
         ('VICTORY', 'DEFEAT'), ('HAPPY', 'SAD'), ('VILLAIN', 'HERO'), ('HARD', 'EASY'), ('WAR', 'PEACE'),
         ('HARD', 'SOFT'), ('WIDE', 'NARROW'), ('HEAD', 'TAIL'), ('WIN', 'LOSE'), ('HEAVY', 'LIGHT'),
         ('WISE', 'FOOLISH'), ('HELL', 'HEAVEN'), ('WITHIN', 'WITHOUT'), ('HELP', 'HINDER'), ('WORK', 'REST'),
         ('HERE', 'THERE'), ('WRONG', 'RIGHT'), ('HIDE', 'SHOW'), ('YES', 'NO'), ('HIGH', 'LOW')]

Parts = ["O", "│", '/', '\\', '/', '\\']

weelcomescreen()

def maingame():
    while True:

            clear()

            hanged_parts = ['O', ' ', ' ', ' ', ' ', ' ']
            alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z']

            var = ''
            wrong = 0
            win = 0
            changeword = False

            antonym, original = words[randint(0, 259)]
            original = list(original)
            lenght = len(original)
            copy = ['-' for i in range(lenght)]

            hangimage(hanged_parts, alphas)
            disword(antonym, copy, wrong)

            while wrong < 5 and win < lenght:
                flag = True
                inp = getch().upper()
                if inp.isalpha():
                    if inp in alphas:
                        for i in range(lenght):
                            if original[i] == inp:
                                copy[i] = inp
                                flag = False
                                win += 1
                        if flag:
                            wrong += 1
                    else:
                        wrong += 1
                        
                    alphas[ord(inp) - 65] = '■'
                elif inp == '0':
                    changeword = True
                    break
                else:
                    continue
                clear()

                hanged_parts[wrong] = Parts[wrong]
                hangimage(hanged_parts, alphas)
                disword(antonym, copy, wrong)
                
            if not changeword:
                if win == lenght:
                    print('           You:  Won')
                else:
                    print('       Correct:  ', *original, sep='')
                    print('           You:  Lost')
                    print()

                print('\n')
                print('   >> PRESS R TO PLAY AGAIN <<')
                print('   >> PRESS ANY KEY TO EXIT <<')
                playexit = getch().upper()
                if playexit != 'R':
                    break

while True:
    option = gamemenu()
    if option == 1:
        maingame()
    elif option == 2:
        instructionenu()
    else:
        break
