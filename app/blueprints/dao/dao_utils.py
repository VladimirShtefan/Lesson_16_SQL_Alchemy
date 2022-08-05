import json
from pathlib import Path

from sqlalchemy.exc import IntegrityError

from data_base.creat_db import db
from data_base.models.models import User, Offer, Order


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
    db.session.close()


class DataBase:
    def __init__(self, object_name: db.Model):
        self.object_name = object_name

    def add_object(self, data: dict) -> list[dict]:
        new_object: User | Offer | Order = [self.object_name(**data)][0]
        db.session.add(new_object)
        db.session.commit()
        return new_object.convert_in_dict()

    def update_object(self, data: dict, id: int) -> list[dict]:
        item: User | Offer | Order = db.session.query(self.object_name).get(id)
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item.convert_in_dict()

    def delete_object(self, id: int) -> dict:
        item: User | Offer | Order = db.session.query(self.object_name).get(id)
        db.session.delete(item)
        db.session.commit()
        return {
                'object_id': id,
                'status_deleted': 'ok'
                }
