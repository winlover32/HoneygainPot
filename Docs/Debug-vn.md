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
> <a href="#error-code-3">3 </a>
> <a href="#error-code-4">4 </a>
> </p>
# Làm thế nào để lấy mã lỗi/nhật ký báo lỗi?
1. Vào tab Actions trên repo đã fork của bạn
2. Chọn tiến trình chạy bị lỗi
3. Chọn tab `Manual` hoặc `Daily` rồi chọn tab `Run HoneygainPot` bạn sẽ thấy mã lỗi/nhật ký báo lỗi

<p align="left">
  <img src="/Img/step-1.png">
</p>
<p align="center">
  <img src="/Img/step-2.png">
</p>
<p align="center">
  <img src="/Img/step-3.png">
</p>
<p align="left">
  <img src="/Img/step-4.png">
</p>
  
## GitHub Actions

### Error code 1

```
❌ Error code 1: You are not eligible to get the lucky pot because you do not reach 15mb of sharing bandwich everyday ( following to Honeygain's TOS )
```

> [!TIP]
> Bạn chưa đủ điều kiện chia sẻ đủ 15mb băng thông mỗi ngày ( theo chính sách của Honeygain ) để nhận được lucky pot, hãy để cho máy farm đến khi đủ 15mb băng thông!


### Error code 2

```
❌ Error code 2: Wrong login credentials,please enter the right ones
```

> [!TIP]
> Kiểm tra lại thông tin tài khoản lại


### Error code 3

```
❌ Error code 3: Cannot receive any input, make sure 'IsGit' = 1
```

> [!TIP]
> Hỏi GitHub đi, lỗi này tôi bó tay

### Error code 4

```
❌ Error code 4: Failed to fetch commit information
```

> [!TIP]
> Do trong quá trình lấy SHA của commit có xảy ra vấn đề, hãy liên hệ với tôi nếu nó xuất hiện