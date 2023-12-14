import configparser
import json
import os
from configparser import ConfigParser
from getpass import getpass
import sys

class colors:
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

def create_config():
    cfg: ConfigParser = ConfigParser()
    cfg.add_section('User')
    cfg.set('User', 'email', "")
    cfg.set('User', 'password', "")
    cfg.set('User', 'token', "")
    if os.getenv('GITHUB_ACTIONS') == 'true':
        if os.getenv('IsJWT') == '1':
            token = os.getenv('JWT_TOKEN')
            cfg.set('User', 'token', f"{token}")
            cfg.set('User', 'IsJWT', '1')
        else:
            email = os.getenv('MAIL')
            password = os.getenv('PASS')
            cfg.set('User', 'email', f"{email}")
            cfg.set('User', 'password', f"{password}")
            cfg.set('User', 'IsJWT', '0')
    else:
        print(f"{colors.WARNING}### First time setup ###{colors.ENDC}")
        print(f"{colors.WHITE}Please choose authentication method:{colors.ENDC}")
        print(f"{colors.WHITE}1. Using Token{colors.ENDC}")
        print(f"{colors.WHITE}2. Using Email and Password{colors.ENDC}")
        choice = input(f"{colors.WHITE}Enter your choice (1 or 2):{colors.ENDC}")
        if choice == '1':
            token = input(f"{colors.WHITE}Token: {colors.ENDC}")
            cfg.set('User', 'token', f"{token}")
            cfg.set('User', 'IsJWT', '1')
            os.environ['IsJWT'] = '1'
        elif choice == '2':
            email = input(f"{colors.WHITE}Email: {colors.ENDC}")
            password = getpass(f"{colors.WHITE}Password: {colors.ENDC}")
            cfg.set('User', 'email', f"{email}")
            cfg.set('User', 'password', f"{password}")
            cfg.set('User', 'IsJWT', '0')
        else:
            print(f"{colors.FAIL}Wrong Input could not read it correctly. Try again!{colors.ENDC}")
            create_config()
            
    print(f"{colors.WHITE}Created 'Config' folder at:", os.path.join(os.getcwd(), f"{colors.WHITE}Config{colors.ENDC}"))
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

print(f"{colors.WARNING}----------- Welcome to HoneygainPot Config Reader and Writer -----------{colors.ENDC}")
print(f"{colors.OKBLUE}Made by GFx and MrLolf{colors.ENDC}")

config: ConfigParser = ConfigParser()
config.read(config_path)

def check_config_integrity(conf: ConfigParser) -> None:
    if not os.path.exists(config_folder):
        print(f"{colors.WARNING}Creating new config folder at:", os.path.join(os.getcwd()))
        os.mkdir(config_folder)
    if not os.path.isfile(config_path) or os.stat(config_path).st_size == 0:
        create_config()
        return
    conf.read(config_path)
    if (not conf.has_section('User') or not conf.has_section('Settings')
            or not conf.has_section('Url')):
        create_config()


check_config_integrity(config)
config.read(config_path)

is_jwt = config.get('User', 'IsJWT', fallback='0')

if is_jwt == '1' or os.getenv('IsJWT') == '1':
    print(f"{colors.OKGREEN}Using JWT Token: Yes{colors.ENDC}")
    print(f"{colors.FAIL}Using Mail and Password: No{colors.ENDC}")
    os.environ['IsJWT'] = '1'
else:
    print(f"{colors.FAIL}Using JWT Token: No{colors.ENDC}")
    print(f"{colors.OKGREEN}Using Mail and Password: Yes{colors.ENDC}")

print(f"{colors.WHITE}Codename: Sandy{colors.ENDC}")
print(f"{colors.WHITE}Config folder:", os.path.join(os.getcwd(), f"{colors.WHITE}Config{colors.ENDC}"))
print(f"{colors.WARNING}---------------------------------------------------------------------{colors.ENDC}")
choice = input(f"{colors.WHITE}Do you want to edit the config file (Y/N): {colors.ENDC}")
if choice.lower() == 'y':
    create_config()

if not config.has_section('User') or not config.has_section('Settings') or not config.has_section('Url'):
    print(f"{colors.FAIL}Incomplete or missing information in the config{colors.ENDC}")
    print(f"{colors.WARNING}Removed the existing configuration file...{colors.ENDC}")
    if os.path.exists(config_path):
        os.remove(config_path)
    create_config()
