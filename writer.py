import os


db_root = os.path.join(os.getcwd(), "db")
GLOBAL_SILENCE = False


def get_all_tables(db_name):
    res = {}

    db_path = os.path.join(db_root, db_name)
    res["db_path"] = db_path

    return res

class FurDB:
    def __init__(self, db_name=None, silent=GLOBAL_SILENCE):
        self.db_name = db_name

        if self.db_name:
            db_path = os.path.join(db_root, self.db_name)
            silent or print(f"Checking {db_path}")

            if os.path.exists(db_path):
                silent or print("DB location already exists.")
            else:
                silent or print("DB location not present. Attempting to create.")
                os.mkdir(db_path)

    def get_table(self, table_name, columns):
        table = FurTable(self, table_name, columns)
        return table


class FurColumn:
    def __init__(self, column_name = "", size=1):
        self.column_name = column_name
        self.size = size

    def __repr__(self):
        return f"<FurColumn({self.column_name}, {self.size})>"


class FurTable:
    def __init__(self, db, table_name="", columns=[]):
        self.db = db
        self.table_name = table_name
        self.columns = columns


def main():
    print(f"DB Root: {db_root}")
    db = FurDB("MyDB")
    # print(db)


# data = [173, 40]
# column_sizes = [4, 10]

# correct_ans = [10, 842]

def get_bit(data, n):
    byte = n // 8
    offset = 7 - (n % 8)
    return (data[byte] >> offset) & 1


def get_slice(data, start, end):
    value = 0

    for bit in range(start, end):
        value += get_bit(data, bit) << (end - bit - 1)

    return value


def get_value(data, column_sizes, row, col):
    row_bits = 0
    col_bits = 0

    for i, e in enumerate(column_sizes):
        row_bits += e
        if i < col:
            col_bits += e

    base = row * row_bits + col_bits
    return get_slice(data, base, base + column_sizes[col])

def get_row(data, column_sizes, base=0):
    row = []

    start = base

    for col_number in column_sizes:
        current_value = get_slice(data, start, start + col_number)

        row.append(current_value)

        start += col_number

    return row


# print(get_value(data, column_sizes, 0, 1))
# print(correct_ans)


if __name__ == "__main__":
    main()
