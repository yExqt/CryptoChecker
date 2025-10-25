import time 
import requests

def get_crypto_prices(cryptos, currency="eur"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(cryptos),
        "vs_currencies": currency
    }
    response = requests.get(url, params=params)
    return response.json()

from tabulate import tabulate

def show_prices(prices, currency="eur"):
    table = []
    for coin, data in prices.items():
        table.append([coin.upper(), f"{data[currency]} €"])
    print(tabulate(table, headers=["Crypto", "Price"], tablefmt="fancy_grid"))

# easyyy
def main():
    print("== crypto tracker ==")
    cryptos_input = input("insert the crryptos (es: bitcoin, ethereum, tether): ")
    cryptos = [c.strip().lower() for c in cryptos_input.split(",")]
    refresh = input("Auto refresh every 30s? (y/n): ").lower()
    auto_refresh = refresh == "y"

    while True:
        try:
            prices = get_crypto_prices(cryptos)
            print("\n")
            show_prices(prices)
        except Exception as e:
            print("Error fetching data:", e)

        if not auto_refresh:
            break
        
        print("\nUpdating in 30 seconds...\n")
        time.sleep(30)


if __name__ == "__main__":
    main()
