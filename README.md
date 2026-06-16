# 📁 File Organizer Python

> Automatically sorts cluttered folders into clean, categorized directories — in one script run.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OS Automation](https://img.shields.io/badge/Automation-OS%20Module-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

---

## 🧠 What It Does

Most people's Downloads folder is a disaster. This script fixes that automatically.

Run it once — it scans the target folder, creates category subfolders if they don't exist, and moves every file into the right place based on its extension.

**Before:**
```
Downloads/
├── resume.pdf
├── holiday.mp4
├── screenshot.png
├── notes.docx
├── random_file.xyz
├── lecture.mp4
└── budget.xlsx
```

**After:**
```
Downloads/
├── Documents/
│   ├── resume.pdf
│   ├── notes.docx
│   └── budget.xlsx
├── Videos/
│   ├── holiday.mp4
│   └── lecture.mp4
├── Photos/
│   └── screenshot.png
└── Others/
    └── random_file.xyz
```

---

## ✨ Features

- **Auto-creates folders** — `Documents`, `Videos`, `Photos`, `Others` are created only if they don't already exist
- **Smart sorting** — files are moved based on their extension automatically
- **Catch-all** — anything that doesn't match a known category goes to `Others`, nothing gets lost
- **Non-destructive** — only moves files, never deletes anything
- **Zero dependencies** — uses only Python's built-in `os` and `shutil` modules, no pip install needed

---

## 📂 File Categories

| Folder | Extensions |
|--------|-----------|
| 📄 Documents | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.xls` `.pptx` `.csv` |
| 🎬 Videos | `.mp4` `.mkv` `.avi` `.mov` `.wmv` `.flv` |
| 🖼️ Photos | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` |
| 📦 Others | Anything not in the above categories |

---

## 🚀 How to Use

**1. Clone the repo**
```bash
git clone https://github.com/AshirNarang/file-organizer-python.git
cd file-organizer-python
```

**2. No installation needed** — only uses Python standard library

**3. Run the script**
```bash
python file_organizer.py
```

> By default it organizes the folder where the script is placed. To target a different folder, edit the `target_path` variable at the top of the script.

---

## 🛠️ Tech Stack

- **Python 3.x**
- `os` — folder creation and file detection
- `shutil` — file moving operations

---

## 💡 Why I Built This

I kept having to manually sort my Downloads folder every few weeks. Writing a 30-line Python script to automate it permanently was the obvious fix. It was also my first real automation project — the one that showed me how much you can do with just the Python standard library.

---

## 📌 Future Improvements

- [ ] Add a config file to let users define custom categories and extensions
- [ ] Add logging to show what was moved where
- [ ] Schedule it to run automatically on startup
- [ ] GUI version with folder picker

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">
<sub>Made by <a href="https://github.com/AshirNarang">Ashir Narang</a></sub>
</div>
