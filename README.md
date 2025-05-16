# 🖱️ Mouse Jiggler GUI

A simple and user-friendly **Mouse Jiggler** application written in Python. Prevent your system from going idle by automatically simulating small mouse movements at regular intervals. Useful for remote work, streaming, or avoiding AFK detection.

---

## ✨ Features

- 🔄 Moves mouse by 1px every X seconds
- 🧠 Prevents screensaver, lock, or idle timeout
- 🖼️ Intuitive GUI using Tkinter
- 🧵 Runs in the background using threading
- ⚙️ Auto-installs missing dependencies on first run

---

## 📦 Requirements

Install dependencies automatically (first run) or manually with:

```bash
pip install pyautogui
```

---

## 🚀 How to Run

```bash
python mouse_jiggler.py
```

---

## 🖥️ Usage

1. Enter your desired interval in seconds (e.g., `10`)
2. Click **Start** to begin jiggling
3. Click **Stop** to pause
4. Close the window to exit

---

## 🔧 How It Works

- Uses `pyautogui` to move the mouse by 1px diagonally and back
- Interval is customizable via GUI input
- GUI updates status to show jiggling or idle state

```python
x, y = pyautogui.position()
pyautogui.moveTo(x + 1, y + 1)
pyautogui.moveTo(x, y)
```

---

## 🛠️ GUI Preview

```
+--------------------------+
|     Mouse Jiggler       |
|--------------------------|
| Interval (seconds): [10]|
|  [Start]   [Stop]        |
| Status: Jiggling...     |
+--------------------------+
```

---

## 📌 Notes

- Runs only while GUI window is open
- Designed for Windows, but works on most platforms with Python and Tkinter
- Consider running in the background for passive use
