import os
import pandas as pd
from datetime import datetime

class MonthlyIncomeExpenseLoader:

    @staticmethod
    def save_to_csv(df, output_dir="data/analytics"):

        # Ensure directory exists
        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"analytics_monthly_{timestamp}.csv"
        path = os.path.join(output_dir, filename)

        # Save CSV
        df.to_csv(path, index=False)

        print(f"CSV saved at: {path}")

        return path
