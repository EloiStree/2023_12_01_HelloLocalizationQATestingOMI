# Salut à tous

En tant que testeur, vous allez devoir rédiger des rapports, mais aussi enregistrer des vidéos, des captures d'écran et du son. Il existe de nombreuses façons de le faire. Pour cet atelier, je vais vous montrer une méthode.

## Étape par étape

Allons-y étape par étape. Il y a beaucoup d'installations à effectuer et de travail à se familiariser.

### OBS : Open Broadcast Software

[Download OBS et OBS Portable](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/8)

OBS est un outil qui vous permettra d'enregistrer des vidéos. Cet outil est parfait et Open Source.

Si vous enregistrez la vidéo, n'oubliez pas de choisir un emplacement approprié :
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/fe8316ce-0b57-4a9b-9ca9-b23c73847885)

[Guide vidéo pour débuter sur OBS](https://www.youtube.com/results?search_query=commencer+sur+obs)


#### Shortcut

Comme notre but est de créer des outils qui permettent de se faciliter la vie, nous allons définir des macros dans OBS et utiliser ces macros depuis Python pour lancer l'enregistrement.

![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/22915316-42fb-46fc-bfbd-f555f6722a91)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/5dae7ac3-0645-4cab-b0d1-c961fe78cc77)

Shortcut, Example:
- CTRL+Shift+ALT+ Arrow Left = Start recording
- CTRL+Shift+ALT+ Arrow Right = Stop recording
- CTRL+Shift+ALT+ Arrow Up = Screenshot


#### Websocket

C'est bien beau de hacker les touches pour lancer un enregistrement... Mais n'y aurait-il pas quelque chose de plus direct ? Une API ?
Depuis OBS 28, il est possible de lancer un Websocket pour contrôler OBS :) !!!

Cela permet de prendre le contrôle de ce que l'on veut afficher et de changer à la volée l'outil par le réseau.
Info: [Lien vers l'issue](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/21)
Par exemple, depuis [Streamer.bot](https://streamer.bot) ou depuis son navigateur web: [http://obs-web.niek.tv](http://obs-web.niek.tv)  
Pour les plus audacieux d'entre vous:  
[https://websocketking.com](https://websocketking.com)

Et comme nous avons fait du Python... Vous devinez pourquoi je vous en parle ;) 
[obs-websocket-py sur GitHub](https://github.com/Elektordi/obs-websocket-py)

Vous pouvez le paramétrer en lançant OBS:  
`D:\OBS Video>OBSPortable.exe --portable --websocket_port 4545 --websocket_password HelloWorld --websocket_debug --websocket_ipv4_only`  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/57793bff-94c0-491e-9d92-80ec955a7c6f)


### SCRCPY: Screen copy (& ADB)

Nous allons un peu explorer comment enregistrer votre écran de téléphone et chipoter avec.

#### Mode développeur

Avant de pouvoir "jouer" avec son téléphone, il faut lui permettre d'être débuggé par USB et éventuellement d'installer depuis une source inconnue. Pour cela, il faut passer votre téléphone en mode développeur.
L'idée reste la même mais est différente sur tous les téléphones Android:
[Guide détaillé](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/30)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/2933e161-1058-4b6f-bd67-8186540faee5)![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/0c94d4d5-495d-43e3-9910-1f7e46271911)

#### SCRCPY
Pour pouvoir enregistré ce qui se passe sur votre téléphone Android ou sur votre casque de réalité virtuelle Android.
Vous allez devoir utiliser SCRCPY qui est un project open source qui permet de communiquer avec les flux vidéos du téléphone.

[Download](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/4)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/d990e5ec-bc00-4252-95cc-5cd36e77d35a)

#### ADB: Android debug bridge

Android Debug Bridge est un autre outil qui est référencé SCRCPY qui permet de communiquer avec votre téléphone.
Il permet de communiquer avec votre téléphone.

##### Command Line

Pour utiliser ADB, vous allez utiliser un interface d'un développeur ou utiliser de command via la console sur window.


```
adb devices -l
adb reboot
adb install MonJeu.apk
adb uninstall com.entreprise.nomdujeu
adb shell screencap -p /sdcard/capture.png
adb pull /sdcard/capture.png chemin_sur_ordinateur

```

![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/5924354d-a503-47df-a020-ce5fe9dd4834)

![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/986cec82-357d-4b5f-b469-cfe753d2dad6)


`adb shell input keyevent KEYCODE_BACK`
`adb shell input keyevent KEYCODE_ENTER`
`adb shell input keyevent KEYCODE_MENU`
All keycodes: https://developer.android.com/reference/android/view/KeyEvent

Ouvrir la page des paramètres
`adb shell am start -a android.settings.SETTINGS`

Ouvrir une page web
`adb shell am start -a android.intent.action.VIEW -d "http://www.example.com"`

Lancer le playstore
`adb shell am start -a android.intent.action.VIEW -d "market://details?id=com.android.vending"`

Capture d'écran;
`adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png`
`adb exec-out screencap -p > screen.png`

Start / Stop recording on the device:
`adb shell screenrecord /sdcard/yourfilename.mp4`
`adb shell pkill -l 15 -f /system/bin/screenrecord`
`adb pull /sdcard/yourfilename.mp4`

Ne pas utiliser de cable  ?

`adb tcpip 5555`
`adb shell ip -f inet addr show wlan0`
`adb connect adresse_ip_du_telephone:5555`


**Essayez de deviner ce que fait le script suivant :**

``` py
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

```

_GPT used for those command https://chat.openai.com/share/0d61d5f0-21ed-4efa-a03b-24dc21b8b40b_


# La VR ?

Slide: https://docs.google.com/presentation/d/1X9EGTp2brfUrhXHbxRmtjNG-ZmBA3ZfKqmobidP_fgU/edit?usp=sharing
Headset: https://docs.google.com/presentation/d/12jUnK69IXJHHdJyTyVmaayfdgkEIuzoSXc8ULkvxNHY/edit#slide=id.g3f61c4e2ac_4_436
What is VR 
- https://www.youtube.com/watch?v=wRCS2-AAyNM
- https://www.youtube.com/watch?v=8rVnkWbLnk8

# By Side Quest

Il y a des centaines de commandes et, dans l'ensemble, il y a des milliers de combinaisons. C'est la raison pour laquelle il existe des "wrapper" ou des emballages. Des logiciels dont le but n'est pas de créer mais de proposer une interface pour utiliser ADB. Comme SideQuest qui permet de facilement utiliser ADB avec les casques VR.

**Download:** [SideQuest](https://sidequestvr.com/setup-howto)  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/2da8ccfd-2989-42e2-89eb-92a113e12a0c)

## Le son

- [Spectrogram](https://spectrogram.sciencemusic.org)
- C'est quoi le son ? [Vidéo](https://youtu.be/24yESm63tSY)
  [![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/dd320a9c-c51c-459b-9614-e286ffc3921f)](https://youtu.be/24yESm63tSY)
  ![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a8f2b87b-4508-42bf-80e3-c579c361e44a) [Vidéo](https://youtu.be/24yESm63tSY?t=220)
  ![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/3f5b493f-35e8-4ebc-beab-8cfa0d85bc12) [Vidéo](https://youtu.be/24yESm63tSY?t=360)
  
  440 Hz (nombre de fréquences par seconde)

### Qu'est-ce qu'un spectrogramme ?
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/b8f92205-45f5-446e-90b4-564bef17ae4e)  
[Vidéo](https://youtu.be/_FatxGN3vAM)

### Comment construire un spectrogramme à partir du son :
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/5bda3db5-83f0-42bc-812f-beb2602d666b)
[Vidéo](https://youtu.be/Z7YM-HAz-IY?list=PLhA3b2k8R3t2Ng1WW_7MiXeh1pfQJQi_P&t=356)

## VoiceMeeter
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/c3e1d4b2-1aeb-46cf-8f85-acde2b32701b)
**Download:** [VoiceMeeter](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/31)

## OBS : Astuce pour rediriger le son

OBS n'a pas d'enregistreur audio. Il est construit pour la vidéo. Mais il a beaucoup d'options sur l'audio, dont le fait de rediriger le son pour "monitorer" la qualité du stream. C'est ce que l'on va utiliser avec VoiceMeeter pour permettre d'enregistrer le son de nos tests. Attention de désactiver le Ducking (décaler le son pour débugger le son du stream)  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a6fe84fa-b815-4d79-bc8c-c5a0bef0a1ec)

Il faut aussi mettre l'option "Output Mode" en avancé et vous pouvez augmenter le bitrate de l'audio :  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/d40f9b3f-752c-45a6-9efa-e8110c0aaa30)

### Enregistreur de fenêtre (Sound Recorder)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/d526782e-1681-46be-b2bb-97ab45cff946)

![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/c63fb874-fdee-4f17-b459-40acdf8e8915)

**Raccourcis :**
- CTRL+ R : Enregistrer
- Echap : Arrêter l'enregistrement
- Espace : Mettre en pause l'enregistrement

Cette application enregistre les entrées sons. Mais par VoiceMeeter, nous avons à notre disposition une entrée son.  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/adc2fe02-858f-41f0-b93e-1352222e8121)


## Audacity
[**Download**](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/9)

Audacity est la meilleure application open source que je connaisse pour éditer du son.  
Elle permet aussi d'enregistrer, mais comme la procédure d'exportation du son n'est pas facile à automatiser avec SendMessage, on ne va pas l'utiliser pour enregistrer.    
Cependant, vous en aurez besoin pour "trimmer" et retravailler le son au besoin.  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/cc19a6e7-260e-4441-abbe-c88108dadcde)

**Raccourcis :**
- Ctrl + Shit + E   500> Enter 500> Enter 500> Enter = Exporter le son
- Ctrl+ A  500> Enter 500> Enter = Supprimer toute la piste

## NAudio 

NAudio est une bibliothèque qui permet de gérer avec C# les sons sur Windows. 
Vous voulez enregistrer les sons à partir de votre propre script ? C'est la bibliothèque que vous allez devoir utiliser.

Exemple :
- Écouter aux volumes d'un jeu : [GitHub Repo](https://github.com/EloiStree/2022_04_29_ListenToMixerForVolume)
- Vidéo YouTube sur comment coder un enregistreur : [GitHub Issue](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/15)

> Note : Je n'ai pas réussi à le faire en Python à partir de ChatGPT... Car il y a trop de code open source écoutant le micro... (-__-' ) L'IA finit toujours par croire qu'elle nous donne le bon exemple mais se trompe.

---

## Note : Enregistrement Xbox

Si vous désirez enregistrer des sessions de jeux PlayStation et Xbox, vous pouvez acheter des cartes de capture comme la MiraBox. Cela permet de "hacker" l'HDMI pour voir la sortie vidéo sur votre PC et donc dans OBS.
[MiraBox](https://www.amazon.com.be/-/en/gp/product/B07G84G7VF/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a9feee1a-77c4-46a0-960e-a8f1b0559eca)

## Note : AverMedia
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/851a3633-0651-4246-baab-194a847c4b40)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/ccfb3ac5-6789-4c65-a337-167516bcbdf3)

## Note : FFMPEG

Ce code au format exe pour console est un incontournable de l'industrie, mais trop compliqué à expliquer pour ce cours. Je veux du moins en parler.


