from dataclasses import dataclass
from decimal import Decimal
from datetime import date


@dataclass
class Transaction:
    id: int | None
    type: str
    amount: Decimal
    description: str
    category: str
    date: date
    account: str
    date: date

if __name__ == "__main__":
    # Example usage
    transaction = Transaction(
        id=None,
        type="income",
        amount=Decimal("3800.00"),
        description="Salário",
        category="Salário",
        account="Conta Corrente",
        date=date.today()
    )
    print(transaction)