from event_processing import __version__, inject_dependencies
from event_processing.service import Services
from event_processing.domain.account_model import BankAccount
import event_processing.service.account_handlers as handlers
import event_processing.domain.account_events as events


class MockUserService:
    def fetch_user(self, user_id: str) -> str:
        print("called mock user service")


class MockAccountService:
    def fetch_account(self, account_id: str) -> BankAccount:
        print("called fake fetch")

    def store_account(self, account: BankAccount) -> None:
        print("called fake store")


def test_version():
    assert __version__ == "0.1.0"



def test_something():
    event = events.AccountOpened(aggregateId="agg1")
    services = Services(account=MockAccountService(), user=MockUserService())
    event_handler = inject_dependencies(handlers.EVENT_HANDLERS, services)
    event_handler.handle(event)
