from event_processing.domain.account_model import BankAccount


class AccountService:
    def fetch_account(self, account_id: str) -> BankAccount:
        pass

    def store_account(self, account: BankAccount) -> None:
        pass

