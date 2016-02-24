import pydrive
from os import path
import argparse


class GDrive(object):

    """A utiliity for interfacing with google drive"""

    def __init__(self):
        default_settings = path.expanduser(
            path.join('~', 'Box Sync', 'oauth_configs', 'gdrive_settings.yaml'))
        self.auth = self.authenticate(settings_file=default_settings)
        self.drive = pydrive.drive.GoogleDrive(self.auth)

    def authenticate(self, settings_file):
        gauth = pydrive.auth.GoogleAuth(settings_file=settings_file)
        gauth.LocalWebserverAuth()
        return gauth

    def upload_file(self, filename):
        file = self.drive.CreateFile()
        file.SetContentFile(filename)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="path of file to upload", type=str)
    arg_vals = parser.parse_args(args)

    gdrive = GDrive()
    gdrive.upload_file(arg_vals.filename)
