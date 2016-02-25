from gdrive import gdrive
from mock import patch
from os import path
import pytest

# @pytest.mark.xfail
@patch('gdrive.gdrive.GDrive.set_filename')
@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_basic_file_upload(mockAuth, mockDrive, mockSetName):
    # When command line called with a file
    filename = 'myfile'
    file_path = 'inputs/{}.xlsx'.format(filename)
    gdrive.parse_args([file_path])
    # Authenticator called with settings file in box folder
    exp_file = path.expanduser(
        path.join('~', 'Box Sync',
                  'oauth_configs', 'gdrive_settings.yaml'))
    mockAuth.assert_called_with(
        settings_file=exp_file)
    # Create file called
    assert mockDrive().CreateFile.called
    # SetContentFile called with input file
    mockDrive().CreateFile().SetContentFile.assert_called_with(file_path)
    # Title of file is myfile
    assert mockSetName.called
    # Upload is called on file
