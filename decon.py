import base64
import hashlib
from time import sleep
import pyfiglet

print("\n"+"*"*65)
print(pyfiglet.figlet_format("                 DECON"))
print("*\t\t\tBy Nibil Mathew\t\t\t\t*")
print("*\t\t\tgithub:explo1ter\t\t\t*")
print("\n"+"*"*65)


def encrypt_b64():
    user_pass = input("Enter the string to encrypt : ")
    print("\nEncrypting your string.....\n")
    sleep(1)
    b64_pass = base64.b64encode(user_pass.encode())
    print(f"Your encoded string : {b64_pass}")

def decrypt_b64():
    b64hash = input("Enter the base 64 hashed format : ")
    print("\nDecrypting your string....\n")
    sleep(1)
    dec_data = base64.b64decode(b64hash)
    print(f"Decoded format : {dec_data}")

def encrypt_md5():
    md5_raw = input("Enter the string to encrypt : ")
    md5_obj = hashlib.md5(md5_raw.encode())
    md5_hash = md5_obj.hexdigest()
    print("Encrypting the string....")
    sleep(1)
    print(f"Encrypted string : {md5_hash}")

def decrypt_md5():
    f = False
    md5_hash = input("Enter the md5 string to decrypt : ")

    wordlist = input("Enter the wordlist(complete path should be mentioned) : ")
    try:
        wlist = open(wordlist, "r")
    except:
        print("wordlist not found")
        decrypt_md5()
    print("Wordlist found")
    try:
        for word in wlist:
            stripped_hash = word.strip()
            if(hashlib.md5(stripped_hash.encode()).hexdigest() == md5_hash):
                f = True
                print(f"\nDecrypted!!\nDecoded string : {word}")
                break
    except:
        if f == False:
            print("Decoding failed\nuse another wordlist")


choice = 0
while choice != 4:
    print("\n**********MENU***********\n\n1.Base64\n2.MD5\n3.Exit")
    choice =int(input("Enter your choice : "))
    if choice == 1:
        option = 0
        while option != 4:
            print("\n*******Base64******\n1.Encryptor\n2.Decryptor\n3.Back")
            option = int(input("Enter your option : "))
            if option == 1:
                encrypt_b64()
            elif option == 2:
                decrypt_b64()
            elif option == 3:
                break
            else:
                print("invalid choice")

    elif choice == 2:
        option = 0
        while option != 4:
            print("\n*******md5******\n1.Encryptor\n2.Decryptor\n3.Back")
            option = int(input("Enter your option : "))
            if option == 1:
                encrypt_md5()
            elif option == 2:
                decrypt_md5()
            elif option == 3:
                break
            else:
                print("invalid choice")
    elif choice == 3:
        print("\nExiting\nThankYou use again :)")
        exit(0)
    else:
        print("Invalid choice")

