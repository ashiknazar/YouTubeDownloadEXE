# YouTubeDownloadEXE
a desktop application to download youtube videos 



# 🎬 YouTube Video Downloader (PyQt5)

A simple desktop application built with Python and PyQt5 to download YouTube videos using `yt-dlp`.

---

## 📦 Features

- 🖱️ User-friendly GUI (built with PyQt5)
- 🔗 Paste any YouTube video URL
- 📁 Choose download location
- 📊 Live progress bar
- ✅ Save as `.exe` for Windows
- ⚠️ Handles download errors

---

## 🖥️ Requirements

Install the required Python packages:

```bash
pip install yt-dlp pyqt5
```
## ▶️ How to Run

### 💻 From Python file

1. Save the script as `EtYOU.py`
2. Run it:

```bash
python EtYOU.py
```
### 📦 Convert to .exe (Windows)

Use [PyInstaller](https://pyinstaller.org/) to convert your app into a standalone executable.

```bash
pip install pyinstaller
pyinstaller --onefile --windowed EtYOU.py
```
> ✅ **Optional: Add an icon to your executable**

```bash
pyinstaller --onefile --windowed --icon=EtYOU.ico EtYOU.py
```

## 🔐 Allow the .exe to Run on Windows (Manage Security)

Sometimes Windows Defender might block your `.exe` file, thinking it might be unsafe. This is a **false positive**, especially for programs you built yourself using PyInstaller.

### ✅ Steps to Allow the File:

1. **Run the `.exe` file**
   - If you see a warning like **"Windows protected your PC"**, click **More info** and then **Run anyway**.

2. **Add an Exclusion in Windows Defender** (recommended for developers)

   - Open **Windows Security**
   - Go to **Virus & threat protection**
   - Click **Manage settings** under **Virus & threat protection settings**
   - Scroll down to **Exclusions** → Click **Add or remove exclusions**
   - Click **+ Add an exclusion** → Choose **File** or **Folder**
   - Select your `.exe` file or the entire folder (e.g., `dist/`)

> 💡 This tells Windows Defender to stop flagging your safe file as a threat.

---

**Tip:** If you're planning to share the `.exe` with others, consider signing your app with a digital certificate to avoid these warnings completely.
