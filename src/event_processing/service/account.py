from typing import Dict
from event_processing.domain.account_model import BankAccount
from contextlib import contextmanager

_store = {}  # type: Dict[str, BankAccount]


class AccountService:
    def fetch(self, accountUID: str) -> BankAccount:
        return _store.get(accountUID, None)

    def store(self, account: BankAccount) -> None:
        _store[account.accountUID] = account
