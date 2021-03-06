from typing import Dict, Optional
from event_processing.domain.model import BankAccount

_store = {}  # type: Dict[str, BankAccount]


class AccountService:
    # watch out, no locking or concurrency issues are taken into account
    def fetch(self, accountUID: str) -> Optional[BankAccount]:
        return _store.get(accountUID, None)

    # watch out, no locking or concurrency issues are taken into account
    def store(self, account: BankAccount) -> None:
        _store[account.accountUID] = account
