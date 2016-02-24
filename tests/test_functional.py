from gdrive import gdrive
from mock import patch
from os import path
import pytest

# @pytest.mark.xfail


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_basic_file_upload(mockAuth, mockDrive):
    # When command line called with a file
    filename = 'inputs/myfile.xlsx'
    gdrive.parse_args([filename])
    # Authenticator called with settings file in box folder
    exp_file = path.expanduser(
        path.join('~', 'Box Sync',
                  'oauth_configs', 'gdrive_settings.yaml'))
    mockAuth.assert_called_with(
        settings_file=exp_file)
    # Create file called
    assert mockDrive().CreateFile.called
    # SetContentFile called with input file
    mockDrive().CreateFile().SetContentFile.assert_called_with(filename)
    # Title of file is myfile

    # Upload is called on file
