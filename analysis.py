import pandas as pd

def calculate_revenue_cagr(revenue_series):
    revenue_series = revenue_series.dropna()
    latest_revenue = revenue_series.iloc[0]
    oldest_revenue = revenue_series.iloc[-1]
    years = len(revenue_series) - 1
    cagr = ((latest_revenue/oldest_revenue) ** (1/years)) - 1
    return cagr * 100

def calculate_ebit_margin(revenue_series, ebit_series):
    ebit_margin = (ebit_series/revenue_series) * 100
    return ebit_margin

def calculate_average_margin(ebit_margin_series):
    return ebit_margin_series.mean()

def calculate_average_tax_rate(
    income_statement
):
    try:
        tax_expense = income_statement.loc[
            "Tax Provision"
        ]
        pretax_income = income_statement.loc[
            "Pretax Income"
        ]
        tax_rate = (
            tax_expense
            /
            pretax_income
        ) * 100
        return tax_rate.mean()
    except:
        return 25
    
def calculate_depreciation_percent(
    cashflow,
    revenue
):
    try:
        depreciation = cashflow.loc[
            "Depreciation And Amortization"
        ]
        percentage = (
            depreciation
            /
            revenue
        ) * 100
        return percentage.mean()
    except:
        return 3
    
def calculate_capex_percent(
    cashflow,
    revenue
):
    try:
        capex = abs(
            cashflow.loc[
                "Capital Expenditure"
            ]
        )
        percentage = (
            capex
            /
            revenue
        ) * 100
        return percentage.mean()
    except:
        return 5
    
def calculate_recent_growth(
    revenue_series
):
    revenue_series = revenue_series.dropna()
    latest_revenue = revenue_series.iloc[0]
    previous_revenue = revenue_series.iloc[1]
    growth = (
        (
            latest_revenue
            -
            previous_revenue
        )
        /
        previous_revenue
    ) * 100

    return growth

def calculate_forecast_growth_rate(
    revenue_cagr,
    recent_growth
):

    forecast_growth = (
        revenue_cagr * 0.7
        +
        recent_growth * 0.3
    )

    return forecast_growth

