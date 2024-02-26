from time import sleep
from typing import Annotated

import typer
from rich.console import Console
from rich.progress import Progress

from classes.crypto import Encryption
from classes.passwords import Passwords
from classes.vault import Vault

enc = Encryption()
pw = Passwords()
vault = Vault()
console = Console()
app = typer.Typer(
    add_completion=False,
    name="PeeW",
    help="PeeW is a simple command-line password manager written in Python",
)


@app.command(short_help="Generate an encryption key")
def generate(password: str):
    with Progress() as progress:
        task = progress.add_task("[green]Generating key...", total=50, start=False)
        key = enc.generate_key(password)
        progress.start_task(task)
        while not progress.finished:
            progress.update(task, advance=1)
            sleep(0.02)
    console.print(
        f"[bold yellow]Your key is[/bold yellow]: [bold white]{key.decode()}[/bold white]\n[bold red]Save it somewhere secure![/bold red]"
    )


@app.command(short_help="Store credentials in the vault")
def store(
    key: Annotated[str, typer.Argument()],
    service: Annotated[str, typer.Argument()],
    username: Annotated[str, typer.Argument()],
):
    password = pw.generate_password()
    enc_pass = enc.encrypt_password(password, key)
    vault.add_entry(service, username, enc_pass)
    console.print(
        f"[bold yellow]SERV[/bold yellow]: [bold white]{service}[/bold white]\n[bold yellow]USER[/bold yellow]: [bold white]{username}[/bold white]\n[bold yellow]PASS[/bold yellow]: [bold white]{password}[/bold white]\n[bold yellow]Data has been stored in the vault[/bold yellow]"
    )


@app.command(short_help="Retrieve credentials from the vault")
def retrieve(key: str, service: str):
    entry = vault.get_entry(service)
    dec_pass = enc.decrypt_password(entry[1], key)
    console.print(
        f"[bold yellow]SERV[/bold yellow]: [bold white]{service}[/bold white]\n[bold yellow]USER[/bold yellow]: [bold white]{entry[0]}[/bold white]\n[bold yellow]PASS[/bold yellow]: [bold white]{dec_pass}[/bold white]"
    )


if __name__ == "__main__":
    app()
