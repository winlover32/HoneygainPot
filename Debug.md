<h1 align="center">Debug</h1>

> [!NOTE]
> Error code list:
> <p align="left">
> <a href="#error-code-1">1 </a>
> <a href="#error-code-2">2 </a>
> <a href="#error-code-2">3 </a>
> <a href="#error-code-4">4 </a>
> <a href="#error-code-10">10 </a>
> </p>
# How to get debug logs?
1. Go Actions tab
2. Click to the failure task
3. Then click to `Manual` or `Daily` tab then click to the `Run HoneygainPot` section, you will see the debug logs

<p align="left">
  <img src="Img/step-1.png">
</p>
<p align="center">
  <img src="Img/step-2.png">
</p>
<p align="center">
  <img src="Img/step-3.png">
</p>
<p align="left">
  <img src="Img/step-4.png">
</p>
  
## GitHub Actions

### Error code 1

```
❌ Error code 1: Cannot find 'MAIL_JWD' and 'PASS_JWD'
```

or

```
Logging in to Honeygain!
Traceback (most recent call last):
  File "/home/runner/work/HoneygainPot/HoneygainPot/main.py", line 280, in <module>
    main()
  File "/home/runner/work/HoneygainPot/HoneygainPot/main.py", line 243, in main
    if not achievements_claim(s):
  File "/home/runner/work/HoneygainPot/HoneygainPot/main.py", line 199, in achievements_claim
    achievements: dict = achievements.json()
  File "/usr/lib/python3/dist-packages/requests/models.py", line 900, in json
    return complexjson.loads(self.text, **kwargs)
  File "/usr/lib/python3.10/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.10/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.10/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
Error: Process completed with exit code 1.

```

> [!TIP]
> This means you did not set `MAIL_JWD` and `PASS_JWD` secrets in the GitHub repo settings

### Error code 2

```
❌ Error code 2: You are not eligible to get the lucky pot
```

or

```
Claimed None.
Traceback (most recent call last):
  File "/home/runner/work/HoneygainPot/HoneygainPot/main.py", line 281, in <module>
    main()
  File "/home/runner/work/HoneygainPot/HoneygainPot/main.py", line 263, in main
    print(f'Claimed {pot_claim["data"]["credits"]} Credits.')
KeyError: 'data'

```

> [!TIP]
> You are not eligible to get the lucky pot if you do not reach 15mb of sharing

### Error code 3

```
❌ Error code 3: Cannot receive any input, make sure 'IsGit' = 1
```

or


```
Generating new Config!
Traceback (most recent call last):
  File "/home/runner/work/HoneygainAutoClaim/HoneygainAutoClaim/main.py", line 113, in <module>
    create_config()
  File "/home/runner/work/HoneygainAutoClaim/HoneygainAutoClaim/main.py", line 40, in create_config
    email: str = input("Email: ")
EOFError: EOF when reading a line
Email: 

```

> [!TIP]
> This is because GitHub Actions is basically a non-input console, so the code cannot receive the input, make sure that `IsGit` is set to 1 in the workflows file `daily.yml`


### Error code 4

```
❌ Error code 4: Wrong login credentials,please enter the right ones
```

> [!TIP]
> Check your credenrials again

### Error code 10

```
❌ Error code 10: You have exceeded your login tries.\nPlease wait a few hours or return tomorrow
```

> [!TIP]
> Ask for GitHub
