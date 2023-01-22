import hashlib


def crackHash(inputPass):
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find the file.")

        for password in passFile:
            encPass = password.encode("utf-8")
            digest = hashlib.md5(encPass.strip()).hexdigest()
            if digest == inputPass:
                print("Password found : " + password)

if __name__ == '__main__' :
    crackHash("1a1dc91c907325c69271ddf0c944bc72")