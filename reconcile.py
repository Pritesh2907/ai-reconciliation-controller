import pandas as pd

def load_data(bank_file, ledger_file):
    bank = pd.read_csv(bank_file)
    ledger = pd.read_csv(ledger_file)
    return bank, ledger

def match_transactions(bank, ledger):
    matched = []
    unmatched = []
    for _, b_row in bank.iterrows():
        match = ledger[
            (ledger['amount'] == b_row['amount']) &
            (ledger['date'] == b_row['date'])
        ]
        if not match.empty:
            matched.append(b_row)
        else:
            unmatched.append(b_row)
    return matched, unmatched

if __name__ == "__main__":
    bank, ledger = load_data("bank.csv", "ledger.csv")
    matched, unmatched = match_transactions(bank, ledger)
    print(f"Matched: {len(matched)}, Unmatched: {len(unmatched)}")
