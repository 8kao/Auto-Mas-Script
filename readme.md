# Auto-MAS – Automated Microsoft Office Activation

Auto-MAS is a small utility project designed to fully automate the activation of Microsoft Office using Microsoft Activation Scripts (MAS).

> The script is for Windows users **only**

It provides:

a source/ folder containing the original Python script,

an executable/ folder containing a ready-to-run .exe file for Windows Task Scheduler.

The activation steps are completely automated using Pywinauto.

---

## How It Works

The Python script performs the entire activation flow:

1. Verifies that the user has administrator privileges

2. Launches MAS through PowerShell

3. Waits for MAS windows to appear

4. Automatically selects the required menu options

5. Waits for the activation process to finish

6. Closes the window and confirms success


## How to use

1. Open Task Scheduler

2. Create a Task (not a basic task)

3. Under General:

    - Check `Run with highest privileges`

4. Under Actions:

    - Start a program → choose executable/auto-mas-script.exe

    - Set any trigger you want
    
    - At startup

    - Daily

    - At login

The script will run automatically without interaction.

> The Microsoft Office activation key expires every **180 days**, so make sure to set your task trigger accordingly.
> Please note that the device must be powered on for the script to run successfully.
