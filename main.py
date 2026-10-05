import os
import sys


class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text , speed = 0.3 , color = COLOR.RESET):
    ...

def show_ascii_art():
    ...

def main():
    clear_screen()
    show_ascii_art()




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # برای جلوگیری از ارور وقتی کاربر Ctrl+C را می‌زند
        print(f"\n{Colors.RED}Program terminated by user.{Colors.RESET}")
        sys.exit()