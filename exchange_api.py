import ccxt
import os
from dotenv import load_dotenv

# Load API keys from the .env file
load_dotenv()

class ExchangeAPI:
    def __init__(self, exchange_name):
        """
        Initializes an instance of the ExchangeAPI class.

        :param exchange_name: Name of the exchange (e.g., 'BINANCE').
        """
        self.exchange_name = exchange_name

        # Load API keys from the .env file based on the exchange name
        self.api_key = os.getenv(f"{exchange_name}_API_KEY")
        self.api_secret = os.getenv(f"{exchange_name}_API_SECRET")

        # Initialize the exchange object using ccxt
        self.exchange = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
            'enableRateLimit': True,  # Enable rate limiting for API requests
        })

    def fetch_ticker(self, symbol):
        """
        Fetches the ticker (price information) for a specified trading pair.

        :param symbol: The trading pair symbol (e.g., 'BTC/USDT').
        :return: The last price of the trading pair.
        """
        ticker = self.exchange.fetch_ticker(symbol)
        return ticker['last']

    def place_limit_order(self, symbol, side, price, quantity):
        """
        Places a limit order on the exchange.

        :param symbol: The trading pair symbol (e.g., 'BTC/USDT').
        :param side: The order side ('buy' or 'sell').
        :param price: The price at which to place the order.
        :param quantity: The quantity of the asset to buy or sell.
        :return: The order object returned by the exchange.
        """
        order = self.exchange.create_limit_order(
            symbol=symbol,
            side=side,
            price=price,
            amount=quantity,
        )
        return order
