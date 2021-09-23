from typing import List, Dict, Callable, Type
from datetime import datetime
import event_processing.domain.account_events as events
from event_processing.service import Services
from event_processing.domain.account_model import BankAccount


def open_account(event: events.AccountOpened, services: Services):
    # watch out, no locking or concurrency issues are taken into account
    account = BankAccount(
        accountUID=event.accountUID,
        accountNumber=event.accountNumber,
        ownerName=event.ownerName,
        ownerBirthDate=event.ownerBirthDate,
    )

    services.account.store(account)


def deposit_order(event: events.DepositOrderAccepted, services: Services):
    # watch out, no locking or concurrency issues are taken into account
    account = services.account.fetch(event.aggregateId)
    account.balanceInCents = account.balanceInCents + event.amountInCents


def withdraw_order(event: events.WithdrawOrderAccepted, services: Services):
    # watch out, no locking or concurrency issues are taken into account
    account = services.account.fetch(event.aggregateId)
    account.balanceInCents = account.balanceInCents - event.amountInCents
    account.lastTransactionTimestamp = datetime.now()
    services.account.store(account)


def reject_withdraw_order(event: events.WithdrawOrderRejected, services: Services):
    # watch out, no locking or concurrency issues are taken into account
    account = services.account.fetch(event.aggregateId)
    account.withdrawRejectionCount = account.withdrawRejectionCount + 1
    services.account.store(account)


def close_account(event: events.AccountClosed, services: Services):
    # watch out, no locking or concurrency issues are taken into account
    account = services.account.fetch(event.aggregateId)
    account.closed = True
    services.account.store(account)


EVENT_HANDLERS = {
    events.AccountOpened: [open_account],
    events.DepositOrderAccepted: [deposit_order],
    events.WithdrawOrderAccepted: [withdraw_order],
    events.WithdrawOrderRejected: [reject_withdraw_order],
    events.AccountClosed: [close_account],
}  # type: Dict[Type[events.Event], List[Callable]]
