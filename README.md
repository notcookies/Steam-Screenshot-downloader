# Steam Screenshot Downloader - Version Notes

1. **Uses Official Chrome for Testing and ChromeDriver**  
   Utilizes the official Chrome for Testing and matching ChromeDriver for web automation, ensuring compatibility and stability.

2. **Supports All Screenshot Categories**  
   After logging into Steam, the tool can download all screenshots, including *Public*, *Friends Only*, and *Private*, with no restrictions.

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
