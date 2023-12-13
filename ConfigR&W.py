import configparser
import json
import os
from configparser import ConfigParser
from getpass import getpass
import sys

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'

config_folder: str = 'Config'
token_file: str = f'{config_folder}/HoneygainToken.json'
config_path: str = f'{config_folder}/HoneygainConfig.toml'
header: dict[str, str] = {'Authorization': ''}

def create_config():
    cfg: ConfigParser = ConfigParser()
    cfg.add_section('User')
    if os.getenv('GITHUB_ACTIONS') == 'true':
        if os.getenv('IsJWT') == '1':
            token = os.getenv('JWT_TOKEN')
            cfg.set('User', 'token', f"{token}")
        else:
            email = os.getenv('MAIL')
            password = os.getenv('PASS')
            cfg.set('User', 'email', f"{email}")
            cfg.set('User', 'password', f"{password}")
    else:
        print(f"{Colors.WARNING}### Config setup ###{Colors.ENDC}")
        print(f"{Colors.WHITE}Please choose your main authentication method:{Colors.ENDC}")
        print(f"{Colors.WHITE}1. Using Token{Colors.ENDC}")
        print(f"{Colors.WHITE}2. Using Email and Password{Colors.ENDC}")

        choice = input(f"{Colors.WHITE}Enter your choice (1 or 2):{Colors.ENDC}")
        if choice == '1':
            token = input(f"{Colors.WHITE}Token: {Colors.ENDC}")
            cfg.set('User', 'token', f"{token}")
            cfg.set('User', 'IsJWT', '1') 
            os.environ['IsJWT'] = '1'
        elif choice == '2':
            email = input(f"{Colors.WHITE}Email: {Colors.ENDC}")
            password = getpass(f"{Colors.WHITE}Password: {Colors.ENDC}")
            cfg.set('User', 'email', f"{email}")
            cfg.set('User', 'password', f"{password}")
            cfg.set('User', 'IsJWT', '0')
        else:
            print(f"{Colors.FAIL}Wrong input, could not read it correctly. Try again!{Colors.ENDC}")
            create_config()   
    print(f"{Colors.WHITE}Created 'Config' folder at:", os.path.join(os.getcwd(), f"{Colors.WHITE}Config{Colors.ENDC}"))
    cfg.add_section('Settings')
    cfg.set('Settings', 'Lucky Pot', 'True')
    cfg.set('Settings', 'Achievements', 'True')
    cfg.add_section('Url')
    cfg.set('Url', 'login', 'https://dashboard.honeygain.com/api/v1/users/tokens')
    cfg.set('Url', 'pot', 'https://dashboard.honeygain.com/api/v1/contest_winnings')
    cfg.set('Url', 'balance', 'https://dashboard.honeygain.com/api/v1/users/balances')
    cfg.set('Url', 'achievements', 'https://dashboard.honeygain.com/api/v1/achievements/')
    cfg.set('Url', 'achievement_claim', 'https://dashboard.honeygain.com/api/v1/achievements/claim')
    with open(config_path, 'w', encoding='utf-8') as configfile:
        configfile.truncate(0)
        configfile.seek(0)
        cfg.write(configfile)

print(f"{Colors.WARNING}----------- Welcome to HoneygainPot Config Reader and Writer -----------{Colors.ENDC}")
print(f"{Colors.OKBLUE}Made by GFx and MrLolf{Colors.ENDC}")

if not os.path.exists(config_folder):
    print(f"{Colors.FAIL}'Config' folder not found. Creating configuration...{Colors.ENDC}")
    os.makedirs(config_folder)
    create_config()

config: ConfigParser = ConfigParser()
config.read(config_path)

is_jwt = config.get('User', 'IsJWT', fallback='0')

if is_jwt == '1' or os.getenv('IsJWT') == '1':
    print(f"{Colors.OKGREEN}Using JWT Token: Yes{Colors.ENDC}")
    print(f"{Colors.FAIL}Using Mail and Password: No{Colors.ENDC}")
    os.environ['IsJWT'] = '1'
else:
    print(f"{Colors.FAIL}Using JWT Token: No{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Using Mail and Password: Yes{Colors.ENDC}")

print(f"{Colors.WHITE}Codename: Sandy{Colors.ENDC}")
print(f"{Colors.WHITE}Config folder:", os.path.join(os.getcwd(), f"{Colors.WHITE}Config{Colors.ENDC}"))
print(f"{Colors.WARNING}---------------------------------------------------------------------{Colors.ENDC}")
choice = input(f"{Colors.WHITE}Do you want to edit the config file (Y/N): ?{Colors.ENDC}")
if choice.lower() == 'y':
    create_config()

if not config.has_section('User') or not config.has_section('Settings') or not config.has_section('Url'):
    print(f"{Colors.FAIL}Incomplete or missing information in the config{Colors.ENDC}")
    print(f"{Colors.WARNING}Removed the existing configuration file...{Colors.ENDC}")
    if os.path.exists(config_path):
        os.remove(config_path)
    create_config()
