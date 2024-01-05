# !/usr/bin/env python3
import configparser
import json
import os
import sys
import shutil
from configparser import ConfigParser
from getpass import getpass
import requests
from requests import Response

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

print(f"{colors.WARNING}------- Welcome to HoneygainPot -------{colors.ENDC}")
print(f"{colors.OKBLUE}Made by GFx and MrLolf{colors.ENDC}")

config: ConfigParser = ConfigParser()
config.read(config_path)
is_jwt = config.get('User', 'IsJWT', fallback='0')

if os.getenv('GITHUB_ACTIONS') == 'true':
    print(f"{colors.OKBLUE}Powered by GitHub Actions V3 and Python{colors.ENDC}")
    print(f"{colors.OKGREEN}Run with GitHub Actions: Yes{colors.ENDC}")
    print(f"{colors.WHITE}Original repo: gorouflex/HoneygainPot{colors.ENDC}")
    print(f"{colors.WHITE}Current forked repo: {os.getenv('GITHUB_REPOSITORY')}{colors.ENDC}")
    user_repo = os.getenv('GITHUB_REPOSITORY')
    ORIGINAL_REPO = 'gorouflex/HoneygainPot'
    user_url = f'https://api.github.com/repos/{user_repo}/commits?path=main.py'
    original_url = f'https://api.github.com/repos/{ORIGINAL_REPO}/commits?path=main.py'
    user_response = requests.get(user_url, timeout=10000)
    original_response = requests.get(original_url, timeout=10000)
    if user_response.status_code == 200 and original_response.status_code == 200:
        user_commit = user_response.json()[0]['sha']
        original_commit = original_response.json()[0]['sha']
        if user_commit == original_commit:
            print(f"{colors.OKGREEN}Your repo is up-to-date with the original repo{colors.ENDC}")
        else:
            print(f"{colors.WARNING}Your repo is not up-to-date with the original repo{colors.ENDC}")
            print(f"{colors.FAIL}Please update your repo to the latest commit{colors.ENDC}{colors.FAIL}to get new updates and bug fixes{colors.ENDC}")
    else:
        print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 4: Failed to fetch commit information\nPlease refer to: https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
        exit(-1)
else:
    print(f"{colors.FAIL}Run with GitHub Actions: No{colors.ENDC}")
is_jwt = config.get('User', 'IsJWT', fallback='0')
if is_jwt == '1' or os.getenv('IsJWT') == '1':
    print(f"{colors.OKGREEN}Using JWT Token: Yes{colors.ENDC}")
    print(f"{colors.FAIL}Using Mail and Pass: No{colors.ENDC}")
    os.environ['IsJWT'] = '1'
else:
    print(f"{colors.FAIL}Using JWT Token: No{colors.ENDC}")
    print(f"{colors.OKGREEN}Using Mail and Pass: Yes{colors.ENDC}")
print(f"{colors.WHITE}Codename: Sandy{colors.ENDC}")
print(f"{colors.WHITE}Config folder:", os.path.join(os.getcwd(), f"{colors.WHITE}Config{colors.ENDC}"))
print(f"{colors.WARNING}---------------------------------------{colors.ENDC}")
print(f"{colors.WHITE}Starting HoneygainPot 🍯{colors.ENDC}")
print(f"{colors.WHITE}Collecting information...{colors.ENDC}")

def create_config() -> None:
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

def get_urls(cfg: ConfigParser) -> dict[str, str]:
    urls_conf: dict[str, str] = {}
    try:
        urls_conf: dict[str, str] = {'login': cfg.get('Url', 'login'),
                                     'pot': cfg.get('Url', 'pot'),
                                     'balance': cfg.get('Url', 'balance'),
                                     'achievements': cfg.get('Url', 'achievements'),
                                     'achievement_claim': cfg.get('Url', 'achievement_claim')}
    except configparser.NoOptionError:
        create_config()
    except configparser.NoSectionError:
        create_config()
    return urls_conf

def get_login(cfg: ConfigParser) -> dict[str, str]:
    user: dict[str, str] = {}
    try:
        if os.getenv('IsJWT') == '1':
            token = cfg.get('User', 'token')
            user: dict[str, str] = {'token': token}
        else:
            user: dict[str, str] = {'email': cfg.get('User', 'email'),
                                    'password': cfg.get('User', 'password')}
    except configparser.NoOptionError:
        create_config()
    except configparser.NoSectionError:
        create_config()
    return user

def get_settings(cfg: ConfigParser) -> dict[str, bool]:
    settings_dict: dict[str, bool] = {}
    try:
        settings_dict: dict[str, bool] = {'lucky_pot': cfg.getboolean('Settings', 'Lucky Pot'),
                                          'achievements_bool': cfg.getboolean('Settings',
                                                                              'Achievements')}
    except configparser.NoOptionError:
        create_config()
    except configparser.NoSectionError:
        create_config()
    return settings_dict
    
try:
    settings: dict[str, bool] = get_settings(config)
    urls: dict[str, str] = get_urls(config)
    payload: dict[str, str] = get_login(config)
except configparser.NoOptionError:
    create_config()
except configparser.NoSectionError:
    create_config()
finally:
    settings: dict[str, bool] = get_settings(config)
    urls: dict[str, str] = get_urls(config)
    payload: dict[str, str] = get_login(config)

def login(s: requests.session) -> json.loads:
    print(f"{colors.WHITE}Logging in to Honeygain 🐝{colors.ENDC}")
    if os.getenv('IsJWT') == '1':
        return {'data': {'access_token': payload['token']}}
    token: Response = s.post(urls['login'], json=payload)
    try:
        return json.loads(token.text)
    except json.decoder.JSONDecodeError:
        print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 3: You have exceeded your login tries\nPlease wait a few hours or return tomorrow\nPlease refer to: https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
        exit(-1)

def gen_token(s: requests.session, invalid: bool = False) -> str | None:
    if not os.path.isfile(token_file) or os.stat(token_file).st_size == 0 or invalid:
        with open(token_file, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.seek(0)
            token: dict = login(s)
            if "title" in token:
                print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 2: Wrong login credentials,please enter the right ones\nPlease refer to: https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
                exit(-1)
                return None
            json.dump(token, f)
    with open(token_file, 'r+', encoding='utf-8') as f:
        token: dict = json.load(f)
    return token["data"]["access_token"]

def achievements_claim(s: requests.session, header: dict[str, str]) -> bool:
    if not settings['achievements_bool']:
        return False
    achievements: Response = s.get(urls['achievements'], headers=header)
    achievements: dict = achievements.json()
    if 'data' not in achievements:
        return False
    for achievement in achievements['data']:
        if (not achievement['is_claimed'] and 'progresses' in achievement and
                achievement['progresses'] == []):
            s.post(urls['achievement_claim'],
                   json={"user_achievement_id": achievement['id']},
                   headers=header)
            print(f"{colors.WARNING}Trying to claim {achievement['title']}{colors.ENDC}")
        elif (not achievement['is_claimed'] and 'progresses' in achievement and
              not achievement['progresses'] == [] and
              achievement['progresses'][0]['current_progress'] ==
              achievement['progresses'][0]['total_progress']):
            s.post(urls['achievement_claim'],
                   json={"user_achievement_id": achievement['id']},
                   headers=header)
            print(f"{colors.OKGREEN}Claimed {achievement['title']} ✅{colors.ENDC}")
    return True

def main() -> None:
    with requests.session() as s:
        token: str = gen_token(s)
        if token is None:
            print(f"{colors.FAIL}Closing HoneygainPot due to false login credentials ❌{colors.ENDC}")
            exit(-1)
        header: dict[str, str] = {'Authorization': f'Bearer {token}'}
        if not achievements_claim(s, header):
            print(f"{colors.FAIL}Failed to claim achievements ❌{colors.ENDC}")
            exit(-1)
        dashboard: Response = s.get(urls['balance'], headers=header)
        dashboard: dict = dashboard.json()
        if 'code' in dashboard and dashboard['code'] == 401:
            print(f"{colors.FAIL}Invalid token generating new one{colors.ENDC}")
            token: str = gen_token(s, True)
            header['Authorization'] = f'Bearer {token}'
        pot_winning: Response = s.get(urls['pot'], headers=header)
        pot_winning: dict = pot_winning.json()
        if 'data' not in pot_winning:
             print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 2: Wrong login credentials,please enter the right ones\nPlease refer to: https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
             exit(-1)
        if settings['lucky_pot'] and pot_winning['data']['winning_credits'] is None:
            pot_claim: Response = s.post(urls['pot'], headers=header)
            pot_claim: dict = pot_claim.json()
            if 'type' in pot_claim and pot_claim['type'] == 400:
                print(f"{colors.WARNING}--------- Traceback log ---------{colors.ENDC}\n{colors.FAIL}❌ Error code 1: You are not eligible to get the lucky pot because you do not reach 15mb of sharing bandwich everyday ( following to Honeygain's TOS )\nPlease refer to: https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug.md for more information\nOr create an Issue on GitHub if it still doesn't work for you.{colors.ENDC}")
                exit(-1)
                return
            print(f"{colors.OKGREEN}Claimed {pot_claim['data']['credits']} credits ✅{colors.ENDC}")
        pot_winning: Response = s.get(urls['pot'], headers=header)
        pot_winning: dict = pot_winning.json()
        print(f"{colors.OKGREEN}Won today {pot_winning['data']['winning_credits']} credits ✅{colors.ENDC}")
        balance: Response = s.get(urls['balance'], headers=header)
        balance: dict = balance.json()
        print(f"{colors.OKGREEN}You currently have {balance['data']['payout']['credits']} credits 🍯{colors.ENDC}")

if __name__ == '__main__':
    main()
    if os.getenv('GITHUB_ACTIONS') == 'true':
       try:
         shutil.rmtree(config_folder)
         print(f"{colors.WARNING}Cleaning up...{colors.ENDC}")
       except Exception as e:
         print(f"{colors.FAIL}Error deleting config folder: {e}{colors.ENDC}")
         exit(-1)
    print(f"{colors.OKGREEN}Closing HoneygainPot ✅{colors.ENDC}")
