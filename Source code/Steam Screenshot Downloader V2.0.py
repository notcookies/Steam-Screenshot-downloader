import os
import re
import sys
import time
import random
import win32con
import requests
import threading
import win32file
import pywintypes
import win32timezone
import tkinter as tk
from PIL import Image
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from tkinter import ttk, filedialog
from urllib.parse import urlparse, urlunparse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor, as_completed

# Constants
CHROME_PATH = os.path.join(os.getcwd(), "chrome", "chrome.exe")
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chrome", "chromedriver.exe")
PROFILE_DIR = "Default"

# Redirect stdout to Text widget
class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.after(0, self.widget.insert, tk.END, message)
        self.widget.after(0, self.widget.see, tk.END)

    def flush(self):
        pass

# Chrome init
def init_chrome(user_data_path):
    options = Options()
    options.binary_location = CHROME_PATH
    options.add_argument(f"--user-data-dir={user_data_path}")
    options.add_argument(f"--profile-directory={PROFILE_DIR}")
    options.add_argument("--log-level=3")
    service = Service(CHROMEDRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)

# Get screenshot links
def get_screenshot_links(driver, steam_id, page):
    url = f"https://steamcommunity.com/id/{steam_id}/screenshots/?p={page}&sort=oldestfirst&browsefilter=myfiles&view=grid&privacy=30"
    for _ in range(6):
        time.sleep(random.uniform(1, 2))
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        links = [a['href'] for a in soup.select('a[href*="//steamcommunity.com/sharedfiles/filedetails/"]')]
        if links:
            print(f"[Page {page}] Found {len(links)} screenshot links.\n")
            print(f"Fetching the original resolution URLs of the {len(links)} screenshots, please wait 1-2 minutes.")
            return links
    print(f"[Page {page}] No screenshot links found.")
    return []

# Get image URL
def get_img_url(driver, link):
    try:
        driver.get(link)
        time.sleep(random.uniform(0.3, 0.6))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        tag = soup.select_one('a[href*="//images.steamusercontent.com/ugc/"]')
        if tag:
            return urlunparse(urlparse(tag['href'])._replace(query=''))
    except:
        return None

def fetch_img_urls_concurrently(driver, links, stop_flag):
    img_urls = [None] * len(links)

    def worker(i, link):
        if stop_flag:
            return
        img_urls[i] = get_img_url(driver, link)

    threads = []
    for i, link in enumerate(links):
        t = threading.Thread(target=worker, args=(i, link))
        t.start()
        threads.append(t)
        time.sleep(0.1)

    for t in threads:
        t.join()
    return [url for url in img_urls if url]


# Download image
def download_img(page, link, save_dir, stop_flag, idx):
    if stop_flag:
        return None
    for attempt in range(3):
        try:
            time.sleep(random.uniform(0.2, 0.5))
            r = requests.get(link, stream=True, timeout=5)
            r.raise_for_status()
            match = re.search(r'"([^"]+)"', r.headers.get('Content-Disposition', ''))
            if match:
                fname = match.group(1)
                match2 = re.match(r'(\d+)_screenshots_(\d+)_(\d+).jpg', fname)
                if match2:
                    appid, shot1, shot2 = match2.groups()
                    folder = os.path.join(save_dir, appid, "screenshots")
                    os.makedirs(folder, exist_ok=True)
                    path = os.path.join(folder, f"{shot1}_{shot2}.jpg")
                    with open(path, "wb") as f:
                        for chunk in r.iter_content(1024):
                            f.write(chunk)
                    if idx % 50 == 0:
                        print(f"[Page {page}] Downloaded {idx+1} screenshots...")
                    return None
        except:
            if attempt == 2:
                print(f"[Page {page}] ❌ Failed to download screenshot {idx+1}")
                return link
    return None

def threaded_download_imgs(img_links, page, save_dir, stop_flag):
    error_links = []
    download_counter = [0]
    lock = threading.Lock()

    def wrapped_download(link, idx):
        result = download_img(page, link, save_dir, stop_flag, idx)
        with lock:
            download_counter[0] += 1
            print(f"[Page {page}] Downloaded {download_counter[0]} of {len(img_links)} screenshots...")
        return result

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {
            executor.submit(wrapped_download, link, idx): link
            for idx, link in enumerate(img_links)
        }
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                error_links.append(result)
    return error_links

# Set creation time for one file
def set_creation_time(filepath, timestamp):
    wintime = pywintypes.Time(timestamp)
    handle = win32file.CreateFile(
        filepath,
        win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL,
        None
    )
    win32file.SetFileTime(handle, wintime, wintime, wintime)
    handle.close()

# Set creation times for all downloaded images
def set_all_creation_times(download_dir):
    for root, _, files in os.walk(download_dir):
        for fname in files:
            if fname.lower().endswith(".jpg"):
                match = re.match(r'(\d+)_\d+\.jpg', fname)
                if match:
                    time_str = match.group(1)
                    try:
                        dt = datetime.strptime(time_str, "%Y%m%d%H%M%S")
                        filepath = os.path.join(root, fname)
                        set_creation_time(filepath, dt)
                    except Exception as e:
                        print(f"Failed to set creation time for {fname}: {e}")

# Generate thumbnails
def generate_thumbnails(screenshots_dir, thumbnails_dir, size=(200, 125)):
    os.makedirs(thumbnails_dir, exist_ok=True)
    for fname in os.listdir(screenshots_dir):
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        src_path = os.path.join(screenshots_dir, fname)
        dst_path = os.path.join(thumbnails_dir, fname)
        try:
            with Image.open(src_path) as img:
                img.thumbnail(size)
                img.save(dst_path, "JPEG", quality=85)
        except Exception as e:
            print(f"Failed to create thumbnail for {fname}: {e}")

# GUI App
class SteamDownloaderApp:
    def __init__(self, root):
        self.stop_flag = False
        self.root = root
        root.title("Steam Screenshot Downloader")
        root.geometry("600x450")
        root.resizable(False, False)

        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10))

        # Variables
        self.steam_id = tk.StringVar()
        self.download_dir = tk.StringVar()
        self.chrome_dir = tk.StringVar()
        self.start_page = tk.StringVar()
        self.end_page = tk.StringVar()

        self.make_widgets()
        sys.stdout = TextRedirector(self.text_log)

    def make_widgets(self): 
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Steam ID:").grid(row=0, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.steam_id, width=40).grid(row=0, column=1, columnspan=2, sticky="w")

        ttk.Label(frame, text="Download Dir:").grid(row=1, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.download_dir, width=30).grid(row=1, column=1, sticky="w")
        ttk.Button(frame, text="Browse", command=self.select_download_dir).grid(row=1, column=2)

        ttk.Label(frame, text="Chrome User Data:").grid(row=2, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.chrome_dir, width=30).grid(row=2, column=1, sticky="w")
        ttk.Button(frame, text="Browse", command=self.select_chrome_dir).grid(row=2, column=2)

        ttk.Label(frame, text="Start Page:").grid(row=3, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.start_page, width=10).grid(row=3, column=1, sticky="w")

        ttk.Label(frame, text="End Page:").grid(row=4, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.end_page, width=10).grid(row=4, column=1, sticky="w")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Start Download", width=15, command=self.start_thread).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Stop Download", width=15, command=self.stop_download).pack(side="left", padx=10)

        self.text_log = tk.Text(frame, height=12, wrap="word", font=("Consolas", 9))
        self.text_log.grid(row=6, column=0, columnspan=3, sticky="nsew", pady=10)
        self.text_log.config(state="normal")


    def select_download_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.download_dir.set(path)

    def select_chrome_dir(self):
        path = filedialog.askdirectory()
        if path:
            self.chrome_dir.set(path)

    def start_thread(self):
        t = threading.Thread(target=self.run_downloader)
        t.start()
    def stop_download(self):
        self.stop_flag = True
        print("⛔Stop after completing the remaining tasks...")
        time.sleep(3)
        self.stop_flag = False

    def run_downloader(self):
        steam_id = self.steam_id.get()
        download_dir = self.download_dir.get()
        chrome_dir = self.chrome_dir.get()
        try:
            start_page = int(self.start_page.get())
            end_page = int(self.end_page.get())
        except:
            print("Start and end pages must be integers.")
            return

        if not (steam_id and download_dir and chrome_dir):
            print("All fields are required.")
            return

        os.makedirs(download_dir, exist_ok=True)
        driver = init_chrome(chrome_dir)
        time.sleep(random.uniform(1, 2))

        for page in range(start_page, end_page + 1):
            if self.stop_flag:
                print("⛔ Download stopped by user.")
                break
            links = get_screenshot_links(driver, steam_id, page)
            img_links = [get_img_url(driver, url) for url in links if url]
            retry_links = img_links
            while retry_links:
                retry_links = threaded_download_imgs(retry_links, page, download_dir, self.stop_flag)

            print(f"[Page {page}] ✅ Page download completed. Total downloaded: {len(img_links) - len(retry_links)}\n")

        driver.quit()
        print("✅ All downloads completed.")
        
        set_all_creation_times(download_dir)
        print("✅ Creation time update completed.")

        for appid in os.listdir(download_dir):
            app_screenshot_dir = os.path.join(download_dir, appid, "screenshots")
            app_thumbnail_dir = os.path.join(app_screenshot_dir, "thumbnails")
            if os.path.isdir(app_screenshot_dir):
                generate_thumbnails(app_screenshot_dir, app_thumbnail_dir)
        print("✅ Thumbnails generation completed.")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SteamDownloaderApp(root)
    root.mainloop()
