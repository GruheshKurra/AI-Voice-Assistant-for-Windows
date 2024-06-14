# Jarvis: The Personal AI Assistant

This AI Assistant is a personal assistant tool that uses speech recognition to perform various tasks on your computer, such as opening applications, managing files, checking battery status, controlling volume, and more.

## Features

- Open File Explorer
- Close Google Chrome
- Minimize Google Chrome
- Minimize all windows
- Shutdown the computer
- Restart the computer
- Open Notepad
- Open Calculator
- Perform calculations
- Open browser (Google Chrome)
- Play music
- Check battery status
- Lock the computer
- Log off
- Open Settings
- Open Task Manager
- Navigate to specific folders (Desktop, Documents, Downloads, Pictures, Music, Videos)
- Create and delete files
- Create and delete folders
- Open Control Panel
- Open Command Prompt
- Open PowerShell
- Mute and unmute volume
- Increase and decrease volume
- Open Microsoft Edge
- Open Microsoft Word
- Open Microsoft Excel
- Open Microsoft PowerPoint
- Show system information
- Control YouTube (play/pause)
- Control Spotify (play/pause)
- Tell a joke
- Surprise me with a fun fact

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/GruheshKurra/AI-Voice-Assistant-for-Windows.git
    cd AI-Voice-Assistant-for-Windows
    ```

2. **Install required libraries**:

    ```bash
    pip install pyttsx3 speechrecognition pyautogui psutil pywinauto pynput
    ```

## Usage

1. **Run the script**:

    ```bash
    python personal_assistant.py
    ```

2. **Interact with the assistant**:

    The assistant will greet you and start listening for your commands. You can use any of the supported commands listed above.

## Example Commands

- "Open File Explorer"
- "Close Chrome"
- "Minimize Chrome"
- "Minimize all"
- "Shutdown"
- "Restart"
- "Open Notepad"
- "Open Calculator"
- "Calculate 5+3"
- "Open browser"
- "Open Chrome"
- "Play music"
- "Check battery"
- "Lock"
- "Log off"
- "Open Settings"
- "Open Task Manager"
- "Navigate to desktop"
- "Create file test.txt"
- "Delete file test.txt"
- "Create folder test"
- "Delete folder test"
- "Open Control Panel"
- "Open Command Prompt"
- "Open PowerShell"
- "Mute volume"
- "Unmute volume"
- "Volume up"
- "Volume down"
- "Open Edge"
- "Open Word"
- "Open Excel"
- "Open PowerPoint"
- "System info"
- "YouTube pause"
- "YouTube play"
- "Spotify play"
- "Spotify pause"
- "Tell me a joke"
- "Surprise me"

## Notes

- Ensure your microphone is connected and working properly.
- The assistant uses Google Speech Recognition API, so you need an active internet connection.
- The assistant will respond with a voice and perform the requested actions.

## License

This project is licensed under the MIT License.
