import csv

def load_csv(fpath):
    reader = csv.reader(open(fpath, encoding="utf_8_sig"))
    data = []
    for row in reader:
        data.append(row)
    return data

def load_csv_as_dict(fpath):
    reader = csv.DictReader(open(fpath, encoding="utf_8_sig"))
    data = [row for row in reader]
    return data

def write(fpath, header, data):
    writer = csv.writer(open(fpath, "w", encoding="utf_8_sig"))
    writer.writerow(header)
    for row in data:
        writer.writerow(row)

def write_dict(fpath, header, data):
    writer = csv.DictWriter(open(fpath, "w", encoding="utf_8_sig"), header)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

