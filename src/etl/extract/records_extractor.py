from sqlalchemy.orm import Session
from src.db.models.record import Record

class RecordsExtractor:

    @staticmethod
    def get_all_records(db: Session):
        return (
            db.query(Record)
            .filter(Record.currency_id == 1)  
            .all()
        )