import argparse
import typer
from rich.console import Console
from rich.table import Table

from classes.crypto import Encryption
from classes.passwords import Passwords
from classes.vault import Vault

enc = Encryption()
pw = Passwords()
vault = Vault()
console = Console()
app = typer.Typer()


@app.command(short_help="Generate a new key")
def generate_key(password: str):
    key = enc.generate_key(password)
    console.print(f"Your new key is: {key.decode()}")


@app.command(short_help="Generate a strong password 32 characters in length")
def generate_password():
    password = pw.generate_password()
    console.print(f"Your new password is: {password}")


@app.command(
    short_help="Generate a strong password 32 characters in length and save it to the Vault"
)
def save(key: str, service: str, username: str):
    password = pw.generate_password()
    enc_pass = enc.encrypt_password(password, key)
    vault.add_entry(service, username, enc_pass)
    console.print(f"Password: {password}\nYour password has been added to the Vault")


@app.command(short_help="Retrieve a password from the Vault")
def retrieve(key: str, service: str):
    entry = vault.get_entry(service)
    dec_pass = enc.decrypt_password(entry[1], key)
    console.print(f"Service: {entry[0]}\nPassword: {dec_pass}")


if __name__ == "__main__":
    app()

# --- WORKING EXAMPLE ---
# new_pass = pw.generate_password()
# password = enc.encrypt_password(new_pass, key)
# service = "gmail"
# username = "nickd89"
# vault.add_entry(service, username, password)
# entry = vault.get_entry("gmail")
# dec_pass = enc.decrypt_password(entry[1], key)
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
