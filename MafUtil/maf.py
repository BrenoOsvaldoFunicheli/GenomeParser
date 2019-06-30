import os

# tam = os.path.getsize('/home/breno/Documents/cbioSimone/data/hboc_maf.maf')

# value = os.getcwd()
# value += '/' + os.listdir()[0]
# os.chdir(value)

path_r = '/home/breno/Documents/cbioSimone/data/mafs'
file_r = 'data_mutations_extends.maf'


def join_maf_files(path_dir, file_name):
    for i in os.listdir(path_dir):
        wf = open(file_name, 'a')
        value = get_maf(path_dir, i)
        for j in value[2:]:
            wf.write(j)
        wf.close()


def get_maf(path_dir, path):
    file = open(path_dir + '/' + path, 'r')
    lines = file.readlines()
    file.close()
    return lines


def fill_header(path_dir, file_name):
    for i in os.listdir(path_dir):
        wf = open(file_name, 'w')
        value = get_maf(path_dir, i)
        for j in value[1:2]:
            wf.write(j)
        wf.close()
        break


def build_maf(maf_path, filename):
    fill_header(maf_path, filename)
    join_maf_files(maf_path, filename)
    

if __name__ == '__main__':
    fill_header(path_r, file_r)
    join_maf_files(path_r, file_r)
