#!/usr/bin/python3
import gnupg
import os
from rich import print
from tkinter import * 

def runGen():
    entry_text = eingabe.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zu erst eine E-Mail Adresse ein!")
    else:
        email = entry_text
        id = email.split('@')
        pw = id[0] + "1"



        key_input_data  = gpg.gen_key_input(
            name_real = id[0],
            name_email = email,
            passphrase = pw,
            key_type = 'RSA',
            key_length = 4096
        )

        key = gpg.gen_key(key_input_data)

        pw_label.config(text="Passwort: " + pw)
        fingerprint_label.config(text="Fingerabdruck: " + key.fingerprint)

        print("[red]Passphrase:[/red] " + pw)
        print("[yellow]Fingerprint:[/yellow] " + key.fingerprint)
        ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
        ascii_armored_private_keys = gpg.export_keys(
            keyids=key.fingerprint,
            passphrase=pw,
            secret=True,
        )
        os.mkdir(id[0])
        pub = open(id[0] + "/public-" + id[0] + ".asc", "a")
        pub.write(ascii_armored_public_keys)
        pub.close()
        pri = open(id[0] +"/private-" + id[0] + ".asc", "a")
        pri.write(ascii_armored_private_keys)
        pri.close()

        welcome_label.config(text="Fertig")
        print("[bold green]Done[/bold green]")

fenster = Tk()
fenster.title("PGP Schlüssel Generator")


gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'

my_label = Label(fenster, text="Gib eine E-Mail Adresse ein: ")
eingabe = Entry(fenster, bd=5, width=40 )
welcome_label = Label(fenster)
fingerprint_label = Label(fenster)
pw_label = Label(fenster)

go_button = Button(fenster, text="Go", command=runGen)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

my_label.grid(row = 0, column = 0)
eingabe.grid(row = 0, column = 1)
go_button.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1)
welcome_label.grid(row = 5, column = 0, columnspan = 2)
fingerprint_label.grid(row = 4, column = 0, columnspan = 2)
pw_label.grid(row = 3, column = 0, columnspan = 2)

mainloop()