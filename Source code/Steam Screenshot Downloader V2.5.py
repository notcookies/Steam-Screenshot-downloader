import os
import re
import sys
import time
import random
import win32con
import requests
import threading
import win32file
import pythoncom
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
def get_screenshot_links(driver, steam_id, page, appid=None):
    base_url = f"https://steamcommunity.com/id/{steam_id}/screenshots/?p={page}&sort=oldestfirst&browsefilter=myfiles&view=grid&privacy=30"
    if appid:
        base_url += f"&appid={appid}"
    for _ in range(6):
        time.sleep(random.uniform(1, 2))
        driver.get(base_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        links = [a['href'] for a in soup.select('a[href*="//steamcommunity.com/sharedfiles/filedetails/"]')]
        if links:
            print(f"[Page {page}] Found {len(links)} screenshot links.")
            print(f"Fetching the original resolution URLs of the {len(links)} screenshots, please wait ...")
            return links
    print(f"[Page {page}] No screenshot links found.")
    return []

# Chrome.get_cookies
def extract_steam_cookies_from_driver(driver, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        cookies = driver.get_cookies()
        cookie_dict = {c['name']: c['value'] for c in cookies}
        # check cookie
        if all(k in cookie_dict for k in ["steamLoginSecure", "sessionid"]):
            print("✅ Steam cookies extracted successfully.")
            return cookie_dict
        time.sleep(delay)
    print("❌ Failed to extract required cookies after 3 attempts.")
    return {}

# Get image URL
# change driver.get to request_html
def get_img_url_from_html(link, cookies):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        r = requests.get(link, headers=headers, cookies=cookies, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.select_one('a[href*="//images.steamusercontent.com/ugc/"]')
        if tag:
            return urlunparse(urlparse(tag['href'])._replace(query=''))
    except Exception as e:
        print(f"Error fetching {link}: {e}")
    return None

# fetch requests img_urls
def fetch_img_urls_concurrently_requests(links, cookies, page):
    def worker(link):
        return get_img_url_from_html(link, cookies)

    img_urls = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(worker, link): link for link in links}
        for i, future in enumerate(as_completed(futures)):
            try:
                result = future.result(timeout=15)
                if result:
                    img_urls.append(result)
            except Exception as e:
                print(f"Failed to fetch link: {futures[future]} Error: {e}")
    print(f"[Page {page}] ✅ Retrieved {len(img_urls)} original image links.\n")
    return img_urls

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
                original_fname = match.group(1)

                # App-id_screenshots_File-name.jpg
                if "_screenshots_" in original_fname:
                    suffix = original_fname.split("_screenshots_")[1]
                    new_fname = suffix
                    appid = original_fname.split("_screenshots_")[0]
                else:
                    new_fname = original_fname
                    appid = "unknown"

                folder = os.path.join(save_dir, appid, "screenshots")
                os.makedirs(folder, exist_ok=True)
                path = os.path.join(folder, new_fname)
                with open(path, "wb") as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                    return None
        except:
            if attempt == 2:
                return link
    return None

def threaded_download_imgs(img_links, page, save_dir, stop_flag, max_retries=5, retry_history=None, link_to_idx=None):
    if retry_history is None:
        retry_history = {}

    if link_to_idx is None:
        link_to_idx = {link: i for i, link in enumerate(img_links)}

    error_links = []
    success_count = 0
    lock = threading.Lock()

    def wrapped_download(link):
        result = download_img(page, link, save_dir, stop_flag, idx=None)
        return link, result

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {
            executor.submit(wrapped_download, link): link
            for link in img_links
        }

        for future in as_completed(future_to_url):
            link, result = future.result()
            idx = link_to_idx.get(link, "?")
            if result is None:
                with lock:
                    success_count += 1
                    print(f"[Page {page}] Downloaded {idx+1} of {len(link_to_idx)} screenshots...")
            else:
                retry_history[link] = retry_history.get(link, 0) + 1
                if retry_history[link] < max_retries:
                    error_links.append(link)
                else:
                    print(f"[image {idx+1}]\n{link}")

    return error_links, retry_history, success_count

#Extract timestamp from filenames with new/old formats
def extract_datetime_from_filename(fname):
    # 1.new format(after 2016): 20250403215812_1.jpg
    match = re.match(r'^(\d{14})_\d+', fname)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y%m%d%H%M%S")
        except:
            pass
    # 2.old format(before 2016): 2012-01-24_00001.jpg
    match = re.match(r'^(\d{4}-\d{2}-\d{2})_', fname)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except:
            pass
    return None

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
                dt = extract_datetime_from_filename(fname)
                if dt:
                    filepath = os.path.join(root, fname)
                    try:
                        set_creation_time(filepath, dt)
                    except Exception as e:
                        print(f"Failed to set creation time for {fname}: {e}")
                else:
                    print(f"Skipped (no timestamp found): {fname}")

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

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

# GUI App
class SteamDownloaderApp:
    def __init__(self, root):
        self.stop_flag = False
        self.root = root
        root.title("Steam Screenshot Downloader V2.5")
        root.iconbitmap(resource_path("Steam&Cookies.ico"))
        root.geometry("900x600")
        root.resizable(True, True)

        style = ttk.Style()
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10))

        # Variables
        self.steam_id = tk.StringVar()
        self.download_dir = tk.StringVar()
        self.chrome_dir = tk.StringVar()
        self.start_page = tk.StringVar()
        self.end_page = tk.StringVar()
        self.appid = tk.StringVar()

        # Set default download directory
        default_download_dir = os.path.join(os.getcwd(), "Download_Screenshot")
        self.download_dir.set(default_download_dir)

        # Set default Chrome user data path
        user_profile = os.environ.get("USERPROFILE", "")
        default_chrome_path = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome for Testing", "User Data")
        if os.path.exists(default_chrome_path):
            self.chrome_dir.set(default_chrome_path)

        self.make_widgets()
        sys.stdout = TextRedirector(self.text_log)

    def make_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        #Set up five columns: 50px fixed + left spacer + content + right spacer + 50px fixed
        frame.grid_columnconfigure(0, minsize=50)
        frame.grid_columnconfigure(1, minsize=15,weight=1)
        frame.grid_columnconfigure(2, weight=2)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_columnconfigure(4, minsize=50) 
        frame.rowconfigure(9, weight=1)

        # Steam ID
        ttk.Label(frame, text="Steam ID:").grid(row=0, column=1, sticky="e", pady=3, padx=(0, 5))
        ttk.Entry(frame, textvariable=self.steam_id).grid(row=0, column=2, sticky="ew", pady=3)

        # Save Location
        ttk.Label(frame, text="Save Location:").grid(row=1, column=1, sticky="e", pady=3, padx=(0, 5))
        ttk.Entry(frame, textvariable=self.download_dir).grid(row=1, column=2, sticky="ew", pady=3)
        ttk.Button(frame, text="Browse", command=self.select_download_dir, width=10).grid(row=1, column=3, pady=3)

        # Chrome Dir
        ttk.Label(frame, text="Chrome User Data:").grid(row=2, column=1, sticky="e", pady=3, padx=(0, 5))
        ttk.Entry(frame, textvariable=self.chrome_dir).grid(row=2, column=2, sticky="ew", pady=3)
        ttk.Button(frame, text="Browse", command=self.select_chrome_dir, width=10).grid(row=2, column=3, pady=3)

        # App ID
        ttk.Label(frame, text="App ID (optional):").grid(row=3, column=1, sticky="e", pady=3, padx=(0, 5))
        appid_frame = ttk.Frame(frame)
        appid_frame.grid(row=3, column=2, sticky="w", pady=3)
        ttk.Entry(appid_frame, textvariable=self.appid, width=20).pack(side="left")
        ttk.Label(appid_frame, text="(leave blank for all)", foreground="gray").pack(side="left", padx=5)

        # Start Page
        ttk.Label(frame, text="Start Page:").grid(row=4, column=1, sticky="e", pady=3, padx=(0, 5))
        ttk.Entry(frame, textvariable=self.start_page, width=10).grid(row=4, column=2, sticky="w", pady=3)

        # End Page
        ttk.Label(frame, text="End Page:").grid(row=5, column=1, sticky="e", pady=3, padx=(0, 5))
        ttk.Entry(frame, textvariable=self.end_page, width=10).grid(row=5, column=2, sticky="w", pady=3)

        # Browse button
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=8, column=2, pady=10)
        ttk.Button(button_frame, text="Start Download", width=15, command=self.start_thread).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Stop Download", width=15, command=self.stop_download).pack(side="left", padx=10)

        # Log output box
        self.text_log = tk.Text(frame, height=12, wrap="word", font=("Consolas", 9),
                                borderwidth=1, relief="solid", highlightthickness=0)
        self.text_log.grid(row=9, column=2, sticky="nsew", pady=10)
        frame.rowconfigure(9, weight=1)
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
        steam_id = self.steam_id.get().strip()
        download_dir = os.path.normpath(self.download_dir.get().strip())
        chrome_dir = os.path.normpath(self.chrome_dir.get().strip())
        appid_input = self.appid.get().strip()
        appid = appid_input if appid_input else None

        try:
            start_page = int(self.start_page.get())
            end_page = int(self.end_page.get())
        except:
            print("Start and end pages must be integers.")
            return

        if not (steam_id and download_dir and chrome_dir):
            print("All fields are required.")
            return

        if not os.path.exists(download_dir):
            os.makedirs(download_dir, exist_ok=True)

        driver = init_chrome(chrome_dir)
        time.sleep(random.uniform(1, 2))
        
        cookies = None

        for page in range(start_page, end_page + 1):
            if self.stop_flag:
                print("⛔ Download stopped by user.")
                break

            links = get_screenshot_links(driver, steam_id, page, appid=appid)
            if not links:
                continue

            # try get cookies
            if cookies is None:
                print("Extracting Steam cookies from Chrome session...")
                cookies = extract_steam_cookies_from_driver(driver, retries=3, delay=2)
                if not all(k in cookies for k in ["steamLoginSecure", "sessionid"]):
                    print("❌ Missing required cookies from Chrome session.")
                    driver.quit()
                    return

            img_links = fetch_img_urls_concurrently_requests(links, cookies, page)
            
            successful_downloads = 0
            retry_links = img_links
            retry_history = {}
            max_retries = 4
            attempt = 0

            link_to_idx = {link: i for i, link in enumerate(img_links)}

            while retry_links and attempt < max_retries:
                attempt += 1
                if attempt == 2:
                    print(f"\nFind {len(retry_links)} Error screenshot links.")
                if attempt > 1:
                    print(f"🔁 Retrying attempt {attempt-1}.")
                if attempt == max_retries:
                    print('Failed to download after max retries:')
                    
                retry_links, retry_history, new_success = threaded_download_imgs(
                    retry_links, page, download_dir, self.stop_flag, max_retries, retry_history,
                    link_to_idx=link_to_idx
                )
                successful_downloads += new_success

            print(f"\n[Page {page}] ✅ Page download completed. Total downloaded: {successful_downloads}.\n")
        
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
        print("✅ All Done.")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SteamDownloaderApp(root)
    root.mainloop()