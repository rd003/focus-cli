# Focus CLI ⏱️

A simple command-line time tracker for focus sessions. Track your productive time with ease!

**Note:** I have only tested this app in my machine (linux mint 22.2 zara). I am not aware how it will work in other OS.

## Features

- ⏳ Start focus timers with customizable durations
- 📊 Automatically tracks and stores your focus time
- 🔔 Desktop notifications when timer completes
- 📅 Keeps history of last 3 days
- ⌨️ Stop timer early with Ctrl+C (still records elapsed time)

## Installation

### For Users

Make sure to install pipx `sudo apt install pipx -y`

```bash
git clone https://github.com/rd003/focus-cli.git
cd focus-cli
pipx install .
```

To uninstall later

```bash
pipx uninstall focus-cli
```

### For Developers

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/focus-cli.git
   cd focus-cli
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Install the package in editable mode:**
   ```bash
   pip install -e .
   ```

   This allows you to make changes to the code and see them reflected immediately without reinstalling.

## Usage

### Start a Timer

```bash
# Start a 25-minute focus session (Pomodoro)
focus 25

# Start a 5-minute break
focus 5

# Start a 1-hour deep work session
focus 60
```

### View Your Progress

```bash
# Show today's total time
focus --show

# Show time for a specific date
focus --show --date 2025-10-05
```

### Stop Early

Press `Ctrl+C` to stop the timer before it finishes. The elapsed time will still be recorded!

## Data Storage

Your focus time data is stored in `~/.time-tracker/time-tracker.json`

The app keeps track of the last 3 days of data automatically.

## Project Structure

```
focus-cli/
├── focus_cli/
│   ├── __init__.py
│   └── cli.py           # Main application code
├── setup.py             # Package configuration
├── pyproject.toml       # Modern Python packaging (optional)
├── requirements.txt     # Runtime dependencies
├── requirements-dev.txt # Development dependencies
├── README.md
└── LICENSE
```

## Requirements

- Python 3.12+
- Linux, macOS, or Windows


## Acknowledgments

- Built with [Plyer](https://github.com/kivy/plyer) for cross-platform notifications
- Inspired by the Pomodoro Technique and windows 11 focus app.

---

**Happy focusing! 🎯**