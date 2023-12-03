Salut à tous.

En tant que testeur vous allez devoir écrire des rapports.
Mais vous allez aussi devoir enregistrer: des vidéos, des captures d'écran et du son.

Il y a de nombreuses façon de faire.
Pour cette atelier je vais vous montrer une façon de faire.

Durant cette atelier je vous ai apporté des casques de réalité virtuelle tournant sur Android.



## Step by step
Allons y étape par étape, il y a beaucoup à installer et de travail à se familiarizer.

### OBS: Open Broadcast Software
 
[Download OBS et OBS Portable](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/8)

OBS est un outil qui va vous permettre de faire de l'enregistrement vidéo. 
C'est outil est parfait et Open Source. 



Si vous enregistré la video, n'oublier pas de choisir un emplacement adhéquoi:
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/fe8316ce-0b57-4a9b-9ca9-b23c73847885)

https://www.youtube.com/results?search_query=commencer+sur+obs


#### Shortcut

Comme nous notre but c'est de créé des outils qui permet de se facilité la vie.
On va aller définir des macros dans OBS et utiliser c'est macro depuis python pour lancer l'enregistrement.
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/22915316-42fb-46fc-bfbd-f555f6722a91)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/5dae7ac3-0645-4cab-b0d1-c961fe78cc77)

Shortcut, Example: 
CTRL+Shit+ALT+ Arrow Left = Start recording
CTRL+Shit+ALT+ Arrow Right = Stop recording
CTRL+Shit+ALT+ Arrow Up = Screenshot


#### Websocket

C'est bien beau de hacker les touches pour lancer un enregistrement... Mais il y aurais pas plus direct ? Un API ?
Depuis OBS 28, il y a la possibilité de lancer un Websocket pour controller OBS :) !!!

Cela permet de prendre le control de ce que l'on veut afficher et de changer à la volé l'outil par le réseaux.
Info: https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/21
Par example depuis [Streamer.bot](https://streamer.bot) ou depuis son navigateur web: [http://obs-web.niek.tv](http://obs-web.niek.tv)  
Pour les plus guerriers d'entre vous:  
https://websocketking.com  

Et comme on a fait du python... Vous devinez pourquoi je vous en parle ;) 
https://github.com/Elektordi/obs-websocket-py


Vous pouvez le paramettrer en lancant OBS:  
`D:\OBS Video>OBSPortable.exe --portable --websocket_port 4545 --websocket_password HelloWorld --websocket_debug --websocket_ipv4_only`  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/57793bff-94c0-491e-9d92-80ec955a7c6f)


### SCRCPY: Screen copy ( & ADB )
Nous allons un peu explorer comment enregistrer votre écran de téléphone et chipoter avec.

#### Mode développeur
Avant de pouvoir "jouer" avec son téléphone, il faut lui permettre d'être débugger par USB et optionnellement d'installer de source inconnue. Pour ça il faut passer votre téléphone en mode développeur.
L'idée reste la même mais est différent sur tout les téléphones android:
https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/30
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
All keycode: https://developer.android.com/reference/android/view/KeyEvent

Ouvrir la page des paramètres
`adb shell am start -a android.settings.SETTINGS`

Ouvrir une page web
`adb shell am start -a android.intent.action.VIEW -d "http://www.example.com"`

Lancer le playstore
`adb shell am start -a android.intent.action.VIEW -d "market://details?id=com.android.vending"`

Capture d'écran;
`adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png`
`adb exec-out screencap -p > screen.png`

Start /Stop recording on the device:
`adb shell screenrecord /sdcard/yourfilename.mp4`
`adb shell pkill -l 15 -f /system/bin/screenrecord`
`adb pull /sdcard/yourfilename.mp4`

Ne pas utiliser de cable  ?

`adb tcpip 5555`
`adb shell ip -f inet addr show wlan0`
`adb connect adresse_ip_du_telephone:5555`


Essayé de deviner ce que fait le script suivant:

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


##### By Side Quest

Il y a des centaines de commandes et l'une dans l'autres, il y a des milliers de combinaison.
C'est la raison pour laquel il existe des "wrapper"/ des emballagues.
Des logiciels dont le but n'est pas de créé mais de proposer un interface pour utiliser ADB.
Comme SideQuest qui permet de facilement utiliser ADB avec les casques VR 

Download: https://sidequestvr.com/setup-howto
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/2da8ccfd-2989-42e2-89eb-92a113e12a0c)






### Le sons
- https://spectrogram.sciencemusic.org
- C'est quoi le son ? https://youtu.be/24yESm63tSY
[![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/dd320a9c-c51c-459b-9614-e286ffc3921f)](https://youtu.be/24yESm63tSY)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a8f2b87b-4508-42bf-80e3-c579c361e44a)https://youtu.be/24yESm63tSY?t=220 
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/3f5b493f-35e8-4ebc-beab-8cfa0d85bc12)https://youtu.be/24yESm63tSY?t=360
440 Hz (number of frequence per seconds)

What is a spectrogram ?   
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/b8f92205-45f5-446e-90b4-564bef17ae4e)  
https://youtu.be/_FatxGN3vAM


### VoiceMeeter
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/c3e1d4b2-1aeb-46cf-8f85-acde2b32701b)


### OBS: Hack to redirect audio

OBS n'a pas d'enregistreur audio. Il est construit pour la video.
Mais il a beaucoup d'option sur l'audio, dont le fait de rediriger le son pour "monitorer" la qualité du stream.
C'est que l'on va utiliser avec Voice Meeter pour permettre d'enregistrer le son de nos tests.
Attention de désactiver le Ducking (décaler le son pour debugger le son du stream)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a6fe84fa-b815-4d79-bc8c-c5a0bef0a1ec)

Il faut aussi mettre l'option "Ouput Mode" en avancé et vous pouvez augmenter le bitrate de l'audio:
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/d40f9b3f-752c-45a6-9efa-e8110c0aaa30)




#### Window Recorder (Sound recorder)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/d526782e-1681-46be-b2bb-97ab45cff946)

![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/c63fb874-fdee-4f17-b459-40acdf8e8915)
Shortcut: 
- CTRL+ R : Record
- Escape : Stop Recording
- Space : Pause Recording

Cette application enregistre les entrées sons.  
Mais par Voice Meeter, nous avons à notre disposition une entrée son.  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/adc2fe02-858f-41f0-b93e-1352222e8121)


#### Audacity
 [Download](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/9) 

Audacity est la meilleur application open source que je connais pour editer du son.  
Elle permet aussi d'en enregistré, mais comme la procédure d'exporter le son n'est pas facile à automatiser avec SendMessage.
On ne vas pas l'utiliser pour enregistré.    
Mais vous en aurez besoin pour "trimmer" et retravailler le son au besoin.  
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/cc19a6e7-260e-4441-abbe-c88108dadcde)

Shortcut: 
- Ctrl + Shit + E   500> Enter 500> Enter 500> Enter = Exporter le son
- Ctrl+ A  500> Enter 500> Enter = Supprimer toute la piste






-------------------------------------

## Note: Record Xbox

Si vous désirez enregistré des playsations et Xbox, vous pouvez acheter des cartes de captures comme la MiraBox qui permet de hacker l'HDMI pour le voir comment entrée vidéo sur votre PC et donc dans OBS.
[MiraBox](https://www.amazon.com.be/-/en/gp/product/B07G84G7VF/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/a9feee1a-77c4-46a0-960e-a8f1b0559eca)


## Note: AverMedia
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/851a3633-0651-4246-baab-194a847c4b40)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/ccfb3ac5-6789-4c65-a337-167516bcbdf3)



## Note: FFMPEG

Ce code en format exe pour console est un incontournable de l'industrie mais trop complique à expliquer pour ce cours.
Je veux du moins en parler.



 
-------------------------

