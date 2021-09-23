from typing import List, Set, Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime


class BankAccount:
    accountUID: str
    accountNumber: str
    ownerName: str
    ownerBirthDate: datetime
    balanceInCents: int
    lastTransactionTimestamp: datetime
    withdrawRejectionCount: int
    closed: bool

    def __init__(self) -> None:
        pass
