# Trading Bot (Binance Futures Testnet)

## Objective
CLI-based trading bot supporting MARKET and LIMIT orders.

## Features
- CLI input (symbol, side, type, quantity, price)
- Input validation
- Logging (bot.log)
- Error handling
- Modular code structure

## Note
Due to Binance API access restrictions (KYC requirement), a mock trading system is implemented.

The architecture is fully compatible with Binance Futures API and can be easily integrated by replacing the mock layer with real API calls.

## How to Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Sample Output
Order ID: 123456  
Status: FILLED  
Executed Qty: 0.01  

## Future Improvement
- Real Binance API integration
- Advanced order types
