from src.db.database import SessionLocal
from src.etl.extract.records_extractor import RecordsExtractor
from src.etl.transform.monthly_transformer import MonthlyIncomeExpenseTransformer
from src.etl.load.monthly_loader import MonthlyIncomeExpenseLoader

def run_monthly_income_expense_etl(user_id: int):

    db = SessionLocal()

    try:
        print("Extracting records...")
        records = RecordsExtractor.get_records_by_user(db, user_id=1)

        print("Transforming...")
        df = MonthlyIncomeExpenseTransformer.transform(records)

        print(df.head())

        print("Saving to CSV...")
        output_path = MonthlyIncomeExpenseLoader.save_to_csv(df)

        print(f"ETL completed successfully. File saved at: {output_path}")

    finally:
        db.close()


if __name__ == "__main__":
    run_monthly_income_expense_etl(user_id=1)
