from sqlalchemy.orm import Session, joinedload
from src.db.models.account import Account
from src.db.models.record import Record


class RecordsExtractor:

    @staticmethod
    def get_records_by_user(db: Session, user_id: int):
        """
        Retrieves all records that belong to any account of the specified user,
        filtered by currency_id = 1.
        """

        account_ids = (
            db.query(Account.id)
              .filter(Account.user_id == user_id)
              .all()
        )

        account_ids = [a[0] for a in account_ids]

        if not account_ids:
            return []

        return (
            db.query(Record)
            .options(joinedload(Record.subcategory))
            .filter(
                Record.account_id.in_(account_ids),
                Record.currency_id == 1
            )
            .all()
        )
