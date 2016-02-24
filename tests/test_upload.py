from gdrive import gdrive
from mock import patch


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_file_creation(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    gd.upload_file('file.xlsx')
    assert mockDrive().CreateFile.called


@patch('pydrive.drive.GoogleDrive')
@patch('pydrive.auth.GoogleAuth')
def test_content_set(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    filename1 = 'file.xlsx'
    filename2 = 'file2.xlsx'
    gd.upload_file(filename1)
    mockDrive().CreateFile().SetContentFile.assert_called_with(filename1)

    gd.upload_file(filename2)
    mockDrive().CreateFile().SetContentFile.assert_called_with(filename2)
