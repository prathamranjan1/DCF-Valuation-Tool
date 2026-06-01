import yfinance as yf

def get_beta(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get(
        "beta",
        1
    )

RISK_FREE_RATES = {
    "United States": 0.045,
    "India": 0.070,
    "Japan": 0.010,
    "Germany": 0.025,
    "United Kingdom": 0.040,
    "Switzerland": 0.015,
    "Canada": 0.035,
    "Australia": 0.040
}

def get_risk_free_rate(country):
    return RISK_FREE_RATES.get(
        country,
        0.04
    )

# CAPM
def calculate_cost_of_equity(
    risk_free_rate,
    beta,
    equity_risk_premium
):
    return (
        risk_free_rate
        +
        beta * equity_risk_premium
    )

# KD
def calculate_cost_of_debt():
    return 0.05

#WACC
def calculate_wacc(
    market_cap,
    debt,
    tax_rate,
    cost_of_equity,
    cost_of_debt
):

    equity_weight = (
        market_cap
        /
        (market_cap + debt)
    )

    debt_weight = (
        debt
        /
        (market_cap + debt)
    )

    wacc = (
        equity_weight
        * cost_of_equity
    ) + (
        debt_weight
        * cost_of_debt
        * (1 - tax_rate)
    )

    return wacc

ERP_BY_CURRENCY = {
    "USD": 0.05,
    "INR": 0.07,
    "EUR": 0.05,
    "JPY": 0.05,
    "GBP": 0.055,
    "CHF": 0.045,
    "CAD": 0.05,
    "AUD": 0.055
}

def get_equity_risk_premium(currency):

    return ERP_BY_CURRENCY.get(
        currency,
        0.05
    )

INTEREST_EXPENSE_LABELS = [
    "Interest Expense",
    "Net Interest Income",
    "Interest Expense Non Operating"
]

def get_row_value(
    statement,
    possible_rows
):
    for row in possible_rows:
        if row in statement.index:
            return statement.loc[row]
    return None

def calculate_cost_of_debt(
    income_statement,
    debt_series
):
    try:
        interest_expense = get_row_value(
            income_statement,
            INTEREST_EXPENSE_LABELS
        )
        if interest_expense is None:
            return 0.05
        average_interest = abs(
            interest_expense.mean()
        )
        average_debt = debt_series.mean()
        if average_debt <= 0:
            return 0.05
        return (
            average_interest
            /
            average_debt
        )
    except:
        return 0.05
    
TERMINAL_GROWTH_BY_CURRENCY = {
    "USD": 0.025,
    "EUR": 0.020,
    "GBP": 0.025,
    "INR": 0.050,
    "JPY": 0.010,
    "CHF": 0.015,
    "CAD": 0.020,
    "AUD": 0.025
}

def get_terminal_growth_rate(
    currency
):
    return TERMINAL_GROWTH_BY_CURRENCY.get(
        currency,
        0.025
    )