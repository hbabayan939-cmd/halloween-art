ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"
GREEN = "\033[38;5;46m"
RESET = "\033[0m"

def colorize(text: str, color: str) -> str:
    return f"{color}{text}{RESET}"