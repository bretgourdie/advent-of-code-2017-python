passphrases = []

with open("day4-input.txt", "r") as passphraseFile:
    passphrases = passphraseFile.readlines()

correctPassphrases = 0

for passphrase in passphrases:
    passwords = passphrase.split()
    passwordsSet = set(passwords)

    if len(passwords) == len(passwordsSet):
        correctPassphrases += 1

print("Number of correct passphrases: {}".format(correctPassphrases))
