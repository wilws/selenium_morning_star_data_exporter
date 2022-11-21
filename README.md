# selenium_morning_star_data_exporter
To automatically download company data from morning star


# Requirement:
pip3 install webdriver-manager --upgrade
pip3 install -U selenium


# Get Financial Data
tsla_fin_data = Scrapper('xnas','tsla','financials')
tsla_fin_data.get_financial_reports()

<!-- new folder will be created to store the reports -->
data/xnas/tsla/Balance Sheet_Annual_As Originally Reported.xls /n
data/xnas/tsla/Cash Flow_Annual_As Originally Reported.xls
data/xnas/tsla/Income Statement_Annual_As Originally Reported.xls


# Get Valuation Data
tsla_val_data = Scrapper('xnas','tsla','valuation')
tsla_val_data.get_valuation_reports()

<!-- new folder will be created to store the reports -->
data/xnas/tsla/cashFlow.xls
data/xnas/tsla/financialHealth.xls
data/xnas/tsla/growthTable.xls
data/xnas/tsla/OperatingEfficiency.xls
