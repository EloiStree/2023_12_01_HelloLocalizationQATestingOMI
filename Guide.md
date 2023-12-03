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


#### SCRCPY
Pour pouvoir enregistré ce qui se passe sur votre téléphone Android ou sur votre casque de réalité virtuelle Android.
Vous allez devoir utiliser SCRCPY qui est un project open source qui permet de communiquer avec les flux vidéos du téléphone.

ADB: Android Debug Bridge est un autre outil qui est dans SCRCPY qui permet de communiquer avec votre téléphone.

[Download](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/issues/4)
![image](https://github.com/EloiStree/2023_12_01_HelloLocalizationQATestingOMI/assets/20149493/e63d1121-6436-4963-8752-e9671005e07f)

#### ADB

##### Command Line

##### By Side Quest









### Le sons
- https://spectrogram.sciencemusic.org

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

 
