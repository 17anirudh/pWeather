import pycountry
import sys
import time

class Fetch:
    def Country(self, nation, RED, RESET):
        if nation in ['russia', 'ussr', 'soviet union']:
            nation = 'Russian Federation'
        elif nation in ['england', 'uk', 'united kingdom', 'northern ireland', 'wales', 'scotland']:
            nation = 'United Kingdom of Great Britain and Northern Ireland'
        elif nation in ['heard island and mcdonald island', 'heard islands and mcdonald islands', 'heard island and the mcdonald island']:
            nation = 'Heard Island and McDonald Islands'
        elif nation in ['uae', 'emirates', 'united arab emirates']: 
            nation = 'United Arab Emirates'
        elif nation in ['bonaire', 'saba', 'bonaire sint eustatius and saba']:
            nation = 'Bonaire, Sint Eustatius and Saba'
        elif nation in ['cocos', 'cocos island', 'cocos islands', 'keeling', 'keeling islands']:
            nation = 'Cocos (Keeling) Islands'
        elif nation in ['zaire', 'car', 'central african republic', 'central africa']:
            nation = 'Central African Republic'  
        elif nation in ["cote d'ivoire", 'cote divoire']:
            nation = "Côte d'Ivoire"
        elif nation in ['curacao']:
            nation = 'Curaçao'
        elif nation in ['djiboti', 'dibouti']:
            nation = 'Djibouti'
        elif nation in ['falkland island', 'malvinas', 'falkland islands', 'falkland islands - Malvinas']:
            nation = 'Falkland Islands (Malvinas)'
        elif nation in ['micronesia', 'federated states of micronesia']:
            nation = 'Micronesia, Federated States of'
        elif nation in ['south georgia islands', 'south sandwich islands', 'south georgia and sandwick island', 'south georgia and sandwick islands']:
            nation = 'South Georgia and the South Sandwich Islands'
        elif nation in ['palestine']:
            nation = 'Palestine, State of'
        elif nation in ['reunion']:
            nation = 'Réunion'
        elif nation in ['st barthelemy', 'saint barthelemy']:
            nation = 'Saint Barthélemy'
        elif nation in ['saint helena, ascension and tristan da cunha', 'saint helena', 'ascension', 'tristan da cunha', 'saint helena ascension and tristan da cunha']:
            nation = 'Saint Helena, Ascension and Tristan da Cunha'
        try:
            location = pycountry.countries.lookup(nation)
            return location.alpha_2
        except LookupError:
            time.sleep(1)
            sys.exit(f'{RED}Enter valid country{RESET}')

    def Second(self, RED, GREEN, YELLOW, MAGENTA, RESET):
        print(f'{GREEN}1)Enter locality name\n2)Enter zip/pin code{RESET}')
        choice = int(input(f'{MAGENTA}Choose an option (1/2): {RESET}'))
        if choice == 1:
            user_input = str(input(f'{YELLOW}Enter valid name: {RESET}'))
            return user_input
        elif choice == 2:
            user_input = int(input(f'{YELLOW}Enter proper code: {RESET}'))
            return user_input
        else:
            sys.exit(f'{RED}Choose only 1 or 2{RESET}')

        