# Bot automatizare mesaje

## Dependinte
1. Rularea intr-un mediu LINUX

2. Urmatoarele bibliotecii pentru `Python`

```bash
$ pip3 install pywhatkit    # API mesageria WhatsApp
$ pip3 install discord      # API mesageria Discord
$ pip3 install asyncio
$ pip3 install datetime

$ # verificare:
$ pip3 freeze
```


3. Din cauza faptului ca este o idee total gresita din punctul de vedere al securatatii
sa hardcodam parole, numerele de tolefon, ID-uri si token-uri
(acestea fiind informatii sensibile, de altfel), am ales sa stochez aceste 
date folosind
`variabile de mediu`.
Acestea vor fi ulterior accesate in cod folosind functia `getenv` a modului `os`.


Este nevoie sa deschidem fisierul de configuratii al `bash`-ului (sau al `shell`-ului curent) si sa exportam aceste variabile.


```bash
$ nano -l ~/.bashrc     # deschidem fisierul si inseram urm linii la final

# variabile de mediu pentru bot discord
export MY_DAILY_DISCORD_BOT_INVITATION_LINK=''
export MY_DISCORD_DAILY_MESSENGER_BOT_TOKEN=''
export MY_DISCORD_DAILY_SERVER_ID=''
export MY_DISCORD_DAILY_CHANNEL_ID=''
export MY_DISCORD_DAILY_USERNAME=''
export MY_DISCORD_DAILY_USER_ID=''
export MY_PHONE_NUMBER=''       # pentru WhatsApp

CTRL+S
CTRL+X

$ source ~/.bashrc
$ reset
$ env | grep 'DISCORD'
$ env | grep 'PHONE_NUMBER'
```



## Algoritm
`Bot`-ul de Python ruleaza in mod asincron, verificand la fiecare minut
daca urmeaza o actiunea / un eveniment important. In caz ca da, va trimite
pe `Discord` un mesaj sugestiv.



## Rulare
```bash
$ python3 main.py       # va afisa toate informatiile conexilor

$ chmod +x main.py
$ ./main --silent
```


## Bug
Este scris si cod pentru a trimite un text pe `WhatsApp`,
doar ca intampina problema la trimiterea efectiva.


## 24/7
Pentru ca `bot`-ul sa functioneze fara problemele la orice ora din zi si din naopte,
este nevoie 

