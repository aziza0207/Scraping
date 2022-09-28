from engine import Session
from models import Ads


def data_base(records: list[dict]):
    for record in records:
        record = Ads(image=record["image"], price=record["price"], date=record["date"])
        session = Session()
        session.add(record)
        session.commit()
        session.close()
