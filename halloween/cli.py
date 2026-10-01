import argparse
import sys
from halloween.arts import get_art
from halloween.renderer import render

def main():
    parser = argparse.ArgumentParser(prog="halloween", description="Halloween ASCII art in your terminal 🎃")
    parser.add_argument("art", nargs="?", default="pumpkin", choices=["pumpkin", "ghost", "skeleton", "all"], help="Which art to show (default: pumpkin)")
    parser.add_argument("-c", "--color", action="store_true", help="Enable colors")
    parser.add_argument("-a", "--animate", action="store_true", help="Animate the art")
    parser.add_argument("-v", "--version", action="version", version="halloween 0.1.0")

    args = parser.parse_args()

    try:
        art = get_art(args.art)
        render(art, color=args.color, animate=args.animate)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)