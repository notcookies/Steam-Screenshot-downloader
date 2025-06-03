# Steam Screenshot Downloader - Version V1.0 Notes
Release: https://github.com/notcookies/Steam-Screenshot-downloader/releases/tag/V1.0

1. **Uses Official Chrome for Testing and ChromeDriver**  
   Utilizes the official Chrome for Testing and matching ChromeDriver for web automation, ensuring compatibility and stability.

2. **Supports All Screenshot Categories**  
   After logging into Steam, the tool can download all screenshots, including *Public*, *Friends Only*, and *Private*, with no restrictions.“You can see it，you can download it.”

3. **Default Download Strategy**  
   - Downloads **all** available screenshots  
   - Uses **Grid View** mode  
   - Starts from **Page 1**, downloading from the **oldest** screenshots first  

4. **File Naming Convention**  
   Downloaded images are named using the **Steam app ID + upload timestamp**, fully consistent with how the Steam client names them. This makes organizing and archiving easier.

5. **Simple Graphical User Interface (GUI)**  
   A basic GUI is provided for users to select the download path, define the page range, and configure the Chrome user data directory.

6. **Single-Threaded with Random Delay**  
   The current version uses single-threaded downloading, which may be slower. A random delay of 1–2 seconds is added between each download to avoid triggering Steam's rate limits, ensuring stable operation without being blocked.

+------------------------------------------+------------------------------------------+


# How to use it?

## 1. Download

- Download and unzip the **Steam-Screenshot-Downloader**.
  
![exe步骤6](https://github.com/user-attachments/assets/8736847d-1235-4563-8057-addd09a57cd8)

## 2. Chrome Setup

- Open the `chrome` folder and run `chrome.exe` (The Chrome for Testing and ChromeDriver included in this archive were both downloaded from the official website).
 
![exe步骤7](https://github.com/user-attachments/assets/8c20cd48-3123-4a71-8e89-c01b8075a9a4)

- Log into your **Steam account** using this Chrome.

![exe步骤12](https://github.com/user-attachments/assets/13398610-da5b-4ced-a4a1-91113f91383e)

- Go to your **Profile → Screenshots**, and open any screenshot.
- Click on the screenshot again to see if the **original uploaded image** opens.
- You may need to **log in to Steam again** during this process.
- If you can open a link like:"https://steamcommunity.com/sharedfiles/filedetails/?id=3xxxxxxxx"

![exe步骤13](https://github.com/user-attachments/assets/b5402964-6d55-48ce-bed6-6cd778976192)

🎉 **Congratulations! All preparations are complete.**

> 💡 After logging in, Chrome for Testing will automatically create user data on your C drive under your user folder.  
> This authentication data is required to download the screenshots.

## 3. Run the Downloader

- Launch `Steam-Screenshot-Downloader`.

## 4. Enter Steam ID or Profile Name

- Input your **Steam ID** or **custom profile name**.
- You can find it by visiting your Steam profile, e.g.:"https://steamcommunity.com/id/lxxxxxxx233/"

## 5. Choose Save Location

- Select the folder where you want to **save the downloaded screenshots**.

## 6. Select Chrome User Data Folder

- Choose the Chrome user data folder from step 2, usually located at:"C:\Users\YourUsername\AppData\Local\Google\Chrome for Testing\User Data"

![exe步骤1](https://github.com/user-attachments/assets/83957562-2033-453c-babb-6d258731c5d3)

## 7. Set Screenshot Page Range

- Specify the **page range** you want to download.
- For a test run, try downloading pages **1 to 2**.
![exe步骤2](https://github.com/user-attachments/assets/4a8e51d8-75e6-4a3a-90d0-7ee8e159e79d)

✅ If everything is set up correctly, the program should run smoothly and download your screenshots!

![exe步骤10](https://github.com/user-attachments/assets/d5d29944-7d71-4a2a-b0c0-6380c518ba88)

![exe步骤8](https://github.com/user-attachments/assets/d33b72f8-b3ad-4779-aed9-a9cdefa4c0d3)

![exe步骤9](https://github.com/user-attachments/assets/f3f37005-92e9-403a-bc5c-8c4119299e63)






