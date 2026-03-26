import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("SUCCESS")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))

    except Exception as e:
        print("FAILED:", e)

if __name__ == "_main_":
    main()