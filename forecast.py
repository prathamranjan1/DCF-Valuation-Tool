def forecast_revenue(last_revenue, growth_rate, years):
    revenues = []
    current_revenue = last_revenue 
    for year in range(years):
        current_revenue = current_revenue * (1 + growth_rate)
        revenues.append(current_revenue)
    return revenues  

def forecast_ebit(revenues, ebit_margin):
    ebit_forecast = []
    for revenue in revenues:
        ebit = revenue * ebit_margin
        ebit_forecast.append(ebit)
    return ebit_forecast

