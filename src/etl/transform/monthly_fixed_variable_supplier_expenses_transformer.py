import pandas as pd


class MonthlyFixedVsVariableSupplierExpensesTransformer:

    @staticmethod
    def transform(records):

        if not records:
            return pd.DataFrame()

        data = []

        for r in records:
            if not r.entity or not r.subcategory:
                continue

            data.append({
                "date": r.record_date,
                "amount": float(r.record_amount),
                "type": r.record_type,
                "entity_name": r.entity.entity_name,
                "entity_type": r.entity.entity_type,
                "is_fixed": r.subcategory.is_fixed,
            })

        df = pd.DataFrame(data)

        df = df[df["type"] == "expense"]
        df = df[df["entity_type"] == "SUPPLIER"]

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        df["expense_category"] = df["is_fixed"].apply(
            lambda x: "FIXED" if x else "VARIABLE"
        )

        grouped = (
            df.groupby(
                ["year", "month", "entity_name", "expense_category"],
                as_index=False
            )
            .agg(total_expense=("amount", "sum"))
        )

        result = (
            grouped.pivot_table(
                index=["year", "month", "entity_name"],
                columns="expense_category",
                values="total_expense",
                fill_value=0
            )
            .reset_index()
        )

        result["total_expense"] = (
            result.get("FIXED", 0) + result.get("VARIABLE", 0)
        )

        result = result.sort_values(
            by=["year", "month", "total_expense"],
            ascending=[True, True, False]
        )

        return result
