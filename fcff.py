def calculate_nopat(ebit_forecast, tax_rate):
    nopat_forecast = []
    for ebit in ebit_forecast:
        nopat = ebit * (1 - tax_rate)
        nopat_forecast.append(nopat)
    return nopat_forecast

def calculate_fcff(
        nopat_forecast,
        depreciation_percent,
        capex_percent,
        revenue_forecast
):
        fcff_forecast = []
        for i in range (len(revenue_forecast)):
             depreciation = (
                  revenue_forecast[i]
                  * depreciation_percent
             )

             capex = (
                  revenue_forecast[i]
                  * capex_percent
             )

             fcff = (
                  nopat_forecast[i]
                  + depreciation
                  - capex
             )

             fcff_forecast.append(fcff)
        return fcff_forecast

