import os
import pandas as pd
from datetime import datetime

class MonthlyFixedVariableLoader:

    @staticmethod
    def save_to_csv(df, output_dir="data/analytics"):
        """
        Saves the monthly fixed vs variable expense analysis into a timestamped CSV.
        """

        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"analytics_fixed_vs_variable_{timestamp}.csv"
        path = os.path.join(output_dir, filename)

        df.to_csv(path, index=False)

        print(f"CSV saved at: {path}")

        return path
