from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, VARCHAR
from pydantic import BaseModel
from flask import Flask, request, jsonify

app = Flask(__name__)


class Validate_Data(BaseModel):
    Index: int
    Name: str
    Age: int


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    if request.method == "GET":
        return "Get return"

    elif request.method == "POST":
        request_data = request.json
        breakpoint()
        return jsonify(request_data)

    return "Welcome"


@app.route("/data", methods=["GET", "POST"])
def post_data():
    request_data = request.json
    breakpoint()
    result = Validate_Data(**request_data)
    type(result)

    engine = create_engine("mysql+pymysql://root:8080@localhost:3306/yogeshdb", echo=True)

    meta = MetaData()

    Demo_table = Table(
        "Demo", meta, Column('Index', Integer), Column("Name", String(50)), Column("Age", Integer)
    )
    meta.create_all(engine)

    conn = engine.connect()
    # data1 = Demo_table.insert().values(Index=3,Name="Yogesh",Age=23)
    conn.execute(Demo_table.insert(), [{'Index': 4, 'Name': "Vishal", 'Age': 25},
                                       {'Index': 5, 'Name': "Vijay", 'Age': 20},
                                       {'Index': 6, 'Name': "Ajay", 'Age': 30}])
    conn.commit()

    data = conn.execute(Demo_table.select())

    data = data.fetchone()

    return "request_data"


if __name__ == "__main__":
    app.run(debug=True)