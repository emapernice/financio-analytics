import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

connection_str = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
)

def test_connection():
    try:
        engine = create_engine(connection_str)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✔️ Database connection successful!", result.fetchone())
    except Exception as e:
        print("❌ Database connection FAILED.")
        print(e)

if __name__ == "__main__":
    test_connection()
