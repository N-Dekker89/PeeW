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
