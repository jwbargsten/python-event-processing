from typing import List, Set, Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime,date


@dataclass
class Event:
    aggregateId: str


@dataclass
class AccountOpened(Event):
    accountUID: str
    accountNumber: str
    ownerName: str
    ownerBirthDate: date


@dataclass
class DepositOrderAccepted(Event):
    amountInCents: int


@dataclass
class WithdrawOrderAccepted(Event):
    amountInCents: int


@dataclass
class WithdrawOrderRejected(Event):
    pass


@dataclass
class AccountClosed(Event):
    pass

