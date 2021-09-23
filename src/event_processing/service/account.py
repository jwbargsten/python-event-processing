from typing import Dict
from event_processing.domain.model import BankAccount
from contextlib import contextmanager

_store = {}  # type: Dict[str, BankAccount]


class AccountService:
    # watch out, no locking or concurrency issues are taken into account
    def fetch(self, accountUID: str) -> BankAccount:
        return _store.get(accountUID, None)

    # watch out, no locking or concurrency issues are taken into account
    def store(self, account: BankAccount) -> None:
        _store[account.accountUID] = account
