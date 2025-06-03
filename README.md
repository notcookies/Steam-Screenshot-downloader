# Steam Screenshot Downloader - Version V1.0 Notes
Release: https://github.com/notcookies/Steam-Screenshot-downloader/releases/tag/V1.0

Please refer to “How to use it.pdf” for the user manual.

+------------------------------+------------------------------+------------------------------+

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

![exe步骤10](https://github.com/user-attachments/assets/065e1a76-b09a-4fb4-9eec-9a40edbc8195)

![exe步骤8](https://github.com/user-attachments/assets/c8cf942d-5230-445b-93c0-ae929119c882)

![exe步骤9](https://github.com/user-attachments/assets/26eda762-9423-41a7-acbe-aeeea9cfb39e)
