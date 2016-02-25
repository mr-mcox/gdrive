from gdrive import gdrive
from mock import patch, MagicMock
import pytest


@patch('gdrive.gdrive.GoogleDrive')
@patch('gdrive.gdrive.GoogleAuth')
@pytest.fixture
def proto_file(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    gf = gdrive.GFile(gd)
    return gf


@pytest.fixture
def gfile(proto_file):
    proto_file._file = MagicMock()
    return proto_file


@pytest.fixture
def gfile_dict(proto_file):
    proto_file._file = dict()
    return proto_file


@patch('gdrive.gdrive.GoogleDrive')
@patch('gdrive.gdrive.GoogleAuth')
def test_file_creation(mockAuth, mockDrive):
    gd = gdrive.GDrive()
    gdrive.GFile(gd)
    assert mockDrive().CreateFile.called


def test_content_set(gfile):
    filename1 = 'file.xlsx'
    filename2 = 'file2.xlsx'
    gfile.upload_file(filename1)
    gfile._file.SetContentFile.assert_called_with(filename1)

    gfile.upload_file(filename2)
    gfile._file.SetContentFile.assert_called_with(filename2)


def test_set_filename(gfile_dict):

    gfile_dict.set_filename('../input/thefile.xlsx')
    assert gfile_dict._file['title'] == 'thefile'

    gfile_dict.set_filename('../input/thefile2.xlsx')
    assert gfile_dict._file['title'] == 'thefile2'


@patch('gdrive.gdrive.GFile.set_filename')
def test_set_name_on_upload(mockSetName, gfile):
    gfile.upload_file('../input/thefile.xlsx')

    mockSetName.assert_called_with('../input/thefile.xlsx')


def test_call_upload_on_upload(gfile):
    gfile.upload_file('../input/thefile.xlsx')

    gfile._file.Upload.assert_called_with({'convert': True})
