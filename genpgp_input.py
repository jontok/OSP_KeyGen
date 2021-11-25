#!/usr/bin/python3
import gnupg
import os


gpg = gnupg.GPG('/usr/bin/gpg')
gpg.encoding = 'utf-8'

email = input("Enter the e-Mail address: ")
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

print("Passphrase: " + pw)
print("Fingerprint: " + key.fingerprint)
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

print("Done")