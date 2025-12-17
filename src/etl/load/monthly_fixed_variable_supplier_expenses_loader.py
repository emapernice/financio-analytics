import os
from datetime import datetime


class MonthlyFixedVsVariableSupplierExpensesLoader:

    @staticmethod
    def save_to_csv(df, output_dir="data/analytics"):

        os.makedirs(output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = (
            f"analytics_monthly_fixed_vs_variable_supplier_expenses_{timestamp}.csv"
        )

        path = os.path.join(output_dir, filename)
        df.to_csv(path, index=False)

        print(f"CSV saved at: {path}")

        return path
