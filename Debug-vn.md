<h1 align="center">Sửa các lỗi thường gặp</h1>
<p align="center">
  <a href="Debug.md">English 🇺🇸</a>
  •
  <a href="Debug-vn.md">Tiếng Việt 🇻🇳</a>
</p>

> [!NOTE]
> Danh sách mã lỗi:
> <p align="left">
> <a href="#error-code-1">1 </a>
> <a href="#error-code-2">2 </a>
> <a href="#error-code-2">3 </a>
> <a href="#error-code-4">4 </a>
> <a href="#error-code-10">10 </a>
> </p>
# Cách nào để có mã lỗi/nhật ký báo lỗi?
1. Vào tab Actions trên repo đã fork của bạn
2. Chọn tiến trình chạy bị lỗi
3. Chọn tab `Manual` hoặc `Daily` rồi chọn tab `Run HoneygainPot` bạn sẽ thấy mã lỗi/nhật ký báo lỗi

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

hoặc ( với phiên bản cũ hơn chưa sync với repo chính ) :

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
> Có nghĩa là bạn chưa set biến `MAIL_JWD` và `PASS_JWD` secrets ở phần cài đặt repo của bạn đã fork

### Error code 2

```
❌ Error code 2: You are not eligible to get the lucky pot because you do not reach 15mb of sharing bandwich everyday ( following to Honeygain's TOS )

```

hoặc ( với phiên bản cũ hơn chưa sync với repo chính ) :

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
> Bạn chưa đủ điều kiện chia sẻ đủ 15mb băng thông mỗi ngày (theo chính sách của Honeygain) để nhận được lucky pot, hãy để cho máy farm đến khi đủ 15mb băng thông!

### Error code 3

```
❌ Error code 3: Cannot receive any input, make sure 'IsGit' = 1
```

hoặc ( với phiên bản cũ hơn chưa sync với repo chính ) :

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
> Bản chất GitHub Actions là 1 console không thể được nhập từ bên ngoài, hãy kiểm tra `IsGit` ( ở file workflow ) đã set về 1 chưa?


### Error code 4

```
❌ Error code 4: Wrong login credentials,please enter the right ones
```

> [!TIP]
> Kiểm tra lại thông tin tài khoản lại

### Error code 10

```
❌ Error code 10: You have exceeded your login tries.\nPlease wait a few hours or return tomorrow
```

> [!TIP]
> Hỏi GitHub đi lỗi này bó tay
