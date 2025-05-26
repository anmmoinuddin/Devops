class Logger:
    def __init__(self):
        # Initialize an empty list to store logs
        self.logs = []

    def log(self, user, amount, result):
        # Log the conversion details
        self.logs.append(f"User: {user}, Amount: {amount}, Converted to: {result}")
        print(f"Log Entry: User: {user}, Amount: {amount}, Result: {result}")

    def show_logs(self):
        # Optional: method to display all logs
        print("\nConversion Logs:")
        for log in self.logs:
            print(log)

class CurrencyConverter:
    #exchange rates are stored in a dictionary
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'INR': 73.5
        
    }

    def __init__(self, user_name, amount, from_currency, to_currency, logger):
        self.user_name = user_name
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
        self.logger = logger

    def convert(self):
        # Validate currencies
        if not self.is_valid_currency(self.from_currency):
            print(f"Invalid from_currency code: {self.from_currency}")
            return None
        if not self.is_valid_currency(self.to_currency):
            print(f"Invalid to_currency code: {self.to_currency}")
            return None

        # Check if conversion is possible
        if self.from_currency not in self.exchange_rates or self.to_currency not in self.exchange_rates:
            print("Conversion not possible due to missing exchange rates.")
            return None

        # Perform conversion
        rate_from = self.exchange_rates[self.from_currency]
        rate_to = self.exchange_rates[self.to_currency]
        converted_amount = (self.amount / rate_from) * rate_to

        # Log the conversion
        self.logger.log(self.user_name, self.amount, f"{converted_amount:.2f} {self.to_currency}")

        return converted_amount

    @classmethod
    def update_exchange_rate(cls, currency_code, new_rate):
        currency_code = currency_code.upper()
        if currency_code in cls.exchange_rates:
            cls.exchange_rates[currency_code] = new_rate
            print(f"Exchange rate for {currency_code} updated to {new_rate}")
        else:
            print(f"{currency_code} is not in the exchange rates list.")

    @staticmethod
    def is_valid_currency(currency_code):
        # For simplicity, let's assume valid currencies are those stored in exchange_rates
        # Alternatively, you can expand this method to check against a list of valid codes
        return currency_code.isalpha() and len(currency_code) == 3

# Main program  
def main():
    # Instantiate a Logger object (association)
    logger = Logger()

    user_name = input("Enter your name: ")

    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    from_currency = input("Enter the currency code to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency code to convert to (e.g., EUR): ").upper()

    # Create a CurrencyConverter object
    converter = CurrencyConverter(user_name, amount, from_currency, to_currency, logger)

    result = converter.convert()
    if result is not None:
        print(f"{amount} {from_currency} is approximately {result:.2f} {to_currency}")
    else:
        print("Conversion failed due to invalid currency codes or missing rates.")

    # Optionally, display logs
    logger.show_logs()

# Run the main function
if __name__ == "__main__":
    main()
