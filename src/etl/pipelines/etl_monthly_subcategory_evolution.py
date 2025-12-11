from src.db.database import SessionLocal
from src.etl.extract.records_extractor import RecordsExtractor
from src.etl.transform.monthly_subcategory_evolution_transformer import MonthlySubcategoryEvolutionTransformer
from src.etl.load.monthly_subcategory_evolution_loader import MonthlySubcategoryEvolutionLoader


def run_monthly_subcategory_evolution_etl(user_id: int):

    db = SessionLocal()

    try:
        print("Extracting records...")
        records = RecordsExtractor.get_records_by_user(db, user_id=1)

        print("Transforming...")
        df = MonthlySubcategoryEvolutionTransformer.transform(records)

        print("Preview:")
        print(df.head())

        print("Saving CSV...")
        output_path = MonthlySubcategoryEvolutionLoader.save_to_csv(df)

        print(f"ETL completed successfully. File saved at: {output_path}")

    finally:
        db.close()


if __name__ == "__main__":
    run_monthly_subcategory_evolution_etl(user_id=1)
