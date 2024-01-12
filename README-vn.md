<p align="center">
<img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/Banner.png">
</p>
<h1 align="center">HoneygainPot - Dự án Sandy</h1>
<h4 align="center">🐝 Tự động nhận Honeygain lucky pot của bạn mỗi ngày🍯 </h4>
<h4 align="center">Dưới sự hỗ trợ của GitHub Actions 🐙 và Python 🐍</h4>
<p align="center">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/forks/gorouflex/HoneygainPot?style=flat">
<p align="center">
<img src="https://img.shields.io/github/stars/gorouflex/HoneygainPot?style=flat">
<img alt="GitHub watchers" src="https://img.shields.io/github/watchers/gorouflex/HoneygainPot?style=flat">
<img src="https://img.shields.io/github/contributors/gorouflex/HoneygainPot?style=flat">
</p>
<p align="center">
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/codeql.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/codeql.yml/badge.svg"></a>
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/cl.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/cl.yml/badge.svg"></a>
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/daily.yml/badge.svg"></a>
</p>
<p align="center">
<a href="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml"><img src="https://github.com/gorouflex/HoneygainPot/actions/workflows/manual.yml/badge.svg"></a> (*)
</p>
<p align="center">
  <a href="https://github.com/gorouflex/HoneygainPot/">English 🇺🇸</a>
  •
  <a href="README-vn.md">Tiếng Việt 🇻🇳</a>
<p align="center">
  <a href="https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug-vn.md">Sửa các lỗi thường gặp</a>
  •
  <a href="https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/FAQ-vn.md">FAQ</a>  
  •
  <a href="#tính-năng">Tính năng</a>
  •
  <a href="#cách-sử-dụng">Cách sử dụng</a>
  •
  <a href="#config">Config</a>     
  •
  <a href="#xem-trước">Xem trước</a>
  •
  <a href="#trách-nhiệm">Trách nhiệm</a>  
</p>

  ### [Honeygain](https://r.honeygain.me/BADBO762DE)  là một nền tảng trực tuyến sử dụng các thiết bị mạng của bạn như một cánh cổng để giúp các nhà doanh nghiệp hay các nhà phân tích dữ liệu để thực hiện các chiến dịch SEO, nghiên cứu thị trường, bảo vệ thương hiệu....

### Thuộc chuỗi dự án Sandy

- [Sandy](https://github.com/gorouflex/Sandy/) ( Official Documents and Information Repository for Project Sandy )
- [HoneygainPot](https://github.com/gorouflex/HoneygainPot/) ( 🐝 Automatically claim your Honeygain lucky pot every day 🍯 )
- [DuoXPy](https://github.com/gorouflex/DuoXPy/) ( ⚡️ XP farm and Streak keeper for Duolingo 🔥 )

> [!IMPORTANT]
> **Vui lòng đọc hết tất cả** tài liệu và văn bản hướng dẫn trong repo này trước khi làm!
> 
> Đừng quên cho repo của mình 1 star nhé ⭐ 
> - Luôn cập nhật repo của các bạn theo repo gốc này để nhận được những bản cập nhật và vá lỗi mới nhất, và tôi GorouFlex sẽ không hỗ trợ nếu phát hiện repo của bạn đã lỗi thời và không được cập nhật theo repo chính.
> - Nếu bạn gặp lỗi khi sử dụng GitHub Actions, hãy kham khảo lỗi tại [Sandy/Docs/HoneygainPot/Debug-vn.md](https://github.com/gorouflex/Sandy/blob/main/Docs/HoneygainPot/Debug-vn.md).
> - **Vui lòng không** nhập thông tin tài khoản của bạn vào 2 file workflow ( `daily.yml` và `manual.yml`)  vì nó sẽ không hoạt động mà sẽ gây ra lỗi và còn có thể bị lộ thông tin cho người khác xem
> - (*) Không được fork repo nếu bạn thấy cả 1 trong 2 ( không bao gồm cả CodeQL và CL ) trạng thái của GitHub Actions đều chuyển sang đỏ, hãy chờ cho đến khi 1 trong 2 hoặc cả 2 chuyển sang màu xanh thì có thể fork
> - `Daily claim` sẽ luôn luôn tự động chạy vào lúc 14:00 giờ ( UTC + 0 ) tức là 9:00 tối theo giờ UTC +7, nếu muốn chỉnh thì tham khảo tại [đây](https://github.com/gorouflex/HoneygainPot/blob/main/README-vn.md#l%C3%A0m-th%E1%BA%BF-n%C3%A0o-%C4%91%E1%BB%83-ch%E1%BB%89nh-l%E1%BA%A1i-th%E1%BB%9Di-gian-t%E1%BB%B1-%C4%91%E1%BB%99ng-ch%E1%BA%A1y-m%E1%BB%97i-ng%C3%A0y).
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Tính năng

- Giúp bạn nhận lucky pot và thưởng thành tựu của Honeygain mỗi ngày mà không cần treo máy với sự hỗ trợ của GitHub Actions, tăng thêm thu nhập cho bạn 🔥
- Kiểm tra được số dư tài khoản Honeygain của bạn 💵

# Cách sử dụng

## Sử dụng Token

  1. Đến Honeygain Dashboard của bạn hoặc nhấn [vào đây](https://dashboard.honeygain.com/) và đăng nhập tài khoản Honeygain của bạn vào
  2. Sau khi đã đăng nhập mở công cụ cho lập trình viên của trình duyệt bằng cách ấn nút `F12` ( hoặc `Fn+F12` trên laptop )
  3. Ấn vào tab  `Application` trên thanh công cụ rồi ấn vào danh sách `Local storage` rồi click vào `https://dashboard.honeygain.com` sau đó bạn sẽ thấy được 1 cái key tên là `JWT` và đó là nơi chứa token của bạn, copy token rồi để dành cho những bước sau
  4. [Fork repo này 🍴](https://github.com/gorouflex/HoneygainPot/fork)  
  5. Đến repo mà bạn đã fork🍴
  6. Vào `Settings > Secrets and Variables > Actions`, và ấn nút `New Repository secret`
  7. Tạo 1 secrets tên `JWT_TOKEN` rồi dán Token mà bạn đã làm ở bước 3, tạo thêm 1 secrets tên `IsJWT` rồi đặt thành `true`
  8. Trở lại repo của bạn đã fork 🍴, vào Actions trên thanh công cụ repo rồi ấn `I understand my workflows, go ahead and enable them`

<p align="left">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/get_token.png">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/GitSettings-Token.png">
</p>

## Sử dụng Mail và Pass

  1. [Fork repo này 🍴](https://github.com/gorouflex/HoneygainPot/fork)  
  2. Đến repo mà bạn đã fork🍴
  3. Vào `Settings > Secrets and Variables > Actions`, và ấn nút `New Repository secret`
  4. Đặt tên secrets đầu tiên tên là `MAIL` và điền mail Honeygain của bạn vào, sau đó tạo thêm secrets thứ 2 tên là `PASS` rồi nhập pass của bạn vào, tạo thêm secrects thứ 3 tên `IsJWT` rồi đặt thành `false`
  5. Trở lại repo của bạn đã fork 🍴, vào Actions trên thanh công cụ repo rồi ấn `I understand my workflows, go ahead and enable them`

<p align="left">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/GitSettings.png">
</p>

# Config

- Thông thường bạn có tìm thấy thư mục config ở cùng nơi mà file `main.py` ở. Nhưng 1 số trường hợp đặc biệc thì bạn cần phải tự tìm file config thông quan cửa sổ thông tin khi chạy của file `main.py`
- Bạn có đổi thông tin tài khoản ở file config, nhưng chắc chắn rằng `IsJWT` ở file config được đặt về `0` nếu bạn đang sử dụng email,mật khẩu và đặt thành `1` nếu bạn sử dụng jwt token hoặc sử dụng file `ConfigR&W.py` ở trong repo của tôi

## Làm thế nào để chỉnh lại thời gian tự động chạy mỗi ngày?

> [!IMPORTANT]
File tự động chạy mỗi ngày ở ( mặc định là 14:00 UTC ± 0, và vui lòng **không** nhập email tài khoản và mật khẩu của bạn vào vì nó sẽ không hoạt động dẫn đến lỗi và còn có thể bị lộ thông tim cho người bên ngoài ): `.github/workflows/daily.yml`

- GitHub sử dụng giờ UTC quốc tế ( UTC ± 0 ) để đặt lịch trình chạy GitHub Actions, nên chúng ta phải đổi sang múi giờ của mình

- Ví dụ: Nếu tôi muốn đặt lịch để cho GitHub Actions chạy vào lúc 9:00 tối ( múi giờ UTC + 7 ) thì tôi phải chuyển thành là 2 giờ chiều theo múi giờ UTC ± 0, vì 2+7 là 9!
Lưu ý là phải sử dụng định dạng 24 giờ để đặt lịch: 

```
name: Daily claim
on:
  schedule:
    - cron: '0 14 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes) and use 24-hour format
```

- Nên nếu tôi muốn đặt vào lúc 5h sáng theo giờ UTC +7 thì tôi phải đặt thành 10h tối theo giờ UTC +0, và phải sử dụng định dạng 24 giờ:

```
name: Daily claim
on:
  schedule:
    - cron: '0 22 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes) and use 24-hour format
```

> [!NOTE]
> GitHub Actions có thể bị delay hơn so với giờ dự kiến đã đặt khoảng từ 3p đến 15p vì do nhu cầu chạy đang cao nên đừng lo lắng vì sao nó không chạy đúng giờ nhé!⏱️

# Xem trước

<p align="center">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/preview.png">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/HoneygainPot/preview-1.png">
</p>

# Trách nhiệm

> [!WARNING]
> Dự án này được bảo hộ dưới giấy phép [MIT License](https://mit-license.org/)
> 
> Thông tin chi tiết ,vui lòng xem [file LICENSE](/LICENSE)
> - Script/Bot này **KHÔNG** có liên kết hay được xác nhận bởi Honeygain
> - **Tôi GorouFlex và MrLolf** **không có trách nhiệm** cho bất kỳ hậu quả mà có thể phát sinh trong quá trình dùng Script/Bot này
> - Nếu Honeygain muốn chúng tôi xoá con bot này thì chúng tôi sẽ làm

## Recent activity [![Time period](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_badge.svg)](https://repography.com)
[![Timeline graph](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_timeline.svg)](https://github.com/gorouflex/HoneygainPot/commits)
[![Issue status graph](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_issues.svg)](https://github.com/gorouflex/HoneygainPot/issues)
[![Pull request status graph](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_prs.svg)](https://github.com/gorouflex/HoneygainPot/pulls)
[![Trending topics](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_words.svg)](https://github.com/gorouflex/HoneygainPot/commits)
[![Top contributors](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_users.svg)](https://github.com/gorouflex/HoneygainPot/graphs/contributors)
[![Activity map](https://images.repography.com/44739709/gorouflex/HoneygainPot/recent-activity/tXCw9M5i0HgQ3S3BsxKFTCsKpg43C6MCG6gN6bnFCTc/fRHoqaVaReVH-CrjejSHavn1gHM4SFsKAtm_P7QJivk_map.svg)](https://github.com/gorouflex/HoneygainPot/commits)

### Đặt biệt cảm ơn 💖
- [MrLolf](https://github.com/MrLoLf/) x [HoneygainAutoClaim](https://github.com/MrLoLf/HoneygainAutoClaim) cho mã nguồn mở
- [rfoal](https://github.com/rfoel/) x [duolingo](https://github.com/rfoel/duolingo) cho ý tưởng
