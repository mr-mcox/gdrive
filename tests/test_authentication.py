from gdrive import gdrive
from mock import patch


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_authentication_call_settings(mockAuth, mockDrive):
    gdrive.GDrive().authenticate('setttings.yaml')
    mockAuth.assert_called_with(settings_file='setttings.yaml')


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_local_server_called(mockAuth, mockDrive):
    gdrive.GDrive().authenticate('setttings.yaml')
    assert mockAuth().LocalWebserverAuth.called


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_drive_creation(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    mockDrive.assert_called_with(gd.auth)
    assert gd.drive == mockDrive()
