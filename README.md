# 🎙️ Nova – Python Voice Assistant

**Nova** is a smart voice assistant built in Python that can perform basic tasks using speech recognition and text-to-speech technology. It can tell time/date, open websites, fetch Wikipedia summaries, tell jokes, set reminders, send emails, and more.

---

## 🎬 Demo Video

> 🎩 [Watch Demo on YouTube](https://youtube.com/your-demo-link)

---

## 📌 Features

* 🕒 Tells the current time and date
* 🌐 Opens websites like YouTube and Google
* 📚 Searches topics on Wikipedia
* 🤣 Tells random jokes
* 📝 Sets and shows reminders
* ✉️ Sends emails (via Gmail SMTP)
* ☁️ Optional: Get weather updates (if extended)

---

## 🛠️ Tech Stack

* Python 3.x
* `SpeechRecognition` – to recognize voice
* `pyttsx3` – text-to-speech
* `wikipedia` – fetch Wikipedia summaries
* `pyjokes` – random jokes
* `requests` – (optional for weather API)
* `smtplib` – for sending emails via SMTP

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/nova-voice-assistant.git
cd nova-voice-assistant
```

### 2. Create a Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 🔐 Email Setup (Optional for Sending Emails)

Set the following environment variables in your system:

* `NOVA_EMAIL` – your Gmail address
* `NOVA_EMAIL_PASS` – app password (use App Passwords in Gmail with 2FA)

---

## ▶️ Running the Assistant

```bash
python nova.py
```

Once it starts, Nova will greet you and start listening to your voice commands.

---

## 💡 Sample Commands

* "What's the time?"
* "Open YouTube"
* "Search for Python on Wikipedia"
* "Tell me a joke"
* "Set reminder"
* "Send email"

---

## 📞 Contact Information

**Developer:** Your Name
**Email:** [shanmathigopikrishnan@gmail.com](mailto:shanmathigopikrishnan@gmail.com)
**GitHub:** [shanmathigopikrishnan](https://github.com/shanmathigopikrishnan)
**LinkedIn:** [Shanmathi G](www.linkedin.com/in/shanmathigopikrishnan)

Feel free to reach out for contributions, suggestions, or queries!

---
