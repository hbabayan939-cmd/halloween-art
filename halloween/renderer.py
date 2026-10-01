import time
import sys
from halloween.colors import ORANGE, WHITE, GREEN, RESET

COLOR_MAP = {
    "pumpkin": ORANGE,
    "ghost": WHITE,
    "skeleton": GREEN,
}

def render(art: str, color: bool = False, animate: bool = False):
    output = art
    if color:
        output = f"{ORANGE}{art}{RESET}"
    if animate:
        animate_art(output)
    else:
        print(output)

def animate_art(art: str):
    for frame in range(3):
        sys.stdout.write("\033[2J\033[H")  # clear screen
        sys.stdout.write(art)
        sys.stdout.flush()
        time.sleep(0.5)