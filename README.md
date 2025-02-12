# AI-Tools

# How to set up

## Step 0 - Setup Python (skip this if you already have Python)

Go to https://www.python.org/downloads/ to download Python onto your computer.

Once downloaded, use the Python setup window to set up Python.

## Step 1 - Download files

Click the Python file that shows your OS, then "Download".

## Step 2 - Install libraries with pip

Open Terminal (macOS, Windows) or Command line (Linux), and enter the following commands:

```bash
pip install -q -U google-generativeai
```

```bash
pip install pyautogui
```

```bash
pip install Pillow
```

```bash
pip install pyttsx3
```

and if that doesn't work, try

```bash
pip3 install -q -U google-generativeai
```

```bash
pip3 install pyautogui
```

```bash
pip3 install Pillow
```

```bash
pip3 install pyttsx3
```

The first command is absolutely required. This will allow you to use Google Gemini through my app. The second command is required only is you want Gemini to be able to use your keyboard and mouse. If you don't install it, then you'd have to delete the `import pyautogui as control` line in the code, and then you can only use the chatbot.

## Step 3 - Get a Gemini API key

You need a Google Account. Go to https://aistudio.google.com/app/apikey, sign in, and click "Create API Key". Copy the key.

Right click on the `ai_tools.py` file and select "Open with..." > "IDLE.app" (macOS | Windows and Linux are similar). Remove `API_KEY` and paste your own there.

## Step 4 - Use and set up for easy access

You can now open the `ai_tools.py` file and use the tools! **If you use macOS, you will have to allow "Terminal" to access accessibility shortcuts by opening System Settings > Privacy & Security > Accessibility and toggle Terminal to on.** You can drag the file to your destop for easy access. Make sure it opens with "Python Launcher".
