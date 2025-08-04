## 1. Download
- Download the **Steam-Screenshot-Downloader_Linux** and **geckodriver (0.36.0)** to a folder on your Steam Deck.
- If they are not executable, please run:
```
        chmod +x Steam-Screenshot-Downloader_Linux geckodriver
```
## 2. Firefox Setup
SteamOS seems to include a **sandboxed version of Firefox**, which I couldn't invoke.
- Open Steam Deck ```Konsole``` 
- Disable SteamOS readonly mode:
```
    sudo steamos-readonly disable
```
- Edit the Pacman Config File:
```
    sudo nano /etc/pacman.conf
```
- Find the following line near the top of the file:
```
    SigLevel = Required DatabaseOptional
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modify it to:
```
    #SigLevel = Required DatabaseOptional
    SigLevel = Never
```
- Press `Ctrl + O` to save the file, then press `Enter` to confirm.
- Press `Ctrl + X` to exit the editor.
- Setup Firefox:
```
    sudo pacman -Syu firefox 
```
```
🧐Why Edit the Pacman Config File?

SteamOS  Konsole When running:
    sudo pacman -S firefox

You might see the following errors:
checking keys in keyring...
error: keyring is not writeable
error: required key missing from keyring

This happens because SteamOS uses its own package signing keys, and pacman is unable to verify the package signatures.
By default, pacman only trusts the official Arch Linux keys and does not recognize or trust SteamOS's custom keyring, so signature verification fails.

⚠️ Important: After downloading the screenshots is complete, it is strongly recommended to restore the original secure configuration.
sudo nano /etc/pacman.conf
Then change the lines back to:
SigLevel = Required DatabaseOptional
#SigLevel = Never
Save and exit again.
```

**For example：**

<img width="1285" height="925" alt="Image" src="https://github.com/user-attachments/assets/9c3df332-52b4-4f5f-b697-94824321d734" />

## 3. Test Geckodriver(optional) & Run Firefox(Required)
- check geckodriver & firefox(**optional**)
```
cd /usr/lib/firefox/
firefox --version

cd ~/your SteamDeck folder
./geckodriver --version

./geckodriver
xxxxx   geckodriver     INFO    Listening on 127.0.0.1:4444 
crtl+c (^C)

./geckodriver --binary /usr/lib/firefox/
xxxxx   geckodriver     INFO    Listening on 127.0.0.1:4444
crtl+c (^C)
```
- Run firefox(**Required**)
```
/usr/lib/firefox/firefox
```
- In Firefox settings, go to `Privacy & Security → Enhanced Tracking Protection`, and set it to `Custom` (to allow easier access to Steam cookies).
- Open the Steam homepage in Firefox and log in. Make sure you can open any screenshot from your profile, then close the browser.

**For example：**

```
[jinx@jinx ~]$ cd ~/SteamScreenshotDownloader/
[jinx@jinx SteamScreenshotDownloader]$ ./geckodriver --version
geckodriver 0.36.0 (a3d508507022 2025-02-24 15:57 +0000)

The source code of this program is available from
testing/geckodriver in https://hg.mozilla.org/mozilla-central.

This program is subject to the terms of the Mozilla Public License 2.0.
You can obtain a copy of the license at https://mozilla.org/MPL/2.0/.
[jinx@jinx SteamScreenshotDownloader]$ 
[jinx@jinx SteamScreenshotDownloader]$ 
[jinx@jinx SteamScreenshotDownloader]$ cd /usr/lib/firefox/
[jinx@jinx firefox]$ firefox --version 
Mozilla Firefox 141.0
[jinx@jinx firefox]$ 
[jinx@jinx firefox]$ 
[jinx@jinx firefox]$ cd ~/SteamScreenshotDownloader/
[jinx@jinx SteamScreenshotDownloader]$ ./geckodriver
1753845485227   geckodriver     INFO    Listening on 127.0.0.1:4444
^C
[jinx@jinx SteamScreenshotDownloader]$ ./geckodriver --binary /usr/lib/firefox/
1753845510531   geckodriver     INFO    Listening on 127.0.0.1:4444
^C
[jinx@jinx SteamScreenshotDownloader]$
```
<img width="1353" height="898" alt="Image" src="https://github.com/user-attachments/assets/7e20d14a-c4cd-4d5c-9674-928f08a0e5db" />

<img width="1488" height="922" alt="Image" src="https://github.com/user-attachments/assets/89c4bd31-f2e4-42d2-81ac-5fc1d824cafe" />

## 4. Enjoy the Tool and Start Downloading Your Screenshots

<img width="1354" height="903" alt="Image" src="https://github.com/user-attachments/assets/9fe89e5c-9d70-4214-a681-fa6fe54ca9bd" />


![c9b72404fe335041408f5d96c197f74](https://github.com/user-attachments/assets/35699f1c-618d-4be8-a52e-988eaa3d1169)


<img width="1280" height="800" alt="Screenshot_20250730_185949" src="https://github.com/user-attachments/assets/cc16819e-1dc0-4395-bafc-c25933494555" />

<img width="1280" height="800" alt="Screenshot_20250730_223531" src="https://github.com/user-attachments/assets/e99a3583-b427-4362-ad0e-25f0b53ccb23" />


<img width="1280" height="800" alt="Screenshot_20250730_223548" src="https://github.com/user-attachments/assets/d1bab749-dc1e-4451-ad7e-710c44a1e782" />

<img width="1280" height="800" alt="Screenshot_20250730_223559" src="https://github.com/user-attachments/assets/60a490df-952a-44ed-ae5b-dc49283f2df2" />

<img width="1280" height="800" alt="Screenshot_20250730_224650" src="https://github.com/user-attachments/assets/5b5f07f3-4c35-43a6-a9ba-9c7204b1c2cb" />
