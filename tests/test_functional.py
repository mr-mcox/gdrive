from gdrive import gdrive

def test_basic_file_upload():
    #When command line called with a file
    gdrive.parse_args(['inputs/myfile.xlsx'])
    #Authenticator called with settings file in yaml folder
    #SetContentFile called with input file
    #Title of file is myfile
    #Upload is called on file