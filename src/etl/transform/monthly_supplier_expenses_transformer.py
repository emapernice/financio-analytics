import pandas as pd


class MonthlySupplierExpensesTransformer:

    @staticmethod
    def transform(records):

        if not records:
            return pd.DataFrame()

        data = []

        for r in records:
            if not r.entity:
                continue

            data.append({
                "date": r.record_date,
                "amount": float(r.record_amount),
                "type": r.record_type,
                "entity_name": r.entity.entity_name,
                "entity_type": r.entity.entity_type,
            })

        df = pd.DataFrame(data)

        df = df[df["type"] == "expense"]

        df = df[df["entity_type"] == "SUPPLIER"]

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        result = (
            df.groupby(["year", "month", "entity_name"], as_index=False)
              .agg(total_expense=("amount", "sum"))
        )

        result = result.sort_values(
            by=["year", "month", "total_expense"],
            ascending=[True, True, False]
        )

        return result
