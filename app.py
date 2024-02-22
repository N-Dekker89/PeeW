import argparse

from classes.crypto import Encryption
from classes.passwords import Passwords
from classes.vault import Vault

enc = Encryption()
pw = Passwords()
vault = Vault()

key = enc.generate_key("Xn52Zn12")
new_pass = pw.generate_password()
print(new_pass)
password = enc.encrypt_password(new_pass, key)
print(password)
dec_pass = enc.decrypt_password(password, key)
print(dec_pass)

# service = "gmail"
# username = "nickd89"
# new_pass = pw.generate_password()
# password = enc.encrypt_password(new_pass, key)
# vault.add_entry(service, username, password)
# entry = vault.get_entry("gmail")
# test = entry[1]
# dec_pass = enc.decrypt_password(test, key)
# print(new_pass)
# print(dec_pass)


# parser = argparse.ArgumentParser(description="A simple command-line password manager")
# parser.add_argument(
#     "-g", "--generate_key", type=str, help="generate a new master password"
# )
# parser.add_argument(
#     "-k",
#     "--key",
#     type=str,
#     help="master password used to encrypt/decrypt your passwords.",
# )
# parser.add_argument("-e", "--encrypt", type=str, help="encrypt a password")
# parser.add_argument("-d", "--decrypt", type=str, help="decrypt a password")
# args = parser.parse_args()

# if __name__ == "__main__":
#     if args.generate_key:
#         key = enc.generate_key(args.generate_key)
#         print(key.decode())
#     elif args.key and args.encrypt:
#         encrypted_message = enc.encrypt_message(args.encrypt, args.key.encode())
#         print(encrypted_message.decode())
#     elif args.key and args.decrypt:
#         decrypted_message = enc.decrypt_message(args.decrypt, args.key.encode())
#         print(decrypted_message)
