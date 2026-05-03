import pandas as pd

def get_financial_input(prompt):
    """Function to ensure inputs are valid numbers"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! Please enter a valid number.")

def generate_balance_sheet():
    print("="*30)
    print("Smart Balance Sheet System")
    print("="*30)

    # Assets
    cash = get_financial_input("Enter Cash value: ")
    inventory = get_financial_input("Enter Inventory value: ")
    fixed_assets = get_financial_input("Enter Fixed Assets value: ")
    total_assets = cash + inventory + fixed_assets

    # Liabilities
    creditors = get_financial_input("Enter Creditors value: ")
    loans = get_financial_input("Enter Loans value: ")
    total_liabilities = creditors + loans

    # Equity
    capital = get_financial_input("Enter Capital value: ")
    retained_earnings = get_financial_input("Enter Retained Earnings value: ")
    total_equity = capital + retained_earnings

    total_liabilities_equity = total_liabilities + total_equity

    # Display Results
    print("\n" + "-"*10 + " Balance Sheet Summary " + "-"*10)
    print(f"Total Assets: {total_assets:,.2f}")
    print(f"Total Liabilities & Equity: {total_liabilities_equity:,.2f}")

    if total_assets == total_liabilities_equity:
        status = "Balanced ✔"
    else:
        status = "Unbalanced ✘"
    print(f"Balance Status: {status}")

    # Save Data to Excel
    report_data = {
        "Item": [
            "Cash", "Inventory", "Fixed Assets", "Total Assets", 
            "Creditors", "Loans", "Total Liabilities", 
            "Capital", "Retained Earnings", "Total Equity", "Status"
        ],
        "Value": [
            cash, inventory, fixed_assets, total_assets, 
            creditors, loans, total_liabilities, 
            capital, retained_earnings, total_equity, status
        ]
    }
    
    df = pd.DataFrame(report_data)
    df.to_excel("balance_sheet_report.xlsx", index=False)
    print("\n✅ Report successfully saved in balance_sheet_report.xlsx")

if __name__ == "__main__":
    generate_balance_sheet()