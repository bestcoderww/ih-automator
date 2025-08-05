# 📋 TODO - Idle Heroes Automator

## ✅ DONE
- Working daily automation (mail, quests, screenshots)
- Discord webhook integration
- Screenshot cropping to Bluestacks region - NEEDS REVISION FOR PUBLISHED VERSION
- Project structure cleaned (bot.py, daily.py)
- Added README.md, LICENSE, .gitignore, requirements.txt

---

## 🔜 NEXT UP

### 🧠 Vision-based automation (OpenCV)
- [ ] `vision/detector.py`: template matching with cv2
- [ ] store reference buttons in `/assets/`
- [ ] replace coordinate clicks with image detection

### 🧾 OCR progress tracking
- [ ] `vision/ocr.py`: extract gold, gems, scrolls
- [ ] `resources.py`: parse and log that data
- [ ] upload values alongside screenshots

### 🧪 New features
- [ ] `aspen.py` stub
- [ ] `brave_trial.py` stub
- [ ] `ida.py`, `tower_of_dream.py`, etc.
- [ ] toggle logic for each in config

### 🎛️ UX / polish
- [ ] timestamped screenshots folder
- [ ] error handling if screen changes fail
- [ ] optional retry logic for missed clicks

---

## 💡 IDEAS
- [ ] make it respond to Discord commands (2-way)
- [ ] schedule auto-runs (daily cron job or task scheduler)
- [ ] host on Raspberry Pi or headless Mac
- [ ] publish it for others to use
