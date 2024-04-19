class CurrencyConverter:
    exchange_rates = {
        "USD": 1.0,  # Base currency is USD
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 110.42,
        "CHF": 0.92,
        "CAD": 1.25,
        "AUD": 1.32,
        "CNY": 6.44,
        "INR": 74.97,
        "RUB": 75.20,
        "BRL": 5.67,
        "ZAR": 15.38,
        "MXN": 20.05,
        "SGD": 1.35,
        "NZD": 1.40
        # Add more currencies and their exchange rates as needed
    }

    @classmethod
    def convert_currency(cls, amount, source_currency, target_currency):
        source_rate = cls.exchange_rates.get(source_currency)
        target_rate = cls.exchange_rates.get(target_currency)

        if source_rate is None or target_rate is None:
            return -1  # Invalid currency

        return amount / source_rate * target_rate

def main():
    print("Welcome to Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, CHF, CAD, AUD, CNY, INR, RUB, BRL, ZAR, MXN, SGD, NZD")

    amount = float(input("Enter the amount: "))
    source_currency = input("Enter the source currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., USD): ").upper()

    result = CurrencyConverter.convert_currency(amount, source_currency, target_currency)
    if result == -1:
        print("Invalid currency entered.")
    else:
        print("Converted amount:", result, target_currency)

if __name__ == "__main__":
    main()
