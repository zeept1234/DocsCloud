# DocsCloud
DocsCloud is a tool used to store images, audio, video or really any file in Google Docs, essentially using Google Docs as your own cloud storage. The purpose of this is to take advantage of a company or schools unlimited Google Docs storage, and use it to our benefit, rather than just storing documents.

## Description
DocsCloud utilises Google Docs as cloud storage, through encoding files into base85. Then, using Google Docs API, the files are sent in a JSON format to a document. This document's ID is saved, and can be accessed in the future.

## Getting Started
### Installation
DocsCloud can be installed through one of two methods:
- Go to "https://github.com/zeept1234/DocsCloud", click releases, and install the zip file. Unzip the file and move the folder to a directory of your choice (e.g. C:/documents/DocsCloud). 
- Alternatively, navigate to a directory of your choice and open a terminal window (right click, click "Terminal" or, open Terminal and run ```cd C:/path/to/whereYouWantYourDocsCloudFolder```). Then, run ```git clone https://github.com/zeept1234/DocsCloud```

### Dependancies
- Windows 11 (should work on windows 10 - not guaranteed)
- Python 3.12+ (https://www.python.org/downloads/)
- Install requirements.txt (see creating a virtual environment and installing dependancies)
- Google API and cloud account (see setting up Google API)
- Git (only if using ```git clone``` https://git-scm.com/install)

#### Creating a Virtual Environment and installing dependancies
1. Run ```python -m venv .venv``` to create a virtual environment named ".venv"
2. Run ```.venv\Scripts\Activate.ps1``` to activate the virtual environment
3. Run ```pip install -r requirements.txt``` to install the requirements for this project

#### Setting up Google API
See "https://developers.google.com/workspace/docs/api/quickstart/python" for a more in depth guide.
1. Access the Google Cloud Console and create a project via "https://console.cloud.google.com/projectcreate". ![Creating a project](assets/create_project.png)
2. Name the project anything, and set organisation to "No organization".
3. Configure the OAuth settings via "https://console.cloud.google.com/auth/branding?project=docscloud-514322".
4. Click "Get started" and fill out "App Information" (It doesn't matter what you put, only you will be using it). ![Setting up branding](assets/branding.png)
5. For "Audience", select "External". For "Contact Information", enter your email. For "Finish", click "I agree", then "continue". Finally, press "Create".
6. Access the clients menu via "https://console.cloud.google.com/auth/clients" or the "Clients" section on the left side of the Google Cloud Console.
7. Click "Create Client". Set "Application type" to "Desktop app" and "Name" to anything ("Name" is only shown to you"). Click "Create".
8. After clicking create, popup should appear. Click "Download JSON" (You may need to scroll down to see it) to download a JSON file, named "client_secret" followed by a string of numbers and letters. Rename this file (without changing the file extension) to "credentials.JSON".
9. Put "credentials.JSON" into the DocsCloud folder.
10. Navigate back to the "Audience" section and click "Add users" (You may need to scroll down to see it). Enter your email (same one as before) and click "Save".
11. Open a terminal in the DocsCloud directory (open the folder, right click, click "Terminal" or, open Terminal and run ```cd C:/path/to/DocsCloud```), then run ```python token_setup.py```. A web page should open, select or sign in to your email (same one as before). If you get a "Google hasn't verified this app" page, click "continue". Then, click "Continue" again to give DocsCloud access to your Google Docs. The page will close and "token.JSON" should appear in the DocsCloud directory
12. Navigate to the "APIs and Services" page of the Google Cloud console via "https://console.cloud.google.com/apis" or the "APIs and Services" button in the "Quick access" of your Google Cloud console project homepage. Click on "Library", located on the left bar.
13. In the search bar, marked "Search for APIs & Services", type "Google Docs API", then click enable.![Google Docs API](assets/Google_Docs_API.png)
12. Google API is now set up.

### Executing the program
Ensure dependencies are installed and Google API is set up before continuing
1. Activate the virtual environment by running ```.venv\Scripts\Activate.ps1``` in a terminal pointing to the DocsCloud directory. The terminal should say ```(.venv) PS C:path/to/DocsCloud>```
2. Run ```python main.py``` to execute "main.py", the terminal should show the DocsCloud main menu.

## Using the program
After executing the program, the main menu should appear. Press the number associated with the action you want to perform. Upload encodes the files in the "upload/" folder, then sends it to Google Docs. Download downloads the files from Google Docs, then decodes it and puts it in the "download/" folder. Exit program exits DocsCloud. Hide tooltips disables tooltips (this only appears if tooltips are visible.)

![Main menu](assets/main_menu.png)

## How it works
### The main menu
The main menu is animated using rich live, spinner and console. The upload option encodes and uploads, while the download function downloads and decodes. Tooltips are saved in a json, and are loaded when the main menu is launched. If "Hide tooltips" is pressed, it clears the json file, and sets all tooltips to be "". The main menu checks if tooltips have a value
### Encoding
DocsCloud encodes via Python's Base64 module, which encodes any files in the "upload/" folder to Base85. This Base85 encoded file is saved to a dictionary, along with the files name and suffix, then saved to a JSON file in "file_properties/".
### Decoding
Like encoding, DocsCloud uses Python's Base64 module, to decode any JSON files in the "file_properties/" folder. It decode's the Base85, saving the text, name and suffix into a dictionary, which is then converted to a readable file in "download/".
### Uploading
DocsCloud utilises the Google Docs API to upload the contents of a JSON in "file_properties/" to Google Docs, in a JSON format. Each JSON file is uploaded one by one, so the program can check if the file will exceed the Google Docs 1,024,000 character limit. If a file will exceed the character limit, a new document is automatically created (unless the individual file is too large for a Google Doc).
### Downloading
Also using the Google Docs API, downloading parses the contents of the Google Docs where the content is uploaded. This Google Docs's ID is saved in a json, associated with the batch in "batch/. This text is broken into chunks of individual files, and saved to "file_propterties/" for encoding.

## Credit and Acknowledgements
To be done.