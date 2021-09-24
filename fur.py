import os

SCHEMA_INFO = "schemainfo"
TBFILE = "tbfile"

db_root = os.path.join(os.getcwd(), "db")

def check_db_presence(db_name):
    """Check whether the DB is present or not."""
    db_path = os.path.join(db_root, db_name)
    return os.path.exists(db_path)


def ensure_db_presence(db_name):
    """If the DB is not present, create it."""
    db_path = os.path.join(db_root, db_name)

    already_existed = False

    if check_db_presence(db_path):
        already_existed = True
    else:
        os.mkdir(db_path)

    return already_existed


def check_tb_presence(db_name, tb_name):
    """Check whether the Table is present or not."""
    db_path = os.path.join(db_root, db_name)
    tb_path = os.path.join(db_path, tb_name)
    if os.path.exists(tb_path):
        si_path = os.path.join(tb_path, SCHEMA_INFO)
        tbfile_path = os.path.join(tb_path, TBFILE)

        if os.path.exists(si_path) and os.path.isfile(si_path) and \
                os.path.exists(tbfile_path) and os.path.isfile(tbfile_path):
            return True

    return False


def ensure_tb_presence(db_name, tb_name):
    """If the Table is not present, create it."""
    db_path = os.path.join(db_root, db_name)
    tb_path = os.path.join(db_path, tb_name)

    already_exists = False

    if check_tb_presence(db_path, tb_path):
        already_exists = True
    else:
        ensure_db_presence(db_name)
        os.mkdir(tb_path)

        si_path = os.path.join(tb_path, SCHEMA_INFO)
        tbfile_path = os.path.join(tb_path, TBFILE)

        with open(si_path, 'w') as f:
            f.write("")

        with open(tbfile_path, 'w') as f:
            f.write("")

    return already_exists
