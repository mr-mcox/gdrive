from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import path
import argparse
import re
import sys


class GDrive(object):

    """A utiliity for interfacing with google drive"""

    def __init__(self):
        def_path = path.join('~',
                             'Box Sync',
                             'oauth_configs',
                             'gdrive_settings.yaml')
        default_settings = path.expanduser(def_path)
        self.auth = self.authenticate(settings_file=default_settings)
        self.drive = GoogleDrive(self.auth)

    def authenticate(self, settings_file):
        gauth = GoogleAuth(settings_file=settings_file)
        gauth.LocalWebserverAuth()
        return gauth


class GFile(object):

    """A class managing google files"""

    def __init__(self, gdrive):
        self._file = gdrive.drive.CreateFile()

    def upload_file(self, file_path):
        self._file.SetContentFile(file_path)
        self.set_filename(file_path)
        self._file.Upload({'convert': True})

    def set_filename(self, file_path):
        self._file['title'] = re.search(
            '(.*)\..+', path.basename(file_path)).group(1)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="path of file to upload", type=str)
    arg_vals = parser.parse_args(args)

    gdrive = GDrive()
    gfile = GFile(gdrive)
    gfile.upload_file(arg_vals.filename)

if __name__ == '__main__':
    parse_args(sys.argv[1:])
