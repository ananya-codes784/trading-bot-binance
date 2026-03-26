import logging
import random

logger = logging.getLogger(__name__)

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # Step 1: Log request
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # Step 2: Create FAKE response (like Binance)
        order_id = random.randint(100000, 999999)

        if order_type == "MARKET":
            response = {
                "orderId": order_id,
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": "Market Price"
            }

        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("Price required for LIMIT order")

            response = {
                "orderId": order_id,
                "status": "NEW",
                "executedQty": 0,
                "avgPrice": price
            }

        else:
            raise ValueError("Invalid order type")

        # Step 3: Log response
        logger.info(f"Order response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise