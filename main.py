try:
    from docs_functions import *
    from codec_functions import *
    from utils import *
    import keyboard
    from rich.console import Console
    from rich.live import Live
    from rich.spinner import Spinner
    from rich import print
    from time import sleep
    import subprocess
    from googleapiclient.errors import HttpError
    from google.auth.exceptions import RefreshError
    from google.auth.exceptions import TransportError
except ModuleNotFoundError as error:
    if error.name == "codec_functions" or error.name == "docs_functions" or error.name == "utils":
        print(f'[bold red]Fatal: Missing module. Module: "{error.name}". Program appears corrupted. Try reinstalling.')
        raise SystemExit(1)
    print(f'[bold red]Fatal: Missing module. Module: "{error.name}". Missing dependencies. Are the dependencies installed? Is the venv active? Try checking README.md for installing dependencies.')
    raise SystemExit(1)

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
            with Live(download_spinner, refresh_per_second=10, transient=True) as live:
                finish_download = download_decode(batch)
                if finish_download == "Fail":
                    live.stop()
                    clear()
                    print(f"[bold red]Invalid batch. No document found for batch {batch}.")
                    sleep(2)
                    action()
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
            keyboard.unhook_all()
            get_tooltip("hide")
            clear()
            action()
        sleep(0.01)

def error_pad_action():
    loading_spinner = Spinner("dots", text="[bold green]Resetting...")
    try:
        action()
    except FileNotFoundError as error:
        clear()
        print(f"[bold red]Missing file or folder: {error.filename}. Is token.json or credentials.json missing? Try checking README.md for Google Docs API guide. Try reinstalling.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except NameError:
        clear()
        print("[bold red]Missing function, file or folder. Is the program corrupted? Are the dependencies installed? Try reinstalling.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except KeyboardInterrupt:
        clear()
        print("[bold red]Program exited by user.")
    except ModuleNotFoundError:
        clear()
        print("[bold red]Missing module. Is the program corrupted? Are the dependancies installed? Try reinstalling.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except HttpError as error:
        clear()
        print(f"[bold red]Google error {error.resp.status}. Is the Google Docs API enabled? Does the document exist? Try checking README.md for Google Docs API guide. Try reinstalling.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except RefreshError:
        clear()
        print("[bold red]Google login expired. Delete token.json and run token_setup.py again.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except TransportError:
        clear()
        print("[bold red]Internet error. Try checking your network connection.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except ValueError:
        clear()
        print("[bold red]Is the program corrupted? Try reinstalling.")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    except Exception as error:
        clear()
        print(f"[bold red]An unexpected error occured. Error: {error}. Exception type: {type(error).__name__}")
        print(f"[italic magenta]Press any key to contine...")
        wait_for_key()
        with Live(loading_spinner, refresh_per_second=10, transient=True):
            sleep(0.5)
        error_pad_action()
    

if __name__ == "__main__":
    action()