from docs_functions import * #ADD " - " to tooltip_functions redefine
from codec_functions import *
from tooltip_functions import *
import keyboard
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from rich import print
from time import sleep

def get_user_choice():
    tooltip_1 = get_tooltip(1)
    tooltip_2 = get_tooltip(2)
    tooltip_4 = get_tooltip(4)
    print(f"[cyan]Choose action:\n1. Upload{tooltip_1}\n2. Download{tooltip_2}\n3. Exit program\n{tooltip_4}Press number to perform action.")

def action():
    console = Console()
    upload_spinner = Spinner("dots", text="[bold green]Uploading...")
    download_spinner = Spinner("dots", text="[bold green]Downloading...")
    exit_spinner = Spinner("dots", text="[bold red]Exiting...")
    clear()
    get_user_choice()
    tooltip = get_tooltip(4)
    while True:
        keyboard.block_key("1")
        keyboard.block_key("2")
        keyboard.block_key("3")
        keyboard.block_key("4")
        if keyboard.is_pressed("1"):
            keyboard.unhook_all()
            with Live(upload_spinner, refresh_per_second=10):
                encode_upload()
            clear()
            with Live("[bold blue]Finished uploading!", console=console, refresh_per_second=10):
                sleep(2)
            action()
        elif keyboard.is_pressed("2"):
            keyboard.unhook_all()
            batch = download_get_batch()
            with Live(download_spinner, refresh_per_second=10):
                finish_download = download_decode(batch)
            clear()
            with Live(f"[bold blue]{finish_download}", console=console, refresh_per_second=10):
                sleep(2)
            action()
        elif keyboard.is_pressed("3") or keyboard.is_pressed("esc"):
            keyboard.unhook_all()
            clear()
            with Live(exit_spinner, refresh_per_second=10, transient=True):
                kill()
                
        elif keyboard.is_pressed("4") and tooltip != "":
            keyboard.unhook_all
            get_tooltip("hide")
            clear()
            action()
        sleep(0.01)

if __name__ == "__main__":
    action()