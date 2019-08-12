import re
import csv
import json

field_names = []


def clean_output(dirty_value):
    """
        :param dirty_value: values of the header that will be clean, based one regular expression
        :return: array with an unique line that contain csv file headers
    """
    array_header = dirty_value.split('\t')
    return [re.sub(r'(\s|\?)', '', j) for j in array_header]


def parse_headers(address):
    """
        :param address: this values is a reference of the first line of the file
        header that be parsed by this function. For example, first line of a csv file.
        :return: return a vector splitted that contains one attribute by position
        according to attribute of the csv file
    """
    with open(address) as file:
        for head in file:
            return clean_output(head)


def create_json(origin_file, dest_path):
    """
    :field_names received parsed header with field names of the attributes of the origin file
    :reader: Data Structure that received mapping of fields parsed and csv file

    :param origin_file: address of the file that will be parsed
    :param dest_path: address json file where going to save json values
    """
    field_name = parse_headers(origin_file)

    with open(origin_file, 'r') as file:
        reader = csv.DictReader(file, fieldnames=field_name, dialect='excel-tab')

        with open(dest_path, 'w') as json_file:
            out = json.dumps([row for row in reader])
            json_file.write(out)


if __name__ == 'main':
    create_json('/home/breno/Downloads/Gene_info.txt', 'file.json')
