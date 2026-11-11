import json, subprocess, time, sys, msvcrt

def get_tooltip(tooltip_num):
    if tooltip_num == "hide":
        with open("config/tooltips.json", "w") as file:
            tooltip_dict = {f"tooltip_1": "", "tooltip_2": "", "tooltip_4": ""}
            json.dump(tooltip_dict, file, indent=4)
            return
    with open("config/tooltips.json", "r") as file:
        tooltip_dict = json.load(file)

    tooltip = tooltip_dict[f'tooltip_{tooltip_num}']
    return tooltip

def redefine_tooltip():
    tooltip_dict = {"tooltip_1": " - Encodes the files in the \"upload/\" folder to base85, then uploads it to google docs.","tooltip_2": " - Downloads the base85 from google docs, decodes it, then puts it in the \"download/\" folder.", "tooltip_4": "4. Do not show tooltips again.\n"}
    with open("config/tooltips.json", "w") as file:
        json.dump(tooltip_dict, file, indent=4)

def clear():
    subprocess.run("cls", shell=True)

def kill():
    time.sleep(1)
    clear()
    time.sleep(0.1)
    sys.exit()

def wait_for_key():
    msvcrt.getch()




        

if __name__ == "__main__":
    redefine_tooltip()