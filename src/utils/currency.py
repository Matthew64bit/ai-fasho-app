import pandas as pd

rates = pd.read_csv('../../examples/exchange_table.csv').values

rate = {
    'RON2EUR': rates[0][1],
    'RON2USD': rates[1][1],
    'EUR2RON': rates[1][0],
    'EUR2USD': rates[1][2],
    'USD2RON': rates[2][0],
    'USD2EUR': rates[2][1]
}

def exchange(conversion: str, val: float) -> float:
    return val * rate[conversion]