import yfinance as yf 

def get_current_price(ticker):
    stock = yf.Ticker(ticker)  
    info = stock.info  
    return info.get("currentPrice")

def calculate_upside_downside(
    fair_value,
    current_price
):
    upside = (
        (
            fair_value
            - current_price
        )
        /
        current_price
    ) * 100
    return upside

def get_recommendation(
    upside_percentage
):
    if upside_percentage >= 15:
        return "BUY"

    elif upside_percentage >= -15:
        return "HOLD"

    else:
        return "SELL"
    
    