from src.db.database import SessionLocal
from src.etl.extract.records_extractor import RecordsExtractor
from src.etl.transform.monthly_supplier_expenses_transformer import MonthlySupplierExpensesTransformer
from src.etl.load.monthly_supplier_expenses_loader import MonthlySupplierExpensesLoader


def run_monthly_supplier_expenses_etl(user_id: int):

    db = SessionLocal()

    try:
        print("Extracting records...")
        records = RecordsExtractor.get_records_by_user(db, user_id)

        print("Transforming (monthly supplier expenses)...")
        df = MonthlySupplierExpensesTransformer.transform(records)


        print("Preview:")
        print(df.head())

        print("Saving to CSV...")
        output_path = MonthlySupplierExpensesLoader.save_to_csv(df)

        print(f"ETL completed successfully. File saved at: {output_path}")

    finally:
        db.close()


if __name__ == "__main__":
    run_monthly_supplier_expenses_etl(user_id=1)
