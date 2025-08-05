import time
import os
import pyautogui
import requests
from ih_automator.config import COORDS, BLUESTACKS_REGION, DEFAULT_DELAY, WEBHOOK_URL, TASKS_ENABLED

# === click a spot by name from config ===
def click(name, delay=DEFAULT_DELAY):
    x, y = COORDS[name]
    pyautogui.moveTo(x, y, duration=0.4)
    pyautogui.click()
    time.sleep(delay)

def move_to(name):
    x, y = COORDS[name]
    pyautogui.moveTo(x, y, duration=0.3)

# === take a screenshot of Bluestacks window only ===
def screenshot(filename, delay=1.5):
    time.sleep(delay)
    print(f"📸 taking screenshot: {filename}")
    x, y, w, h = (
        BLUESTACKS_REGION["x"],
        BLUESTACKS_REGION["y"],
        BLUESTACKS_REGION["width"],
        BLUESTACKS_REGION["height"]
    )
    if os.path.exists(filename):
        os.remove(filename)
    screenshot_img = pyautogui.screenshot(region=(x, y, w, h))
    screenshot_img.save(filename)
    time.sleep(0.5)

# === upload screenshots to Discord ===
def send_to_discord(filepaths):
    for path in filepaths:
        with open(path, "rb") as f:
            print(f"📤 uploading {path} to Discord...")
            payload = {"content": f"Screenshot: `{path}`"}
            files = {"file": f}
            r = requests.post(WEBHOOK_URL, data=payload, files=files)
            print(f"📬 status: {r.status_code}")
            time.sleep(1)

# === DAILY QUEST LOGIC ===
def run_dailies():
    print("▶️ running daily quests...")

    click("mail")
    click("mail_claim_all", delay=2.8)
    click("mail_exit", delay=2.8)

    click("quests_lady", delay=3.0)
    click("idle_master", delay=3.0)
    click("perform_quests", delay=2.8)
    click("confirm", delay=2.5)
    click("idle_master_exit", delay=2.8)

    screenshot("home.png", delay=2.0)

    click("hero_bag", delay=3.2)
    screenshot("heroes.png", delay=2.5)
    click("hero_bag_exit", delay=2.5)

    click("item_bag", delay=3.0)
    screenshot("items1.png", delay=2.0)

    move_to("scroll_target")
    time.sleep(0.3)
    pyautogui.scroll(-400)
    time.sleep(2)
    screenshot("items2.png", delay=2.0)

    click("item_bag_exit", delay=2.5)

    send_to_discord(["home.png", "heroes.png", "items1.png", "items2.png"])

    print("✅ dailies complete.")

# === STUBS for future tasks ===
def run_aspen():
    print("🧪 Aspen Dungeon not implemented yet.")

def run_heroic_summon():
    print("🧪 Heroic Summon not implemented yet.")

def run_ocr_tracking():
    print("🧪 OCR tracking not implemented yet.")

def run_brave_trial():
    print("🧪 Brave Trial not implemented yet.")

def run_ida():
    print("🧪 IDA not implemented yet.")

def run_tod():
    print("🧪 Tower of Dream not implemented yet.")

def run_too():
    print("🧪 Tower of Oblivion not implemented yet.")

def run_prophet_orbs():
    print("🧪 Prophet Orbs not implemented yet.")

def run_wishing_fountain():
    print("🧪 Wishing Fountain not implemented yet.")

def run_super_wishing():
    print("🧪 Super Wishing Fountain not implemented yet.")

def run_realmsgate():
    print("🧪 Realms Gate not implemented yet.")

def run_void_ark():
    print("🧪 Void Ark not implemented yet.")


# === MAIN MASTER RUNNER ===
def run_daily():
    print("⏳ starting in 3 seconds... switch to Bluestacks.")
    time.sleep(3)

    if TASKS_ENABLED["dailies"]:
        run_dailies()

    if TASKS_ENABLED["ida"]:
        run_ida()

    if TASKS_ENABLED["aspen_dungeon"]:
        run_aspen()

    if TASKS_ENABLED["tower_of_dream"]:
        run_tod()

    if TASKS_ENABLED["tower_of_oblivion"]:
        run_too()

    if TASKS_ENABLED["heroic_summon"]:
        run_heroic_summon()

    if TASKS_ENABLED["prophet_orbs"]:
        run_prophet_orbs()

    if TASKS_ENABLED["wishing_fountain"]:
        run_wishing_fountain()

    if TASKS_ENABLED["super_wishing_fountain"]:
        run_super_wishing()

    if TASKS_ENABLED["brave_trial"]:
        run_brave_trial()

    if TASKS_ENABLED["realms_gate"]:
        run_realmsgate()

    if TASKS_ENABLED["void_ark"]:
        run_void_ark()

    if TASKS_ENABLED["ocr_tracking"]:
        run_ocr_tracking()

    print("✅ all enabled tasks complete.")
