import csv

"""
e.g.
    columns = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "name TEXT",
            "age INTERGER",
            ]
"""
def make_table(cur, table_name, columns):
    columns_part = ", ".join(columns)
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_part})"
    #print('sql') # debug
    #print(sql) # debug
    cur.execute(sql)

"""
e.g.
    columns = ["name", "age"]
    data = [
            ["jk", 17],
            ["adult", 20],
            ]
    insert_data(cur, table_name, columns, data)
"""
def insert_data(cur, table_name, columns, data):
    empty_values = ", ".join(["?"] * len(columns))
    columns = ", ".join(columns)
    sql = f"insert into {table_name} ({columns}) values ({empty_values})"
    print('sql') # debug
    print(sql) # debug
    for one in data:
        cur.execute(sql, one)

def dump_table_to_csv(fpath, cur, table_name):
    with open(fpath, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        print('[description[0] for description in cursor.description]') # debug
        print([description[0] for description in cur.description]) # debug
        for row in rows:
            csv_writer.writerow(row)

