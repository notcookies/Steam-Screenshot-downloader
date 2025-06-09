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

~~6. Single-Threaded with Random Delay~~  
   ~~The current version uses single-threaded downloading, which may be slower. A random delay of 1–2 seconds is added between each download to avoid triggering Steam's rate limits, ensuring stable operation without being blocked.~~

6. **Multithreaded Support with High Download Speed**  
   The latest version now supports true multithreaded downloading, significantly improving speed. A retry mechanism is included for failed downloads, and automatic Steam cookie retrieval ensures smooth operation.

+------------------------------------------+------------------------------------------+
For user：

dist/

├── Steam Screenshot Download V2.1.exe

├── chrome/

│   ├── chrome.exe

│   └── chromedriver.exe

**Don't worry, the rar package inside the release already contains everything.**

   
+------------------------------------------+------------------------------------------+
For parking：

steam_screenshot_downloader/

├── chrome/

│ ├── chrome.exe # chrome for testing

│ └── chromedriver.exe #  ChromeDriver

├── Steam Screenshot Download V2.1.py 

├── requirements.txt 

└── README.md

+------------------------------------------+------------------------------------------+


# Video
https://youtu.be/osDHMGYYfiA

