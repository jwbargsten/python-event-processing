from event_processing import __version__, inject_dependencies
from event_processing.service import Services
from datetime import date
from event_processing.domain.account_model import BankAccount
import event_processing.service.account_handlers as handlers
import event_processing.domain.account_events as events
import logging

logger = logging.getLogger(__name__)


class MockUserService:
    def fetch_user(self, user_id: str) -> str:
        print("called mock user service")


class MockAccountService:
    def fetch(self, accountUID: str) -> BankAccount:
        logger.info("called fake fetch")
        if self.tmpAccount.accountUID == accountUID:
            return self.tmpAccount
        return None

    def store(self, account: BankAccount) -> None:
        logger.info("called fake store")
        self.tmpAccount = account


def test_version():
    assert __version__ == "0.1.0"


def test_basic_events():
    event1 = events.AccountOpened(
        aggregateId="agg1",
        accountUID="agg1",
        accountNumber="123",
        ownerName="Angela Merkel",
        ownerBirthDate=date.fromisoformat("1954-07-17"),
    )
    services = Services(account=MockAccountService(), user=MockUserService())
    event_handler = inject_dependencies(handlers.EVENT_HANDLERS, services)
    event_handler.handle(event1)
    assert services.account.tmpAccount.accountUID == "agg1"
    event2 = events.WithdrawOrderAccepted(aggregateId="agg1", amountInCents=100)

    event_handler.handle(event2)
    assert services.account.tmpAccount.balanceInCents == -100
