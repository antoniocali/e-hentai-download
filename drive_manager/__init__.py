from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os.path import join
from os import getcwd
from pathlib import Path
credentials = "secrets.json"


def upload_file(filename: str, local_file: str, folder_id: str) -> bool:
    print(f"Uploading file {local_file}")
    try:
        gauth = GoogleAuth()
        file = Path(join(getcwd(), credentials))
        file.touch(exist_ok=True)
        gauth.LoadCredentialsFile(credentials)
        if gauth.credentials is None:
            gauth.GetFlow()
            gauth.flow.params.update({'access_type': 'offline'})
            gauth.flow.params.update({'approval_prompt': 'force'})
            gauth.LocalWebserverAuth()
            gauth.SaveCredentialsFile(credentials)
        elif gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(credentials)
        else:
            gauth.Authorize()
            gauth.SaveCredentialsFile(credentials)
        drive = GoogleDrive(gauth)
        gfile = drive.CreateFile({'parents': [{'id': folder_id}], 'title': filename})
        gfile.SetContentFile(local_file)
        gfile.Upload()
        print(f"File Uploaded {local_file}")
        return True
    except Exception as e:
        print("ERROR", e)
        return False
