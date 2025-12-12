import pandas as pd

class MonthlyFixedVariableTransformer:

    EXCLUDED_SUBCATEGORIES = [70, 71, 72, 73, 74, 75, 76, 77, 78, 81]

    @staticmethod
    def transform(records):

        if not records:
            return pd.DataFrame()

        data = []

        for r in records:
            data.append({
                "date": r.record_date,
                "amount": float(r.record_amount),
                "subcategory_id": r.subcategory_id,
                "type": r.record_type,   
                "is_fixed": r.subcategory.is_fixed if r.subcategory else None,
            })

        df = pd.DataFrame(data)

        df = df[df["type"] == "expense"]

        df = df[~df["subcategory_id"].isin(MonthlyFixedVariableTransformer.EXCLUDED_SUBCATEGORIES)]

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        df["is_fixed"] = df["is_fixed"].fillna(False).astype(bool)

        pivot = df.pivot_table(
            index=["year", "month"],
            columns="is_fixed",
            values="amount",
            aggfunc="sum",
            fill_value=0
        ).reset_index()

        pivot = pivot.rename(columns={
            True: "fixed_expenses",
            False: "variable_expenses"
        })

        if "fixed_expenses" not in pivot:
            pivot["fixed_expenses"] = 0
        if "variable_expenses" not in pivot:
            pivot["variable_expenses"] = 0

        pivot["total_expenses"] = pivot["fixed_expenses"] + pivot["variable_expenses"]

        return pivot
