<h1 align="center">HoneygainPot - Project Sandy</h1>
<h4 align="center">🐝 A bot that claims Honeygain lucky pot every day 🍯</h4>
<h4 align="center">Powered by GitHub Actions 🐙 and Python 🐍</h4>
<p align="center">
<img src="https://img.shields.io/github/forks/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/stars/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/contributors/gorouflex/HoneygainPot?style=flat">
<p align="center">
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/codeql.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/codeql.yml/badge.svg"></a>
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/cl.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/cl.yml/badge.svg"></a>
</p>
<p align="center">
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml/badge.svg"></a>
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml/badge.svg"></a> (*)
</p>
<p align="center">
  <a href="https://github.com/gorouflex/HoneygainPot/">English 🇺🇸</a>
  •
  <a href="Docs/README-vn.md">Tiếng Việt 🇻🇳</a>
<p align="center">
  <a href="Docs/Debug.md">Debug</a>  
  •
  <a href="Docs/FAQ.md">FAQ</a> 
  •
  <a href="#feature">Feature</a>
  •
  <a href="#usage">Usage</a>     
  •
  <a href="#preview">Preview</a>
  •
  <a href="#disclaimer">Disclaimer</a>
<p align="left">
<img src="Img/Logo.png"               
     width="170" 
     height="170">
</p>

### [Honeygain](https://r.honeygain.me/BADBO762DE) is a service that allows you to earn **passive income** by **sharing** your **internet** connection with businesses for web statistics, price comparison, and other verified business processes

 
> [!IMPORTANT]
> **Read all** documents in this repo before doing anything!
> 
> Don't forget to star ⭐ this repository
> - Always update your repo following the original repo to get the latest update + bug fixes; I will not support anything if your repo is outdated
> - If you face errors when using GitHub Actions, please refer to this [Docs/Debug.md](Docs/Debug.md)
> - **Do not** enter your information such as email and password into 2 workflows file ( `daily.yml` and `manual.yml` ) because it will not work and may leak your information to everyone
> - (*): Do not fork this repo if one of these or all of these ( not CodeQL and CL ) GitHub Actions status badge show failing, and wait until one of these or two of these show passing then you can fork again
> - `Daily claim` workflows always run every 14:00 UTC + 0; if you want to change it, refer to [this](https://github.com/gorouflex/HoneygainPot#how-to-change-the-schedule-to-fit-with-my-timezone-before-the-pot-is-reset)
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Feature 

- Claim Honeygain’s lucky pot and achievement rewards every day with GitHub Actions 🔥
- Checking your current balance 💵

# Usage 

## Use JWT Token

  1. Go to your Honeygain Dashboard or click [here](https://dashboard.honeygain.com/) and log in to your Honeygain account
  2. Open the browser's console by pressing `F12` button ( or `Fn+F12` on some laptops )
  3. Click on the tab `Application` than click to `Local storage` and click to `https://dashboard.honeygain.com`; then you will see key `JWT` that includes your token, copy this for next steps
  4. [Fork this repository 🍴](https://github.com/gorouflex/HoneygainPot/fork)
  5. Go to your forked repository 🍴
  6. Go to `Settings > Secrets and Variables > Actions`, and click `New Repository secret`
  7. Use `JWT_TOKEN` and paste your JWT Token from Steps 3
  8. Go to [`.github/workflows/daily.yml`](https://github.com/gorouflex/HoneygainPot/blob/main/.github/workflows/daily.yml) and [`.github/workflows/manual.yml`](https://github.com/gorouflex/HoneygainPot/blob/main/.github/workflows/manual.yml) and set `IsJWT` to 1 like this `IsJWT: 1`
  9. Go to your forked repository 🍴 and go to the Actions tab and press `I understand my workflows, go ahead and enable them`

<p align="left">
  <img src="Img/get_token.png">
  <img src="Img/GitSettings-Token.png">
  <img src="Img/IsJWT(1).png">
</p>

## Use Mail and Password

  1. [Fork this repository 🍴](https://github.com/gorouflex/HoneygainPot/fork)
  2. Go to your forked repository 🍴
  3. Go to `Settings > Secrets and Variables > Actions`, and click `New Repository secret`
  4. For the secret name, use `MAIL` and set your Honeygain mail and `PASS` for your password
  5. Go to [`.github/workflows/daily.yml`](https://github.com/gorouflex/HoneygainPot/blob/main/.github/workflows/daily.yml) and [`.github/workflows/manual.yml`](https://github.com/gorouflex/HoneygainPot/blob/main/.github/workflows/manual.yml) and set `IsJWT` to 0 like this `IsJWT: 0`
  6. Go to your forked repository 🍴 and go to the Actions tab and press `I understand my workflows, go ahead and enable them`

<p align="left">
  <img src="Img/GitSettings.png">
  <img src="Img/IsJWT(0).png">
</p>


## How to change the schedule to fit with my timezone before the pot is reset?

> [!IMPORTANT]
Daily workflow file path ( default is 14:00 UTC ± 0, and **DO NOT** enter your email and password here cause it will **not work** and may leak your information to everyone ): `.github/workflows/daily.yml`

- Well, GitHub uses UTC time ( UTC ± 0 ) for scheduling workflows, so we should convert it to our timezone

- For example: If I want to set the daily trigger to trigger at 9:00 PM ( UTC + 7 ) , I have to set it to 2:00 PM or 14:00 ( 24-hour format ) ( UTC ± 0 ) ( 2+7=9 ):

```
name: Daily claim
on:
  schedule:
    - cron: '0 14 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes ) and use 24-hour format
```
- So, if I want the daily trigger to run at 5:00 AM ( UTC + 7 ), I have to set it to 10:00 PM ( UTC ± 0 ) ( use 24-hour format ):

```
name: Daily claim
on:
  schedule:
    - cron: '0 22 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes ) and use 24-hour format
```

> [!NOTE]
> GitHub Actions schedules can sometimes be delayed by up to 15 minutes due to high demand, so don’t worry! ⏱️

# Preview

<p align="left">
  <img src="Img/preview.png">
  <img src="Img/preview-1.png">
</p>

# Disclaimer

> [!WARNING]
> This project is licensed under the [MIT License](https://mit-license.org/)
>
> For more information, see the [LICENSE file](./LICENSE)
> - This script is **not** affiliated with or endorsed by Honeygain. Use it at your **own risk** and responsibility.  
> - The **author** is **not responsible** for any consequences that may arise from using this script. If Honeygain wants me 
to delete this bot, I'll do it.

### Special thanks to 💖
- [MrLolf](https://github.com/MrLoLf/) x [HoneygainAutoClaim](https://github.com/MrLoLf/HoneygainAutoClaim) for based code
- [rfoal](https://github.com/rfoel/) x [duolingo](https://github.com/rfoel/duolingo) for the idea
