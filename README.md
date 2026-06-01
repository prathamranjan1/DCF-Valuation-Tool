# Automated DCF Valuation Platform

## Overview

A Python-based valuation platform that automates the Discounted Cash Flow (DCF) process for publicly listed companies across global markets.

The model automatically extracts financial statements, forecasts Free Cash Flow to Firm (FCFF), calculates WACC using CAPM inputs, performs sensitivity analysis, and generates professional Excel reports.

---

## Features

- Automated financial statement extraction
- Revenue forecasting engine
- FCFF forecasting
- Automated WACC calculation
- Country-specific risk-free rates
- Equity Risk Premium integration
- Sensitivity analysis
- Investment recommendation engine
- Excel report generation

---

## Technologies Used

- Python
- Pandas
- OpenPyXL
- Yahoo Finance (yfinance)

---

## Sample Output

### Dashboard

<img width="1470" height="956" alt="dashboard" src="https://github.com/user-attachments/assets/90631f10-7765-4586-a5a1-382d2a852ae4" />


### Sensitivity Analysis

<img width="1470" height="956" alt="sensitivity" src="https://github.com/user-attachments/assets/b86f6de0-313d-4cc8-aef0-ac9dbe46b2e1" />


### Terminal Output

<img width="1342" height="651" alt="terminal_output" src="https://github.com/user-attachments/assets/5a2788a0-09e2-4c3e-865e-f19fbc95ada8" />


---

## Project Structure

```text
DCF-Valuation-Tool/
│
├── main.py
├── data_fetcher.py
├── analysis.py
├── forecast.py
├── fcff.py
├── valuation.py
├── wacc.py
├── sensitivity.py
├── dashboard.py
├── formatter.py
├── excel_exporter.py
│
├── requirements.txt
└── README.md
```

---

## Future Enhancements

- Comparable Company Analysis
- Monte Carlo Simulation
- PDF Equity Research Reports
- Portfolio Valuation Module
