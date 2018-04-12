def isAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

passphrases = []

with open("day4-input.txt", "r") as passphraseFile:
    passphrases = passphraseFile.readlines()

correctPassphrases = 0

for passphrase in passphrases:
    passwords = passphrase.split()
    passwordsSet = set(passwords)

    if len(passwords) == len(passwordsSet):
        correctPassphrases += 1

print("Number of correct passphrases (part 1): {}".format(correctPassphrases))

correctPassphrases = 0
for passphrase in passphrases:
    hasAnagram = False
    passwords = passphrase.split()

    for mainPasswordIndex in range(0, len(passwords)):
        mainPassword = passwords[mainPasswordIndex]

        for comparingPasswordIndex in range(0, len(passwords)):
            if mainPasswordIndex != comparingPasswordIndex:
                comparingPassword = passwords[comparingPasswordIndex]
                hasAnagram = hasAnagram or isAnagram(mainPassword, comparingPassword)

    if not hasAnagram:
        correctPassphrases += 1

print("Number of correct passphrases (part 2): {}".format(correctPassphrases))
