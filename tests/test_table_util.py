import argparse
from pprint import pprint as pp
from pprint import pformat as pf

from pathlib import Path

from mypyutil import table_util

def test_dict():
    data = [
            {"a": "あ"},
            {"b": "イ"},
            {"c": "兎"},
            ]
    fpath_str = "out/data.csv"
    fpath_path = Path(fpath_str)
    header = table_util.collect_header(data)
    table_util.write_dict(fpath_str, header, data)
    table_util.write_dict(fpath_path, header, data)
    table_util.write_csv_dict(fpath_str, header, data)
    table_util.write_csv_dict(fpath_str, header, data)
    table_util.load_as_list(fpath_str)
    table_util.load_as_list(fpath_path)
    table_util.load_as_dict(fpath_str)
    table_util.load_as_dict(fpath_path)
    fpath_str = "out/data.xlsx"
    fpath_path = Path(fpath_str)
    table_util.write_dict(fpath_str, header, data)
    table_util.write_dict(fpath_path, header, data)
    table_util.write_xlsx_dict(fpath_path, header, data)
    table_util.write_xlsx_dict(fpath_path, header, data)
    table_util.load_as_list(fpath_str)
    table_util.load_as_list(fpath_path)
    table_util.load_as_dict(fpath_str)
    table_util.load_as_dict(fpath_path)

def test_ll():
    data = [
            ["value"],
            ["あ"],
            ["イ"],
            ["兎"],
            ]
    fpath_str = "out/data.csv"
    fpath_path = Path(fpath_str)
    table_util.write_ll(fpath_str, data)
    table_util.write_ll(fpath_path, data)
    table_util.write_csv_ll(fpath_str, data)
    table_util.write_csv_ll(fpath_str, data)
    table_util.load_as_list(fpath_str)
    table_util.load_as_list(fpath_path)
    table_util.load_as_dict(fpath_str)
    table_util.load_as_dict(fpath_path)
    fpath_str = "out/data.xlsx"
    fpath_path = Path(fpath_str)
    table_util.write_ll(fpath_str, data)
    table_util.write_ll(fpath_path, data)
    table_util.write_xlsx_ll(fpath_path, data)
    table_util.write_xlsx_ll(fpath_path, data)
    table_util.load_as_list(fpath_str)
    table_util.load_as_list(fpath_path)
    table_util.load_as_dict(fpath_str)
    table_util.load_as_dict(fpath_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("cmd", description="This is hogehoge")
    args = parser.parse_args()

    #test_dict()
    test_ll()

    print('\033[32m' + 'end' + '\033[0m') # ]] fix indent for vim

