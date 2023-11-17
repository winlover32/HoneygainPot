#!/usr/bin/env python3
import configparser
import json
import logging
import os
from configparser import ConfigParser
from getpass import getpass
import requests
from requests import Response

config_folder: str = 'Config'
token_file: str = config_folder + '/HoneygainToken.json'
config_path: str = config_folder + '/HoneygainConfig.toml'
header: dict[str, str] = {'Authorization': ''}

print('--------- Welcome to GitHub Actions ---------')
print('Made by GFx and MrLolf')
print('---------------------------------------------')
print('Starting HoneygainPot 🍯')

def create_config() -> None:
    print('Collecting infomation...')
    cfg: ConfigParser = ConfigParser()
    cfg.add_section('User')
    if os.getenv('IsGit') == '1':
        try:
          email: str = os.getenv('MAIL_JWD')
          password: str = os.getenv('PASS_JWD')
        except:
          print("------ Traceback log ------\n❌ Error code 1: Cannot find 'MAIL_JWD' and 'PASS_JWD'.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
          exit(-1)
    else:
        try:
          email: str = input("Email: ")
          password: str = getpass()
        except:
          print("------ Traceback log ------\n❌ Error code 3: Cannot receive any input, make sure 'IsGit' = 1.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
          exit(-1)
            
    cfg.set('User', 'email', f"{email}")
    cfg.set('User', 'password', f"{password}")
    cfg.add_section('Settings')
    cfg.set('Settings', 'Lucky Pot', 'True')
    cfg.set('Settings', 'Achievements', 'True')
    cfg.add_section('Url')
    cfg.set('Url', 'login', 'https://dashboard.honeygain.com/api/v1/users/tokens')
    cfg.set('Url', 'pot', 'https://dashboard.honeygain.com/api/v1/contest_winnings')
    cfg.set('Url', 'balance', 'https://dashboard.honeygain.com/api/v1/users/balances')
    cfg.set('Url', 'achievements', 'https://dashboard.honeygain.com/api/v1/achievements/')
    cfg.set('Url', 'achievement_claim', 'https://dashboard.honeygain.com/api/v1/achievements/claim')
    with open(config_path, 'w') as configfile:
        configfile.truncate(0)
        configfile.seek(0)
        cfg.write(configfile)

def get_urls(cfg: ConfigParser) -> dict[str, str]:
    urls_conf: dict[str, str] = {}
    try:
        urls_conf: dict[str, str] = {'login': cfg.get('Url', 'login'),
                                     'pot': cfg.get('Url', 'pot'),
                                     'balance': cfg.get('Url', 'balance'),
                                     'achievements': cfg.get('Url', 'achievements'),
                                     'achievement_claim': cfg.get('Url', 'achievement_claim')}
    except configparser.NoOptionError or configparser.NoSectionError:
        create_config()
    return urls_conf

def get_login(cfg: ConfigParser) -> dict[str, str]:
    user: dict[str, str] = {}
    try:
        user: dict[str, str] = {'email': cfg.get('User', 'email'),
                                'password': cfg.get('User', 'password')}
    except configparser.NoOptionError or configparser.NoSectionError:
        create_config()
    return user

def get_settings(cfg: ConfigParser) -> dict[str, bool]:
    settings_dict: dict[str, bool] = {}
    try:
        settings_dict: dict[str, bool] = {'lucky_pot': cfg.getboolean('Settings', 'Lucky Pot'),
                                          'achievements_bool': cfg.getboolean('Settings', 'Achievements')}
    except configparser.NoOptionError or configparser.NoSectionError:
        create_config()
    return settings_dict


if not os.path.exists(config_folder):
    os.mkdir(config_folder)

if not os.path.isfile(config_path) or os.stat(config_path).st_size == 0:
    create_config()

config: ConfigParser = ConfigParser()
config.read(config_path)

if not config.has_section('User') or not config.has_section('Settings') or not config.has_section('Url'):
    create_config()

try:
    settings: dict[str, bool] = get_settings(config)
    urls: dict[str, str] = get_urls(config)
    payload: dict[str, str] = get_login(config)
except configparser.NoOptionError or configparser.NoSectionError:
    create_config()
    settings: dict[str, bool] = get_settings(config)
    urls: dict[str, str] = get_urls(config)
    payload: dict[str, str] = get_login(config)

def login(s: requests.session) -> json.loads:
    print('Logging in to Honeygain 🐝')
    token: Response = s.post(urls['login'], json=payload)
    try:
        return json.loads(token.text)
    except json.decoder.JSONDecodeError:
        print("------ Traceback log ------\n❌ Error code 10: You have exceeded your login tries.\nPlease wait a few hours or return tomorrow.")
        exit(-1)

def gen_token(s: requests.session, invalid: bool = False) -> str | None:
    if not os.path.isfile(token_file) or os.stat(token_file).st_size == 0 or invalid:
        with open(token_file, 'w') as f:
            f.truncate(0)
            f.seek(0)
            token: dict = login(s)
            if "title" in token:
                print("------ Traceback log ------\n❌ Error code 4: Wrong login credentials,please enter the right ones.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
                return None
            json.dump(token, f)
    with open(token_file, 'r+') as f:
        token: dict = json.load(f)
    return token["data"]["access_token"]

def achievements_claim(s: requests.session) -> bool:
    global header
    if settings['achievements_bool']:
        achievements: Response = s.get(urls['achievements'], headers=header)
        try:
          achievements: dict = achievements.json()
        except:
            print("------ Traceback log ------\n❌ Error code 2: You are not eligible to get the lucky pot.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
            exit(-1)
        try:
            for achievement in achievements['data']:
                try:
                    if not achievement['is_claimed'] and achievement['progresses'][0]['current_progress'] == \
                            achievement['progresses'][0]['total_progress']:
                        s.post(urls['achievement_claim'], json={"user_achievement_id": achievement['id']},
                               headers=header)
                        print(f'Claimed {achievement["title"]} ✅')
                except IndexError:
                    if not achievement['is_claimed']:
                        s.post(urls['achievement_claim'], json={"user_achievement_id": achievement['id']},
                        headers=header)
                        print(f'Claimed {achievement["title"]} ✅')
        except KeyError:
            if 'message' in achievements:
                token: str = gen_token(s, True)
                if token is None:
                    print("Exiting HoneygainPot due to false login credentials ❌")
                    exit(-1)
                header = {'Authorization': f'Bearer {token}'}
            return False
        return True

def main() -> None:
    global header
    with requests.session() as s:
        token: str = gen_token(s)
        if token is None:
            print("Closing HoneygainPot due to false login credentials ❌")
            exit(-1)
        header = {'Authorization': f'Bearer {token}'}
        if not achievements_claim(s):
            print('Failed to claim achievements ❌')
            print("------ Traceback log ------\n❌ Error code 2: You are not eligible to get the lucky pot because you still did not reach 15mb of sharing.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
            exit(-1)
        dashboard: Response = s.get(urls['balance'], headers=header)
        dashboard: dict = dashboard.json()
        if 'code' in dashboard and dashboard['code'] == 401:
            print('Invalid token generating new one.')
            token: str = gen_token(s, True)
            header['Authorization'] = f'Bearer {token}'
        pot_winning: Response = s.get(urls['pot'], headers=header)
        pot_winning: dict = pot_winning.json()
        if settings['lucky_pot'] and pot_winning['data']['winning_credits'] is None:
            pot_claim: Response = s.post(urls['pot'], headers=header)
            pot_claim: dict = pot_claim.json()
            try:
              print(f'Claimed {pot_claim["data"]["credits"]} Credits.')
            except:
              print("------ Traceback log ------\n❌ Error code 2: You are not eligible to get the lucky pot because you still did not reach 15mb of sharing.\nPlease refer to: https://github.com/gorouflex/HoneygainPot/blob/main/Debug.md for more information.\nOr create an Issue on GitHub if it still doesn't work for you.")
              exit(-1)
        pot_winning: Response = s.get(urls['pot'], headers=header)
        pot_winning: dict = pot_winning.json()
        print(f'Won today {pot_winning["data"]["winning_credits"]} credits ✅')
        balance: Response = s.get(urls['balance'], headers=header)
        balance: dict = balance.json()
        print(f'You currently have {balance["data"]["payout"]["credits"]} credits 🍯')
        print('Closing HoneygainPot ✅')

if __name__ == '__main__':
    main()
