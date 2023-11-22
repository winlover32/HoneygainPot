<h1 align="center">Honeygain Pot</h1>
<h4 align="center">🐝Un bot qui réclame le Honeygain pot chaque jour🍯</h4>
<h4 align="center">Propulsé par GitHub Actions et Python</h4>
<p align="center">
<img src="https://img.shields.io/github/forks/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/stars/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/contributors/gorouflex/HoneygainPot?style=flat">
<p align="center">
<img alt="CodeQL status" src="https://github.com/gorouflex/HoneygainPot/actions/workflows/codeql.yml/badge.svg">
<img alt="Daily trigger status" src="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml/badge.svg">
<img alt="Manual trigger status" src="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml/badge.svg"> (*)
<p align="center">
  <a href="https://github.com/gorouflex/HoneygainPot/">English 🇺🇸</a>
  •
  <a href="README-vn.md">Tiếng Việt 🇻🇳</a>
  •
  <a href="README-fr.md">Français 🇫🇷</a>
  •
  <a href="README-de.md">Deutsch 🇩🇪</a>
<p align="center">
  <a href="Debug.md">Débogage</a>     
  •
  <a href="#fonctionnalités">Fonctionnalités</a>
  •
  <a href="#utilisation">Utilisation</a>    
  •
  <a href="#aperçu">Aperçu</a>
</p>
 <p align="left">
   
<img src="Img/Logo.png"               
     width="170" 
     height="170"></p>
    
> [!NOTE]
> English: This is not a 100% accurate translation for French
> - Mettez toujours à jour votre repo en suivant le repo original pour obtenir les dernières mises à jour + corrections de bugs, je ne prendrai pas en charge quoi que ce soit si votre repo est obsolète.
> - Si vous rencontrez des erreurs lors de l'utilisation de GitHub Actions, veuillez vous référer à cette [section de débogage](Debug.md)
> - (*): Ne pas fork ce repo si deux de ces (pas seulement 1) badges de statut GitHub Actions montrent un échec, et attendez jusqu'à ce que 1 de ceux-ci ou deux de ceux-ci montrent un succès, puis vous pouvez fork à nouveau
> - Les workflows de `Daily claim` exécutent toujours à 14:00 UTC +0, si vous voulez le changer, référez-vous à [ceci](https://github.com/gorouflex/HoneygainPot/blob/main/README-fr.md#comment-changer-lhoraire-pour-correspondre-%C3%A0-mon-fuseau-horaire-avant-la-r%C3%A9initialisation-du-pot-)
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Fonctionnalités

- Réclamez le Honeygain pot et les récompenses des réalisations tous les jours avec GitHub Actions 🔥
- Vérification de votre solde actuel

# Utilisation

  1. [Faites un fork de ce dépôt](https://github.com/gorouflex/HoneygainPot/fork)
  2. Accédez à votre dépôt forké
  3. Allez dans `Settings > Secrets and Variables > Actions`, et cliquez sur le bouton `New Repository secret`
  4. Pour le nom secret, utilisez `MAIL_JWD` pour définir votre mail Honeygain et `PASS_JWD` pour votre mot de passe
  5. Accédez à votre dépôt forké et allez dans l'onglet Actions, puis appuyez sur le bouton `I understand my workflows, go ahead and enable them`

![GitSettings](https://github.com/gorouflex/HoneygainPot/assets/98001973/d8d33621-5717-488d-9a80-6db395c8ac9d)

## Comment changer l'horaire pour correspondre à mon fuseau horaire avant la réinitialisation du pot ?

> [!IMPORTANT]
Chemin du fichier des workflows quotidiens (par défaut à 14:00 UTC +0) : `.github/workflows/daily.yml`

Eh bien, GitHub utilise l'heure UTC (UTC +0) pour planifier les workflows, donc nous devrions la convertir à notre fuseau horaire.

Par exemple : Si je veux définir le déclencheur quotidien pour se déclencher à 21:00 (UTC +7), je dois le définir à 14:00 (format 24 heures) (UTC±0) (2+7=9).
```
name: Daily claim
on:
  schedule:
    - cron: '0 14 * * *' # <- UTC Time, replace 0 14
```

Ainsi, si je veux que le déclencheur quotidien s'exécute à 5:00 (UTC +7), je dois le définir à 22:00 (UTC±0) (utilisez le format 24 heures) :
```
name: Daily claim
on:
  schedule:
    - cron: '0 22 * * *' # UTC Time
```


> [!NOTE]
> Les horaires des déclencheurs GitHub Actions peuvent parfois être retardés de jusqu'à 15 minutes en raison d'une forte demande, donc ne vous inquiétez pas !

# Aperçu

<p align="center">
  <img src="Img/preview (1).jpeg">
  <img src="Img/preview.jpeg">
</p>

## Remerciements
- [MrLolf](https://github.com/MrLoLf/) pour [HoneygainAutoClaim](https://github.com/MrLoLf/HoneygainAutoClaim)
- [rfoal](https://github.com/rfoel/) x [duolingo](https://github.com/rfoel/duolingo) pour l'idée
