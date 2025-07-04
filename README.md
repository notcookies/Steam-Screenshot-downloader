# 👉 See How to use it.md for detailed usage.
![演示](https://github.com/user-attachments/assets/dc242466-d25e-40fc-bc74-0bd6b39f2358)
Quick Guide:

1. Extract the release, open chrome.exe in the chrome folder, log in to Steam, and check if you can open your screenshot detail page, e.g.:
https://steamcommunity.com/sharedfiles/filedetails/?id=3353482389


2. Enter your SteamID. For example, visit your profile:
https://steamcommunity.com/id/lgsgdsb233/


3. Select the folder to save downloaded screenshots.


4. Select the Chrome for Testing user data folder, usually:
C:\Users\YourUsername\AppData\Local\Google\Chrome for Testing\User Data


5. Enter the start and end page numbers, then start downloading.

# Video
v2.0 full Operation:
https://youtu.be/osDHMGYYfiA

v2.1:
https://youtu.be/xo8fKS03YXo


# For user：

dist/

├── Steam Screenshot Download V2.1.exe

├── chrome/

│   ├── chrome.exe

│   └── chromedriver.exe

**Don't worry, the rar package inside the release already contains everything.**


# Steam Screenshot Downloader

1. **Uses Official Chrome for Testing and ChromeDriver**  
   Utilizes the official Chrome for Testing and matching ChromeDriver for web automation, ensuring compatibility and stability.

2. **Supports All Screenshot Categories**  
   After logging into Steam, the tool can download all screenshots, including *Public*, *Friends Only*, and *Private*, with no restrictions.“You can see it，you can download it.”

3. **Default Download Strategy**  
   - steamcommunity.com/id/**{steam_id}**/screenshots/?p={**page**}&sort=**oldestfirst**&browsefilter=myfiles&view=**grid**&**privacy=30**
   - Downloads **all** available screenshots  
   - Uses **Grid View** mode
   - Starts from **Page 1**, downloading from the **oldest** screenshots first  

4. **File Naming Convention**  
   Downloaded images are named using the **Steam app ID + upload timestamp**, fully consistent with how the Steam client names them. This makes organizing and archiving easier.

5. **Simple Graphical User Interface (GUI)**  
   A basic GUI is provided for users to select the download path, define the page range, and configure the Chrome user data directory.

6. **Multithreaded Support with High Download Speed**  
   The latest version now supports true multithreaded downloading, significantly improving speed. A retry mechanism is included for failed downloads, and automatic Steam cookie retrieval ensures smooth operation.

# Disclaimer:
In theory, this works just like logging into Steam in Chrome.

If you're worried about security, feel free to **replace the included chromedriver and Chrome for Testing in the release** with your own from official sources.

The .exe is packed using Python tools directly from the source code — I’ve verified it.

For extra peace of mind, **change your Steam password after downloading**.



# 快速指导：
1.解压release，打开chrome文件夹内的chrome.exe，登陆steam，确认一下能否打开自己的截图详情页，例如：https://steamcommunity.com/sharedfiles/filedetails/?id=3353482389

2.输入你的steamID, 例如打开你的个人资料：https://steamcommunity.com/id/lgsgdsb233/

3.选择截图下载的文件夹

4.选择chrome for testing的userdata，通常为：C:\Users\YourUsername\AppData\Local\Google\Chrome for Testing\User Data

5.输入起止页，开始下载


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







