import pandas as pd

class MonthlyIncomeExpenseTransformer:

    EXCLUDED_SUBCATEGORIES = [70, 71, 72, 73, 74, 75, 76, 77, 78, 81]

    @staticmethod
    def transform(records):

        if not records:
            return pd.DataFrame()

        data = []

        for r in records:
            data.append({
                "date": r.record_date,
                "type": r.record_type,
                "amount": float(r.record_amount),
                "subcategory_id": r.subcategory_id
            })

        df = pd.DataFrame(data)

        df = df[~df["subcategory_id"].isin(MonthlyIncomeExpenseTransformer.EXCLUDED_SUBCATEGORIES)]

        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        df = df.dropna(subset=["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        pivot = df.pivot_table(
            index=["year", "month"],
            columns="type",
            values="amount",
            aggfunc="sum",
            fill_value=0
        ).reset_index()

        if "income" not in pivot:
            pivot["income"] = 0
        if "expense" not in pivot:
            pivot["expense"] = 0

        pivot["difference"] = pivot["income"] - pivot["expense"]

        return pivot
