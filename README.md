# System Activity Monitoring Suite

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Python-based desktop monitoring application that captures keyboard activity, periodically records screen and webcam footage, streams logs to a real-time monitoring dashboard, and securely packages reports for email delivery.

> This project was developed for educational purposes to demonstrate Python programming, multithreading, socket programming, computer vision, automation, and desktop application development.

---

## Features

- Real-time keyboard activity logging
- Live monitoring dashboard using Flask & Socket.IO
- Automatic screen recording
- Webcam recording
- Automatic report packaging (ZIP)
- Email delivery of reports
- Thread-safe logging
- Environment variable configuration using `.env`
- Modular reporting system
- Automatic report generation every 30 seconds

---

## Tech Stack

- Python 3.12
- Flask
- Flask-SocketIO
- OpenCV
- PyAutoGUI
- Pynput
- NumPy
- SMTP (Gmail)
- Socket Programming

---

## Project Structure

```
KEYLOGGER-FINAL/
│
├── key.py
├── monitor_server.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── logs/
│
├── templates/
│   └── index.html
│
└── .venv/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

---

## Running the Project

Start the monitoring server:

```bash
python monitor_server.py
```

In another terminal:

```bash
python key.py
```

Open your browser:

```
http://localhost:5000
```

---

## Architecture

```
Keyboard Events
        │
        ▼
 Keyboard Logger
        │
        ▼
TCP Socket Client ─────────► Flask Monitoring Server
        │                           │
        │                           ▼
        │                   Live Dashboard
        │
        ▼
Screen Recorder
        │
        ▼
Camera Recorder
        │
        ▼
ZIP Report Generator
        │
        ▼
Email Service
```

---

## Configuration

The project uses environment variables.

Copy:

```
.env.example
```

to

```
.env
```

and fill in your own credentials.

---

## Future Improvements

- Automatic email retry
- Report scheduling improvements
- Better dashboard analytics
- Configuration GUI
- Cross-platform support

---

## Disclaimer

This project is intended **only for educational, research, and authorized security testing purposes**. It should only be used on systems where you have explicit permission to monitor activity. The author is not responsible for any misuse.

---

## License

MIT License