from gdrive import gdrive
from unittest.mock import patch


@patch('gdrive.gdrive.GoogleDrive')
@patch('gdrive.gdrive.GoogleAuth')
def test_authentication_call_settings(mockAuth, mockDrive):
    gdrive.GDrive().authenticate('setttings.yaml')
    mockAuth.assert_called_with(settings_file='setttings.yaml')


@patch('gdrive.gdrive.GoogleDrive')
@patch('gdrive.gdrive.GoogleAuth')
def test_local_server_called(mockAuth, mockDrive):
    gdrive.GDrive().authenticate('setttings.yaml')
    assert mockAuth().LocalWebserverAuth.called


@patch('gdrive.gdrive.GoogleDrive')
@patch('gdrive.gdrive.GoogleAuth')
def test_drive_creation(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    mockDrive.assert_called_with(gd.auth)
    assert gd.drive == mockDrive()
