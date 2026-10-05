import os
import sys
import time


class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.03, color=Colors.RESET):
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_ascii_art():
    art = f"""{Colors.GREEN}
  _   _      _ _         ____ _ _   _   _       _     _ 
 | | | | ___| | | ___   / ___(_) |_| | | | _   _| |__ | |
 | |_| |/ _ \ | |/ _ \ | |  _| | __| |_| || | | | '_ \| |
 |  _  |  __/ | | (_) || |_| | | |_|  _  || |_| | |_) |_|
 |_| |_|\___|_|_|\___/  \____|_|\__|_| |_| \__,_|_.__/(_)
{Colors.RESET}"""
    print(art)

def main():
    clear_screen()
    show_ascii_art()

    type_text(">>> System Booting...", 0.05, Colors.CYAN)
    type_text(">>> Loading profile: Mohammad Hossein Yazdanfar...", 0.03, Colors.CYAN)
    time.sleep(0.5)
    type_text(">>> Access Granted.\n", 0.05, Colors.GREEN)

    type_text("Welcome to Mohammad Hossein's Terminal!", 0.05, Colors.YELLOW)
    type_text("Type the number of the file you want to access:\n", 0.03)

    while True:
        print(f"{Colors.CYAN}==================================={Colors.RESET}")
        print("1. whoami.txt   (About Me)")
        print("2. skills.exe   (My Skills)")
        print("3. contact.sh   (Find Me)")
        print("4. exit         (Log out)")
        print(f"{Colors.CYAN}==================================={Colors.RESET}")

        choice = input(f"{Colors.GREEN}guest@mhyazdanfar-pc:~$ {Colors.RESET}")

        if choice == '1':
            type_text("\n[+] Opening whoami.txt...", 0.03, Colors.YELLOW)
            type_text("Hi! I'm Mohammad Hossein Yazdanfar, a 20-year-old Computer Engineering student.", 0.02)
            type_text("I am currently studying at Shahid Beheshti University.", 0.02)
            type_text("I became interested in the world of computers during my childhood;", 0.02)
            type_text("a growing curiosity drove me to try and understand this fascinating, man-made marvel.", 0.02)
            type_text("Programming, AI, game development, hardware, graphics, and photo and video editing", 0.02)
            type_text("all captured my interest and led me to where I am today: eager to learn more and discover new things in this exciting realm.",0.02)
            type_text("When I'm not studying or coding, I'm probably playing video games or watching movies.\n", 0.02)

        elif choice == '2':
            type_text("\n[+] Executing skills.exe...", 0.03, Colors.YELLOW)
            type_text("Loading tech stack and skills:", 0.02)
            type_text(" - Python                 [||||||||||] Advanced", 0.01)
            type_text(" - AI Models              [||||||||--] Intermediate", 0.01)
            type_text(" - C++ & C#               [||||||||--] Intermediate", 0.01)
            type_text(" - Game Dev (Unity, 2D)   [|||||||---] Intermediate", 0.01)
            type_text(" - Git & Linux            [|||||-----] Beginner", 0.01)
            type_text(" - Web (Flask, HTML, CSS) [|||||-----] Beginner", 0.01)
            type_text(" - Database (SQL)         [|||||-----] Beginner", 0.01)
            type_text(" - Hardware (Verilog, ASM)[|||||-----] Beginner\n", 0.01)



        elif choice == '3':
            type_text("\n[+] Running contact.sh...", 0.03, Colors.YELLOW)
            type_text("Let's connect! You can find me here:", 0.02)
            type_text(f"{Colors.CYAN}* Location:{Colors.RESET} Tehran, Iran ", 0.02)
            type_text(f"{Colors.CYAN}* Phone:{Colors.RESET} 09012040483", 0.02)
            type_text(f"{Colors.CYAN}* GitHub:{Colors.RESET} github.com/mhmdhsynyzdnfr", 0.02)
            type_text(f"{Colors.CYAN}* LinkedIn:{Colors.RESET} linkedin.com/in/mhmdhsynyzdnfr\n", 0.02)

        elif choice == '4':
            type_text("\nLogging out...", 0.05, Colors.RED)
            type_text("Connection closed. Goodbye!", 0.03)
            break

        else:
            type_text("\n[!] Command not found. Please enter 1, 2, 3, or 4.\n", 0.02, Colors.RED)

        time.sleep(1)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program terminated by user.{Colors.RESET}")
        sys.exit()