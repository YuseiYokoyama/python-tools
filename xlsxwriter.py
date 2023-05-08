import argparse
from pprint import pprint as pp
from pprint import pformat as pf

import xlsxwriter


if __name__ == '__main__':
    parser = argparse.ArgumentParser("This is hogehoge")
    args = parser.parse_args()

    wb = xlsxwriter.Workbook('rich_strings.xlsx')
    ws = wb.add_worksheet()

    ws.write(0, 0, "zero indexed")

    ws.set_column('A:A', 30)

    # Set up some formats to use.
    bold = wb.add_format({'bold': True})
    italic = wb.add_format({'italic': True})
    red = wb.add_format({'color': 'red'})
    blue = wb.add_format({'color': 'blue'})
    center = wb.add_format({'align': 'center'})
    superscript = wb.add_format({'font_script': 1})

    # Write some strings with multiple formats.
    ws.write_rich_string('A3',
                                'This is ',
                                red, 'red',
                                ' and this is ',
                                blue, 'blue')

    # If you have formats and segments in a list you can add them like this:
    rich_text = ['This is ', 'normal', ' and this is ', blue, 'blue']
    ws.write_rich_string('A9', *rich_text)

    wb.close()


    print('\33[32m' + 'end' + '\033[0m')

