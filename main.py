import fetching
import retrieve
import time
import sys
import os

def main():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    try:
        a2 = retrieve.Network()
        a = input(f'{RED}Enter your OpenWeather API key to proceed: {RESET}')
        print('Verifying....\n')
        a2.verify(a, RED, RESET)
        time.sleep(1)
        
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        if a:
            API_KEY = a
            a1 = fetching.Fetch()
            
            print(f"{RED}**************************************************{RESET}")

            nation = str(input(f'{CYAN}Enter full country name: {RESET}'))
            nation = nation.lower()
            alpha = a1.Country(nation, RED, RESET)
            time.sleep(1)

            second = a1.Second(RED, GREEN, YELLOW, MAGENTA, RESET)
            
            response = a2.Coord(alpha, second, API_KEY, RED, RESET)

            a2.Display(response, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET)
            print(f"{RED}**************************************************{RESET}")
            print('\n')

        else:
            sys.exit('Enter a valid API key')

    except KeyboardInterrupt:
        sys.exit('\nExiting....')


if __name__ == '__main__':
    main()

