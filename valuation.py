def calculate_pv_fcff (fcff_forecast, wacc):
    pv_fcff = []
    for year, fcff in enumerate(fcff_forecast, start=1):
        pv = fcff / ((1 + wacc) ** year)
        pv_fcff.append (pv)
    return pv_fcff

def calculate_terminal_value (
        final_fcff,
        terminal_growth_rate,
        wacc
):
    terminal_value = (
        final_fcff
        * (1 + terminal_growth_rate)
    ) / (
        wacc - terminal_growth_rate
    )
    return terminal_value

def calculate_pv_terminal_value(
        terminal_value,
        wacc,
        forecast_years
):
    pv_terminal_value = (
        terminal_value
        /
        ((1+wacc) ** forecast_years)
    )
    return pv_terminal_value

def calculate_enterprise_value (
        pv_fcff,
        pv_terminal_value
):
    enterprise_value = (
        sum(pv_fcff)
        + pv_terminal_value
    )
    return enterprise_value

def calculate_equity_value(
        enterprise_value,
        cash,
        debt
):
    equity_value = (
        enterprise_value
        + cash
        - debt
    )
    return equity_value

def calculate_fair_value_per_share(
        equity_value,
        shares_outstanding
):
    fair_value = (
        equity_value
        / shares_outstanding
    )
    return fair_value

