import pandas as pd

class MonthlySubcategoryEvolutionTransformer:

    @staticmethod
    def transform(records):

        if not records:
            return pd.DataFrame()

        data = []

        for r in records:
            data.append({
                "date": r.record_date,
                "amount": float(r.record_amount),
                "subcategory_name": (
                    r.subcategory.subcategory_name if r.subcategory else "Uncategorized"
                )
            })

        df = pd.DataFrame(data)

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        grouped = (
            df.groupby(["year", "month", "subcategory_name"])["amount"]
            .sum()
            .reset_index()
        )

        return grouped
