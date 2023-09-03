import datetime, os
from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class ObjectPOST(BaseModel):
    startDate: str
    endDate: str

@app.post("/info")
def post_info(object: ObjectPOST):
    startDate = str_to_date(object.startDate)
    endDate = str_to_date(object.endDate)
    with open('w.log', 'a') as log_file:
        log_file.write(str(startDate) + '\n')
        log_file.write(str(endDate) + '\n')
    # TODO  сделать создание документов
    return 'Готово'


def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ').date()

    # uvicorn app.main:app --reload --host 172.17.2.99