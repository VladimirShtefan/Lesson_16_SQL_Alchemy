import json
from pathlib import Path

from sqlalchemy.exc import IntegrityError

from data_base.creat_db import db


def get_data_for_table(file_path: Path) -> list[dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def create_table(data_base: list[dict], name_class):
    db.create_all()

    table = [
        name_class(**column)
        for column in data_base
    ]

    db.session.add_all(table)
    try:
        db.session.commit()
    except IntegrityError:
        print('База уже создана')
