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

def type_text(text , speed = 0.3 , color = Colors.RESET):
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
    type_text(">>> Establishing secure connection to GitHub...", 0.03, Colors.CYAN)
    time.sleep(0.5)
    type_text(">>> Access Granted.\n", 0.05, Colors.GREEN)

    type_text("Welcome to MohammadHosseinYazdnafar's Terminal!", 0.05, Colors.YELLOW)
    type_text("Type the number of the file you want to access:\n", 0.03)




    while True:
        print(f"{Colors.CYAN}==================================={Colors.RESET}")
        print("1. whoami.txt   (About Me)")
        print("2. skills.exe   (My Skills)")
        print("3. contact.sh   (Find Me)")
        print("4. exit         (Log out)")
        print(f"{Colors.CYAN}==================================={Colors.RESET}")

        choice = input(f"{Colors.GREEN}guest@[MohammadHosseinYazdnafar]-pc:~$ {Colors.RESET}")

        if choice == '1':
            type_text("\n[+] Opening whoami.txt...", 0.03, Colors.YELLOW)
            type_text("Hi! I'm MohammadHosseinYazdnafar, a beginner Python developer.", 0.02)
            type_text("This is my very first GitHub project!", 0.02)
            type_text("I love coding, problem solving, and building cool things.\n", 0.02)

        elif choice == '2':
            type_text("\n[+] Executing skills.exe...", 0.03, Colors.YELLOW)
            type_text("Loading skills overview:", 0.02)
            type_text(" - Python [||||||||--] 80%", 0.01)
            type_text(" - Git & GitHub [||||------] 40%", 0.01)
            type_text(" - Terminal Magic [||||||||||] 100%\n", 0.01)

        elif choice == '3':
            type_text("\n[+] Running contact.sh...", 0.03, Colors.YELLOW)
            type_text("You can find me here:", 0.02)
            type_text(f" {Colors.CYAN}* GitHub:{Colors.RESET} github.com/mhmdhsynyzdnfr", 0.02)
            type_text(f" {Colors.CYAN}* Email:{Colors.RESET} mhmdhsynyzdnfr@gmail.com", 0.02)
            type_text(f" {Colors.CYAN}* LinkedIn:{Colors.RESET} linkedin.com/in/mhmdhsynyzdnfr\n", 0.02)

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