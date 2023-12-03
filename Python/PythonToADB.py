import subprocess
import time

def run_adb_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande ADB : {e}")

# Forcer l'arrêt de toutes les applications en cours
run_adb_command("adb shell am force-stop com.android.settings")
run_adb_command("adb shell am force-stop com.android.bluetooth")
# Ajoutez d'autres commandes am force-stop pour d'autres applications si nécessaire

# Revenir à l'écran d'accueil (home screen)
run_adb_command("adb shell input keyevent KEYCODE_HOME")

# Attendre un court moment
time.sleep(1.5)  # Changed from 0.1 to 1.5 seconds

# Ouvrir les paramètres Wi-Fi et prendre une capture d'écran
run_adb_command("adb shell am start -a android.settings.WIFI_SETTINGS")
time.sleep(1.5)  # Changed from 0.1 to 1.5 seconds
run_adb_command("adb shell screencap /sdcard/wifi_settings.png")

# Attendre 10 secondes
time.sleep(5)

# Ouvrir les paramètres Bluetooth et prendre une capture d'écran
run_adb_command("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
time.sleep(1.5)  # Changed from 0.1 to 1.5 seconds
run_adb_command("adb shell screencap /sdcard/bluetooth_settings.png")

# Revenir à l'écran d'accueil (home screen)
run_adb_command("adb shell input keyevent KEYCODE_HOME")

# Laisser la console ouverte
input("Appuyez sur Entrée pour fermer la console.")
