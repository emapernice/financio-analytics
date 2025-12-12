from src.db.database import SessionLocal
from src.etl.extract.records_extractor import RecordsExtractor
from src.etl.transform.monthly_fixed_variable_transformer import MonthlyFixedVariableTransformer
from src.etl.load.monthly_fixed_variable_loader import MonthlyFixedVariableLoader


def run_monthly_fixed_variable_etl(user_id: int):

    db = SessionLocal()

    try:
        print("Extracting records...")
        records = RecordsExtractor.get_records_by_user(db, user_id)

        print("Transforming (fixed vs variable)...")
        df = MonthlyFixedVariableTransformer.transform(records)

        print("Preview:")
        print(df.head())

        print("Saving to CSV...")
        output_path = MonthlyFixedVariableLoader.save_to_csv(df)

        print(f"ETL completed successfully. File saved at: {output_path}")

    finally:
        db.close()


if __name__ == "__main__":
    run_monthly_fixed_variable_etl(user_id=1)
