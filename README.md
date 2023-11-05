<h1 align="center">Honeygain Pot</h1>
<h4 align="center">A bot that gains honeygain pot every day</h4>
<h4 align="center">Powered by GitHub Actions and Python</h4>

<p align="center">
<img alt="Daily trigger status" src="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml/badge.svg">
<img alt="Manual trigger status" src="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml/badge.svg">
<p align="center">

  <a href="#feature">Feature</a>
  •
  <a href="#usage">Usage</a>     
</p>

# Feature
- Claims honeygain pot and achievement rewards every day
# Usage

  1. [Fork this repository](https://github.com/gorouflex/honeygainpot/fork)  
  2. Go to your forked repository
  3. Go to Settings > Secrets and Variables > Actions. And click the button `New Repository secret`
  4. For the secret name, use `MAIL_JWD` to set your honeygain mail and `PASS_JWD` for your password
  5. Go to your forked repository and go to the Actions tab and press the button `I understand my workflows, go ahead and enable them`

![GitSettings](https://github.com/gorouflex/HoneygainPot/assets/98001973/d8d33621-5717-488d-9a80-6db395c8ac9d)

## How to change the schedule to fit with my timezone before the pot is reset?

Well, GitHub uses UTC time as the workflow time scheduled so we should convert it to our timezone.

For example: If I want to set the daily trigger to trigger at 9pm (UTC +7) so I have to set it to 2pm (UTC) (2+7=9)

## Big thanks to
- [MrLolf](https://github.com/MrLoLf/) for [HoneygainAutoClaim](https://github.com/MrLoLf/HoneygainAutoClaim)
- [rfoal](https://github.com/rfoel/)-[duolingo](https://github.com/rfoel/duolingo) for idea
