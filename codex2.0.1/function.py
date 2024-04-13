from colorama import Fore,init
import time
import pygame


init(autoreset=True)
pygame.init()
def kaishi():
    global start_time
    start_time = time.process_time()

def clrprint(text,color='x'):
    if color == 'red':
        print(Fore.RED + text)
    elif color == 'green':
        print(Fore.GREEN + text)
    elif color == 'yellow':
        print(Fore.YELLOW + text)
    elif color == 'blue':
        print(Fore.BLUE + text)
    elif color == 'magenta':
        print(Fore.MAGENTA + text)
    elif color == 'cyan':
        print(Fore.CYAN + text)
    elif color == 'white':
        print(Fore.WHITE + text)
    elif color == 'reset':
        print(Fore.RESET + text)
    elif color == 'x':
        print(text)
    else:
        print('ERROR:There is no such color')


def random(start, end):
    random_seed = int(time.time() * 1000000) % (end - start + 1)
    random_number = start + random_seed
    return random_number

def play(music_file, num=1):
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(num)
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error as e:
        print(f"PyvavError:Error playing music: {e}")
    except KeyboardInterrupt:
        pygame.mixer.music.stop()

def stop():
    pygame.mixer.music.stop()