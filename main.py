import yfinance as yf
from data_fetcher import get_standardized_financials
from data_fetcher import validate_ticker
from analysis import calculate_ebit_margin
from analysis import calculate_average_margin
from analysis import calculate_revenue_cagr
from forecast import forecast_revenue
from forecast import forecast_ebit
from fcff import calculate_nopat
from fcff import calculate_fcff
from valuation import calculate_pv_fcff
from valuation import calculate_terminal_value
from valuation import calculate_pv_terminal_value
from valuation import calculate_enterprise_value
from valuation import calculate_equity_value
from valuation import calculate_fair_value_per_share
from sensitivity import create_sensitivity_table
from formatter import get_currency_symbol
from formatter import format_large_number
from excel_exporter import export_dcf_report
from dashboard import get_current_price
from dashboard import calculate_upside_downside
from dashboard import get_recommendation
from wacc import get_risk_free_rate
from wacc import get_beta  
from wacc import calculate_cost_of_equity  
from wacc import calculate_wacc 
from wacc import get_equity_risk_premium
from wacc import calculate_cost_of_debt
from wacc import get_terminal_growth_rate
from analysis import calculate_average_tax_rate
from analysis import calculate_depreciation_percent
from analysis import calculate_capex_percent
from analysis import calculate_recent_growth
from analysis import calculate_forecast_growth_rate


ticker = input("Enter stock ticker: ")
if not validate_ticker(ticker):

    print()

    print(
        f"ERROR: '{ticker}' is not a valid Yahoo Finance ticker."
    )

    quit()


financials = get_standardized_financials(ticker)
stock = yf.Ticker(ticker)
company_name = financials["company_name"]
income_statement = financials["income_statement"]
cashflow = financials["cashflow"]
market_cap = financials["market_cap"]
country = financials["country"]
currency = financials["currency"]
risk_free_rate = get_risk_free_rate(country)
currency_symbol = get_currency_symbol(currency)
beta = get_beta(ticker)
latest_cash = financials["cash"].iloc[0]
latest_debt = financials["debt"].iloc[0]
shares_outstanding = financials["shares_outstanding"]
revenue = financials["revenue"]
ebit = financials["ebit"]
revenue_cagr = calculate_revenue_cagr(revenue)  

recent_growth = (
    calculate_recent_growth(
        revenue
    )
)

forecast_growth_rate = (
    calculate_forecast_growth_rate(
        revenue_cagr,
        recent_growth
    )
)

growth_assumption = (
    forecast_growth_rate
    /
    100
)

equity_risk_premium = (
    get_equity_risk_premium(
        currency
    )
)

terminal_growth_rate = (
    get_terminal_growth_rate(
        currency
    )
)

tax_rate = (
    calculate_average_tax_rate(
        income_statement
    )
    /
    100
)

depreciation_percent = (
    calculate_depreciation_percent(
        cashflow,
        revenue
    )
    /
    100
)

capex_percent = (
    calculate_capex_percent(
        cashflow,
        revenue
    )
    /
    100
)

cost_of_equity = calculate_cost_of_equity(
    risk_free_rate,
    beta,
    equity_risk_premium
)

cost_of_debt = (
    calculate_cost_of_debt(
        income_statement,
        financials["debt"]
    )
)

wacc = calculate_wacc(
    market_cap,
    latest_debt,
    tax_rate,
    cost_of_equity,
    cost_of_debt
)

if terminal_growth_rate >= wacc:

    print()

    print(
        "ERROR: Terminal Growth Rate must be lower than WACC."
    )

    quit()

ebit_margin = calculate_ebit_margin(
    revenue,
    ebit
)  

average_margin = calculate_average_margin(
    ebit_margin
) 

latest_revenue = revenue.iloc[0]

revenue_forecast = forecast_revenue(
    latest_revenue,
    growth_assumption,
    5
)

ebit_forecast = forecast_ebit(
    revenue_forecast,
    average_margin / 100
)

nopat_forecast = calculate_nopat(
    ebit_forecast,
    tax_rate
)

fcff_forecast = calculate_fcff(
    nopat_forecast,
    depreciation_percent,
    capex_percent,
    revenue_forecast
)

pv_fcff = calculate_pv_fcff(
    fcff_forecast,
    wacc
)

terminal_value = calculate_terminal_value(
    fcff_forecast[-1],
    terminal_growth_rate,
    wacc
)

pv_terminal_value = calculate_pv_terminal_value(
    terminal_value,
    wacc,
    5
)

enterprise_value = calculate_enterprise_value(
    pv_fcff,
    pv_terminal_value
)

equity_value = calculate_equity_value(
    enterprise_value,
    latest_cash,
    latest_debt
)

fair_value_per_share = (
    calculate_fair_value_per_share(
        equity_value,
        shares_outstanding
    )
)

current_price = get_current_price(
    ticker
)

upside_downside = (
    calculate_upside_downside(
        fair_value_per_share,
        current_price
    )
)

recommendation = (
    get_recommendation(
        upside_downside
    )
)

sensitivity_table = create_sensitivity_table(
    fcff_forecast,
    latest_cash,
    latest_debt,
    shares_outstanding
)

print()

print("=" * 60)
print("DCF VALUATION REPORT")
print("=" * 60)

# --------------------------------------------------
# COMPANY INFORMATION
# --------------------------------------------------

print()
print("COMPANY INFORMATION")
print("-" * 60)

print("Company:", company_name)
print("Ticker:", ticker)
print("Country:", country)
print("Currency:", currency)

# --------------------------------------------------
# FORECAST ASSUMPTIONS
# --------------------------------------------------

print()
print("FORECAST ASSUMPTIONS")
print("-" * 60)

print(
    "Historical Revenue CAGR:",
    f"{revenue_cagr:.2f}%"
)

print(
    "Recent Revenue Growth:",
    f"{recent_growth:.2f}%"
)

print(
    "Forecast Growth Rate:",
    f"{forecast_growth_rate:.2f}%"
)

print(
    "Average EBIT Margin:",
    f"{average_margin:.2f}%"
)

print(
    "Terminal Growth Rate:",
    f"{terminal_growth_rate * 100:.2f}%"
)

# --------------------------------------------------
# VALUATION ASSUMPTIONS
# --------------------------------------------------

print()
print("VALUATION ASSUMPTIONS")
print("-" * 60)

print(
    "Tax Rate:",
    f"{tax_rate * 100:.2f}%"
)

print(
    "Depreciation (% Revenue):",
    f"{depreciation_percent * 100:.2f}%"
)

print(
    "CapEx (% Revenue):",
    f"{capex_percent * 100:.2f}%"
)

print(
    "Risk Free Rate:",
    f"{risk_free_rate * 100:.2f}%"
)

print(
    "Equity Risk Premium:",
    f"{equity_risk_premium * 100:.2f}%"
)

print(
    "Beta:",
    f"{beta:.2f}"
)

print(
    "Cost of Debt:",
    f"{cost_of_debt * 100:.2f}%"
)

print(
    "Cost of Equity:",
    f"{cost_of_equity * 100:.2f}%"
)

print(
    "Calculated WACC:",
    f"{wacc * 100:.2f}%"
)

# --------------------------------------------------
# FORECAST RESULTS
# --------------------------------------------------

print()
print("FORECAST RESULTS")
print("-" * 60)

for year in range(5):

    print(
        f"Year {year+1}: "
        f"Revenue={format_large_number(revenue_forecast[year], currency_symbol)} | "
        f"EBIT={format_large_number(ebit_forecast[year], currency_symbol)} | "
        f"FCFF={format_large_number(fcff_forecast[year], currency_symbol)}"
    )

# --------------------------------------------------
# DCF VALUATION
# --------------------------------------------------

print()
print("DCF VALUATION")
print("-" * 60)

print(
    "Enterprise Value:",
    format_large_number(
        enterprise_value,
        currency_symbol
    )
)

print(
    "Equity Value:",
    format_large_number(
        equity_value,
        currency_symbol
    )
)

print(
    "Fair Value Per Share:",
    f"{currency_symbol}{fair_value_per_share:.2f}"
)

# --------------------------------------------------
# SENSITIVITY TABLE
# --------------------------------------------------

print()
print("DCF SENSITIVITY TABLE")
print("-" * 60)

print(sensitivity_table)

# --------------------------------------------------
# INVESTMENT RECOMMENDATION
# --------------------------------------------------

print()
print("INVESTMENT RECOMMENDATION")
print("-" * 60)

print(
    "Current Market Price:",
    f"{currency_symbol}{current_price:.2f}"
)

print(
    "DCF Fair Value:",
    f"{currency_symbol}{fair_value_per_share:.2f}"
)

print(
    "Upside / Downside:",
    f"{upside_downside:.2f}%"
)

print(
    "Recommendation:",
    recommendation
)

# --------------------------------------------------
# EXPORT STATUS
# --------------------------------------------------

report_file = export_dcf_report(
    ticker,

    revenue_cagr,
    average_margin,

    revenue,
    ebit,
    ebit_margin,

    revenue_forecast,
    ebit_forecast,
    nopat_forecast,
    fcff_forecast,

    forecast_growth_rate,

    tax_rate,
    depreciation_percent,
    capex_percent,

    risk_free_rate,
    equity_risk_premium,
    beta,
    cost_of_debt,
    wacc,

    terminal_growth_rate,

    terminal_value,
    pv_terminal_value,

    enterprise_value,
    equity_value,
    fair_value_per_share,

    sensitivity_table,

    current_price,
    upside_downside,
    recommendation
)

print()

print("EXPORT STATUS")
print("-" * 60)

print(
    "Excel Report Generated:",
    report_file
)

print()
print("=" * 60)