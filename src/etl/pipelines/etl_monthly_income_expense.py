from src.db.database import SessionLocal
from src.etl.extract.records_extractor import RecordsExtractor
from src.etl.transform.monthly_transformer import MonthlyIncomeExpenseTransformer
from src.etl.load.monthly_loader import MonthlyIncomeExpenseLoader

def run_monthly_income_expense_etl():
    """
    Full ETL pipeline:
    1. Extract records from DB
    2. Transform them into monthly summary
    3. Load results into a CSV file
    """
    db = SessionLocal()

    try:
        print("Extracting records...")
        records = RecordsExtractor.get_all_records(db)

        print("Transforming...")
        df = MonthlyIncomeExpenseTransformer.transform(records)

        print("Preview (primeras filas):")
        print(df.head())

        print("Saving to CSV file...")
        output_path = MonthlyIncomeExpenseLoader.save_to_csv(df)

        print(f"ETL completed successfully. File saved at: {output_path}")

    finally:
        db.close()


if __name__ == "__main__":
    run_monthly_income_expense_etl()
