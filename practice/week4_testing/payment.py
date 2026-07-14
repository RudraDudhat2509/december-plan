class PaymentFailedError(Exception):
    pass


def charge_customer(payment_api, amount, max_retries=3):
    if amount <= 0:
        raise ValueError("amount must be positive")

    for attempt in range(max_retries):
        response = payment_api.charge(amount)
        if response["status"] == 200:
            return response

    raise PaymentFailedError(f"payment failed after {max_retries} attempts")
