| 📦 Release Information & Download Count. | ❤️ Sponsor —— I'd love a $1 coffee if you feel like it.☕~~ |
|----------------------------------|--------------------------------|
| [![GitHub release (latest by date)](https://img.shields.io/github/v/release/notcookies/Steam-Screenshot-downloader)](https://github.com/notcookies/Steam-Screenshot-downloader/releases)<br>[![GitHub All Releases](https://img.shields.io/github/downloads/notcookies/Steam-Screenshot-downloader/total.svg)](https://github.com/notcookies/Steam-Screenshot-downloader/releases) | [![PayPal](https://img.shields.io/badge/PayPal-0070ba?logo=paypal&logoColor=white&style=flat)](https://paypal.me/dongyunboshi)<br>[<img src="assets/Alipay.jpg" alt="Alipay" width="15"/>](https://github.com/notcookies/Steam-Screenshot-downloader/blob/main/assets/Alipay.jpg) [<img src="assets/WeChat_Pay.jpg" alt="WeChat" width="15"/>](https://github.com/notcookies/Steam-Screenshot-downloader/blob/main/assets/WeChat_Pay.jpg) |

## 🎉 Special Thanks to Sponsors 
Huge thanks to the following supporters! (Listed by date)

| Name   | Message | Date  |
|-------------|----------------|-------------|
| **Myself**   | Keep it up! ☕  | 2025-07-11  |

## 🌟 User Reviews

| # | User Review |
|--|-------------|
| 1 | Just used the updated version you provided. And everything works Fantastic!<br>It was able to download all of the screenshots.<br>The way you explained everything in detail was nice.<br>Thank you for looking into it man!<br>**Amazing tool** |
| 2 | Yea man. Thank you so much<br>This makes saving screenshots way easier.<br>Compared to the one made by *ScienceDiscoverer*, this one is **waaay faster** thanks to multithreading.<br>Works perfectly 👍 |
| 3 | Looks fixed, tried with 2 different accounts and worked, thanks! |
| 4 | 好的我试一下<br>可以了！<br>路由模式可以下载了！<br>**up真的厉害**，这截图工具解决了大问题，手动一个一个保存下来估计要到明年啦<br>已点亮收藏 ⭐ |
| 5 | I was searching for hours and hours to find a good screenshot downloader and I randomly found this video in YouTube.<br>This one is by far **the best one**, keep up the good work, I managed to download **12k screenshots**.<br>The guide was clear and easy to understand. Thank you! |
| 6 | ....（Looking forward to your use and feedback.） |


# Steam Screenshot Downloader



![image](https://github.com/user-attachments/assets/1ffbb150-2ded-4ff1-82be-767f9e1a5275)

#  Video base_v2.5
https://www.youtube.com/watch?v=1G6fnU91s2w&t=80s

#  Video base_v2.3
https://youtu.be/9wv2S5nMiGk

https://www.bilibili.com/video/BV1bE3rzrEjY/

![image](https://github.com/user-attachments/assets/7a8461b4-a56e-4e92-91e0-c9b706edf9a0)

# The common scenarios:

1. Unable to locate the Steam profile.If you haven't customized your Steam profile URL, your profile and screenshot pages will start with https://steamcommunity.com/your_steam_ID. However, if you've customized your URL, the prefix will include /id/, such as https://steamcommunity.com/id/lgsgdsb233/.
This software uses the latter format by default, so you may need to customize your URL accordingly.

2. The popped-up Chrome for Testing cannot display the grid view with 50 screenshots.In this case, you need to manually log in to Steam before using this software. After logging in, try randomly opening a few screenshot detail pages—this will also help ensure that the software can retrieve Steam cookies successfully.

# Quick Guide:

1. Extract the release, open chrome.exe in the chrome folder, log in to Steam, and check if you can open your screenshot detail page, e.g.:
https://steamcommunity.com/sharedfiles/filedetails/?id=3353482389


2. Enter your SteamID. For example, visit your profile:
https://steamcommunity.com **/id/** lgsgdsb233/


3. Select the folder to save downloaded screenshots.


4. Select the Chrome for Testing user data folder, usually:
C:\Users\YourUsername\AppData\Local\Google\Chrome for Testing\User Data


5. Enter the start and end page numbers, then start downloading.

# Disclaimer:
1. In theory, this works just like logging into Steam in Chrome.If you're worried about security, feel free to **replace the included chromedriver and Chrome for Testing in the release** with your own from official sources.

2. The .exe is packed using Python tools directly from the source code — I’ve verified it.

3. For extra peace of mind, **change your Steam password after downloading**.

# How it works?

1. **Uses Official Chrome for Testing and Chrome Driver**  
   Utilizes the official Chrome for Testing and matching Chrome Driver for web automation, ensuring compatibility and stability.

2. **Supports All Screenshot Categories**  
   After logging into Steam, the tool can download all screenshots, including *Public*, *Friends Only*, and *Private*, with no restrictions.“You can see it，you can download it.”

3. **Default Download Strategy**  
   - steamcommunity.com/id/**{steam_id}**/screenshots/?p={**page**}&sort=**oldestfirst**&browsefilter=myfiles&view=**grid**&**privacy=30**.
   - Downloads **all** available screenshots.
   - Uses **Grid View** mode.
   - Downloading from the **oldest** screenshots first. 

4. **File Naming Convention**  
   Downloaded images are named using the **Steam app ID + upload timestamp**, fully consistent with how the Steam client names them.

5. **Multithreaded Support with High Download Speed**  
   Starting from version 2.0, the software supports true multithreaded downloading.

# License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file for details.

# 快速指导：
1.解压release，打开chrome文件夹内的chrome.exe，登陆steam，确认一下能否打开自己的截图详情页，例如：https://steamcommunity.com/sharedfiles/filedetails/?id=3353482389

2.输入你的steamID, 例如打开你的个人资料：https://steamcommunity.com/id/lgsgdsb233/

3.选择截图下载的文件夹

4.选择chrome for testing的userdata，通常为：C:\Users\YourUsername\AppData\Local\Google\Chrome for Testing\User Data

5.输入起止页，开始下载

6.如果是UU加速器，选**路由模式**

![c1f87dc7c0abd5677ad5894b995a06b](https://github.com/user-attachments/assets/7939cc37-ad17-4b82-9d11-3e57cce70c69)

![e814547f02950d3bdad1a3f93e2a6ea](https://github.com/user-attachments/assets/8da9b34a-5dc6-4e4a-a652-350a299b7165)


# 软件特色：
1.下载原始分辨率截图

2.下载次序有依可循

3.不需要手动输入steam cookies

4.下载截图时间为原始F12时的时间

5.生成缩略图，文件夹以及命名保持和steam客户端一致

6.私密、仅好友、成人内容、非steam游戏截图，我能看到它，就能下载它


# 软件大致逻辑：
1.利用chromedriver获取截图地址和steam cookies

2.根据网格视图、最早文件优先的规则下载每页的50张截图

3.从steam云返回的Content-Disposition为每张截图命名并修改Windows文件时间戳

4.文件夹、缩略图、命名规章完全符合steam 客户端


# 声明：
理论上，上述流程跟你在chrome上登陆steam没有任何区别。

如果担心，你可以替换掉release内的chromedriver和chrome for testing，自行在官网下载。

exe文件可以使用python打包工具直接对源代码打包，我已经做过校验。

保险起见，截图下载完成后建议更换一次密码。


# 许可协议
本项目遵循 GNU 通用公共许可证 第3版（GPL v3.0）授权。
有关详细内容，请参阅项目中的 LICENSE 文件。





