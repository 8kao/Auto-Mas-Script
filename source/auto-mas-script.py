import subprocess
import time
import pywinauto
from pywinauto import Application
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def wait_for_window(title_re, timeout=120):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            app = Application(backend="uia").connect(title_re=title_re)
            return app.window(title_re=title_re)
        except pywinauto.findwindows.ElementNotFoundError:
            time.sleep(1)
    raise TimeoutError(f"Timeout: apparition de la fenêtre trop lente.")

def open_and_interact():
    try:
        if not is_admin():
            print("Le script doit être exécuté en tant qu'administrateur.")
            return
        print("Lancement du script...")
        subprocess.Popen(
            ["powershell.exe", "-Command", "iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)"],
            shell=True
        )

        window = wait_for_window(".*Microsoft Activation Scripts.*")

        window.set_focus()
        time.sleep(2)

        window.type_keys('2')
        time.sleep(1)

        new_window = wait_for_window(".*Ohook Activation.*")

        new_window.type_keys('1')
        time.sleep(30)
        new_window.type_keys('{ENTER}')

        new_window = wait_for_window(".*Microsoft Activation Scripts.*")
        time.sleep(5)
        new_window.close()
        print("Clé activée !")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

open_and_interact()
