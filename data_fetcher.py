import yfinance as yf

def get_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "Company Name": info.get("longName"), 
        "Currency": info.get("currency"), 
        "Market Cap": info.get("marketCap")
        }

def get_financial_data(ticker):
    stock = yf.Ticker(ticker)
    income_stmt = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cash_flow
    info = stock.info

    return {
        "Income Statement": income_stmt,
        "Balance Sheet": balance_sheet,
        "Cash Flow": cashflow,
        "Info": info
        }

def get_row_value(statement, possible_rows):
    for row in possible_rows:
        if row in statement.index:
            return statement.loc[row]
    return None

REVENUE_LABELS = [
    "Total Revenue" 
]

EBIT_LABELS = [
    "Operating Income",  
    "Operating Profit"   
]

NET_INCOME_LABELS = [
    "Net Income"  
]

CASH_LABELS = [
    "Cash Cash Equivalents And Short Term Investments",  
    "Cash And Cash Equivalents",                        
    "Cash Equivalents",                                 
    "Cash Financial"                                    
]

DEBT_LABELS = [
    "Total Debt",   
    "Net Debt"      
]

def get_standardized_financials(ticker):
    stock=yf.Ticker(ticker)
    info = stock.info
    company_name = info.get("longName")
    country = info.get("country")
    currency = info.get("currency")
    market_cap = info.get("marketCap")
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cash_flow

    revenue = get_row_value(
        income_statement,
        REVENUE_LABELS
    )  

    ebit = get_row_value(
        income_statement,
        EBIT_LABELS
    )  

    net_income = get_row_value(
        income_statement,
        NET_INCOME_LABELS
    )  

    cash = get_row_value(
        balance_sheet,
        CASH_LABELS
    )  # Get cash

    debt = get_row_value(
        balance_sheet,
        DEBT_LABELS
    )  # Get debt

    shares_outstanding = info.get(
    "sharesOutstanding"
    )  

    return {
        "revenue": revenue,
        "ebit": ebit,
        "net_income": net_income,
        "cash": cash,
        "debt": debt,
        "shares_outstanding": shares_outstanding,
        "currency": currency,
        "country": country,
        "company_name": company_name,
        "market_cap": market_cap,
        "income_statement": income_statement,
        "cashflow": cashflow
    }

def validate_ticker(ticker):

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        return info.get("longName") is not None

    except:

        return False
    
    