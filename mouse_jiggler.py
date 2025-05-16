import os
import sys
import time
import threading
import subprocess

# --- Auto-install missing dependencies ---
try:
    import pyautogui
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    os.execv(sys.executable, [sys.executable] + sys.argv)

# --- Mouse Jiggler App ---
class MouseJigglerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Jiggler")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.running = False

        tk.Label(root, text="Interval (seconds):").pack(pady=10)
        self.interval_entry = tk.Entry(root, justify="center")
        self.interval_entry.pack()
        self.interval_entry.insert(0, "10")

        tk.Button(root, text="Start", command=self.start_jiggling).pack(pady=5)
        tk.Button(root, text="Stop", command=self.stop_jiggling).pack(pady=5)

        self.status = tk.Label(root, text="Status: Idle")
        self.status.pack(pady=10)

    def jiggle_mouse(self):
        while self.running:
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 1, y + 1)
            pyautogui.moveTo(x, y)
            self.status.config(text="Status: Jiggling...")
            time.sleep(self.interval)

    def start_jiggling(self):
        try:
            self.interval = float(self.interval_entry.get())
            if self.interval <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return

        if not self.running:
            self.running = True
            threading.Thread(target=self.jiggle_mouse, daemon=True).start()

    def stop_jiggling(self):
        self.running = False
        self.status.config(text="Status: Idle")

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseJigglerApp(root)
    root.mainloop()
