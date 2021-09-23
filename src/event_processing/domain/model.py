from typing import List, Set, Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime, date


class BankAccount:
    accountUID: str
    accountNumber: str
    ownerName: str
    ownerBirthDate: date
    balanceInCents: int
    lastTransactionTimestamp: datetime
    withdrawRejectionCount: int
    closed: bool
    email: Optional[str]

    def __init__(self, accountUID, accountNumber, ownerName, ownerBirthDate) -> None:
        self.accountUID = accountUID
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.ownerBirthDate = ownerBirthDate
        self.balanceInCents = 0
        self.withdrawRejectionCount = 0
        self.closed = False


@dataclass
class User:
    accountUID: str
    email: str
