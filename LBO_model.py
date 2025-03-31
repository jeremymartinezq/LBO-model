def lbo_model(purchase_price, debt_ratio, equity_ratio, exit_price, years, interest_rate):
    debt = purchase_price * debt_ratio
    equity = purchase_price * equity_ratio
    annual_debt_service = debt * interest_rate
    final_equity_value = exit_price - debt
    return (final_equity_value - equity) / equity


# Example inputs
purchase_price = 7200000  # Purchase price in dollars
debt_ratio = 0.70
equity_ratio = 0.30
exit_price = 9750000  # Exit price in dollars
years = 7
interest_rate = 0.07

return_on_equity = lbo_model(purchase_price, debt_ratio, equity_ratio, exit_price, years, interest_rate)
print(f"Return on Equity: {return_on_equity * 100:.2f}%")


