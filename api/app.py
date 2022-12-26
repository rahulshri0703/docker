from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return "this is index page"


@app.get("/home")
def home(name: str, surname: str):
    return "your name is {} {}".format(name, surname)

    # http://127.0.0.1:8000/home?name=rahul&surname=shrivas


class json_dic(BaseModel):
    variable1: float
    variable2: float
    variable3: float


@app.post("/predict")
def predict(data: json_dic):
    data = data.dict()
    v1 = float(data["variable1"])
    v2 = float(data["variable2"])
    v3 = float(data["variable3"])
    v = v1 + v2 + v3

    return f"{v}"


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port="80")

# run: uvicorn app:app --reload --host 0.0.0.0 --port 80
# run from cmd line: uvicorn app:app --host 0.0.0.0 --port 80
# test: curl localhost:80
