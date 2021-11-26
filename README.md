# PythonPGPKeyGeneration

Public and Privat key generation with python_gnupg

## Installation des Python GPG Schlüssel Generator(Linux) 

Folgen Dependencies müssen installiert sein damit das Programm funktioniert 
```
sudo apt install python3  

sudo apt install pip3 

pip3 install python-gnupg 

sudo apt-get install gpa 

export GPG_TTY='('tty')' 

sudo apt-get install gnupg2 
```

Mit dem Folgen Befehl wird bestätigt, dass das Paket gpg im Ordner /usr/bin/gpg liegt. 
```
which gpg  

Output: /usr/bin/gpg 
```
Das Skript wird im nächsten Schritt über den git clone Befehl heruntergeladen. 
```
git clone https://github.com/jontok/OSP_KeyGen.git 
```
 ## Einzel Schlüssel Generation 

Navigieren sie Lokal oder via SecureShell in das OSP_KeyGen-Verzeichnis und führen die den folgenden Befehl im Terminal aus ```./genpgp_input.py ```

 

Folgen sie den Anweisungen und geben sie die E-Mail Adresse des/der SchülerInn oder des/der LehrerInn in die Konsole ein. 

 

 

 

 

Die Ausgabe der Konsole beinhaltet das Passwort und den Fingerabdruck für die generierten Key-Files.  

 

 

## Multi Schlüssel Generation 

Es können auch direkt mehrere Schlüssel erstellt werden. Dafür muss eine Liste mit im .txt Format angelegt werden die wie Folgt aussieht: 

 

Im Anschluss muss die Datei im Verzeichnis OSP_KeyGen/ abgelegt. 

 

Danach kann der Befehl ```./genpgp_list.py``` in der Konsole ausgeführt werden. 

In dem Dialog wird dann der Name der Datei eingefügt und mit der Enter-taste bestätigt. Damit werden die Schlüssel generiert. Die Passwörter und Fingerabdrücke werden jeweils in der Konsole ausgegeben. 

 

 

 

 

 

 

## Datei Ablage 

Die Key Files befinden sich unter OSP_KeyGen/username/ und sind jeweils benannt mit 

private-username.asc und public-username.asc 

 

 

 

Verteilung der Schlüssel 

Die Schlüssel können in dem entsprechenden Ordner an die Benutzer verteilt werden. 
