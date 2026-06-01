import pandas as pd

def create_sensitivity_table(
        fcff_forecast,
        cash,
        debt,
        shares_outstanding
):
    wacc_range = [0.08, 0.09, 0.10, 0.11, 0.12]
    growth_range = [0.02, 0.03, 0.04, 0.05, 0.06]
    sensitivity_table = pd.DataFrame()

    for growth in growth_range:
        values = []

        for wacc in wacc_range:
            terminal_value = (
                fcff_forecast[-1]
                * (1+growth)
            ) / (
                wacc-growth
            )
            pv_fcff = []

            for year, fcff in enumerate(
                fcff_forecast,
                start=1
            ):
                pv = fcff / ((1 + wacc) ** year)
                pv_fcff.append(pv)

            pv_terminal = (
                terminal_value
                /
                ((1+wacc) ** 5)
            )

            enterprise_value = (
                sum(pv_fcff)
                + pv_terminal
            )

            equity_value = (
                enterprise_value
                + cash
                - debt
            )

            fair_value = (
                equity_value
                / shares_outstanding
            )

            values.append(
                round(fair_value, 2)
            )

        sensitivity_table[
            f"{growth*100:.0f}%"
        ] = values

    sensitivity_table.index = [
        "8%",
        "9%",
        "10%",
        "11%",
        "12%"
    ]

    return sensitivity_table