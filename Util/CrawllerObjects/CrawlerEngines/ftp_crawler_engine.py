import ftplib
import os


def get_file_ftp(ftp, filename):
    with open(filename, 'wb') as ftp_file:
        ftp.retrbinary("RETR " + filename, ftp_file.write,  blocksize=1000000000)


def str_trunc(filename, info=-1, split_format=" "):
    """
    :param filename: denote the name of the file without format for transfer
    :param info: show the position of the array that be create after of parsing in the file
    :return:The info of the parsing(or spliting) that doing in the file, in this case mean array position
    """
    if info is not None:
        return filename.split(split_format)[info]


def is_dir(permission):
    """
    :param permission: is useful for verify if a file is it really file or directory based on linux file system
    :return: True if name is really directory or False in other case
    """
    return permission[0].lower() == 'd'


def classifier_files(files_info):
    """

    :param files_info: Contains the files that be choose by ftp download
    :return: A dict that have contains tha file name and one classification of the file
    """
    ftp_class = {}

    for file in files_info:
        dir_response = str_trunc(file, 0)

        """
        If  a file really be file it will be notation with f else d
        """
        if is_dir(dir_response):
            ftp_class[str_trunc(file)] = 'd'
        else:
            ftp_class[str_trunc(file)] = 'f'

    return ftp_class


def recursive_get(ftp_manager, ftp_location):
    path = str_trunc(ftp_location, info=-1, split_format='/')    # caminho no diretorio do host
    print(path)
    os.mkdir(path)  # cria um dir no host como o mesmo nome do raiz do server ftp
    os.chdir(path)  # desloca o host para esse caminho

    ftp_manager.cwd(ftp_location)   # desloca o server ftp para o dir do inicio do download

    """lista todos os arquivos do diretorio dp server ftp"""
    files_info = []
    ftp_manager.retrlines('LIST', files_info.append)

    "classsifica os arquivos(e dir)  criando um dicionario"
    dir_info = classifier_files(files_info)

    for k, v in dir_info.items():
        if v.lower() == 'f':
            get_file_ftp(ftp_manager, k)
        else:
            recursive_get(ftp_manager, ftp_manager.pwd()+"/"+k)
            ftp_manager.cwd("../")
            os.chdir("../")

#
# if __name__ == 'main':
# f = ftplib.FTP("ftp.ebi.ac.uk")
# f.login("anonymous", "dave@dabeaz.com")
# ftp_name = "/pub/databases/Rfam/14.1"
# recursive_get(f, ftp_name)
# f.close()
