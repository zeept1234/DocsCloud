import json

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

if __name__ == "__main__":
    redefine_tooltip()