from typing import List, Set, Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    aggregateId: str


@dataclass
class AccountOpened(Event):
    pass


@dataclass
class DepositOrderAccepted(Event):
    pass


@dataclass
class WithdrawOrderAccepted(Event):
    pass


@dataclass
class WithdrawOrderRejected(Event):
    pass


@dataclass
class AccountClosed(Event):
    pass


