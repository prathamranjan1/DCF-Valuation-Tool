def get_currency_symbol(currency):

    currency_map = {

        "USD": "$",  # US Dollar

        "INR": "₹",  # Indian Rupee

        "EUR": "€",  # Euro

        "GBP": "£",  # British Pound

        "JPY": "¥",  # Japanese Yen

        "CHF": "CHF ",  # Swiss Franc

        "CAD": "C$",

        "AUD": "A$"
    }

    return currency_map.get(
        currency,
        currency + " "
    )

def format_large_number(value, currency_symbol):

    if value >= 1_000_000_000_000:

        return (
            f"{currency_symbol}"
            f"{value/1_000_000_000_000:.2f} Trillion"
        )

    elif value >= 1_000_000_000:

        return (
            f"{currency_symbol}"
            f"{value/1_000_000_000:.2f} Billion"
        )

    elif value >= 1_000_000:

        return (
            f"{currency_symbol}"
            f"{value/1_000_000:.2f} Million"
        )

    else:

        return (
            f"{currency_symbol}"
            f"{value:,.2f}"
        )
    
    