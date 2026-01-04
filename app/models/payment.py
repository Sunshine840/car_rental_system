from enum import Enum


class CurrencyType(Enum):
    NZD = "Nzd"  # New Zealand dollars
    USD = "Usd"  # United stateS
    EUR = "Euro"  # European
    GBP = "Gbp"  # Great Britain pound
    INR = "INR"  # Indian rupee


class PaymentStatus(Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"


class Payment:
    def __init__(
        self,
        id,
        transaction_id,
        booking_id,
        amount,
        status: PaymentStatus,
        payment_method,
        timestamp,
        currency: CurrencyType = CurrencyType.NZD,
    ):
        self.id = id
        self.transaction_id = transaction_id
        self.booking_id = booking_id
        self.amount = amount
        self.status = status
        self.payment_method = payment_method
        self.currency = currency
        self.timestamp = timestamp
