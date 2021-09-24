from flask import Flask, jsonify
import fur

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Yep, it's working")


@app.get("/db/<db_name>")
def check_db_presence(db_name):
    res = {}
    
    if fur.check_db_presence(db_name):
        res["message"] = f"Database '{db_name}' exists."
    else:
        res["message"] = f"Database '{db_name}' does not exist."

    return jsonify(res)


@app.post("/db/<db_name>")
def ensure_db_presence(db_name):
    res = {}
    
    if fur.ensure_db_presence(db_name):
        res["message"] = f"Database '{db_name}' already exists."
    else:
        res["message"] = f"Database '{db_name}' has been created."

    return jsonify(res)


@app.get("/db/<db_name>/tb/<tb_name>")
def check_tb_presence(db_name, tb_name):
    res = {}
    
    if fur.check_tb_presence(db_name, tb_name):
        res["message"] = f"Table '{tb_name}' exists."
    else:
        res["message"] = f"Table '{tb_name}' does not exist."

    return jsonify(res)


@app.post("/db/<db_name>/tb/<tb_name>")
def ensure_tb_presence(db_name, tb_name):
    res = {}
    
    if fur.ensure_tb_presence(db_name, tb_name):
        res["message"] = f"Table '{tb_name}' already exists."
    else:
        res["message"] = f"Table '{tb_name}' has been created."

    return jsonify(res)


@app.get("/db/<db_name>/table/<table_name>/query/all")
def get_all_rows(db_name, table_name):
    pass


if __name__ == "__main__":
    app.run(debug=True)
