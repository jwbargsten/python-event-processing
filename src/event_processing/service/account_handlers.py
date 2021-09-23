from typing import List, Dict, Callable, Type
from datetime import datetime
import event_processing.domain.account_events as events
from event_processing.domain.model import BankAccount
from event_processing.service import Services


def open_account(event: events.AccountOpened, services: Services):
    account = BankAccount(
        accountUID=event.accountUID,
        accountNumber=event.accountNumber,
        ownerName=event.ownerName,
        ownerBirthDate=event.ownerBirthDate,
    )

    # here we enrich the account with data from the user service
    user = services.user.fetch(event.accountUID)
    if user and user.email:
        account.email = user.email

    services.account.store(account)


def deposit_order(event: events.DepositOrderAccepted, services: Services):
    account = services.account.fetch(event.aggregateId)
    if not account:
        raise LookupError(f"could not find account {event.aggregateId}")
    account.balanceInCents = account.balanceInCents + event.amountInCents


def withdraw_order(event: events.WithdrawOrderAccepted, services: Services):
    account = services.account.fetch(event.aggregateId)
    if not account:
        raise LookupError(f"could not find account {event.aggregateId}")
    account.balanceInCents = account.balanceInCents - event.amountInCents
    account.lastTransactionTimestamp = datetime.now()
    services.account.store(account)


def reject_withdraw_order(event: events.WithdrawOrderRejected, services: Services):
    account = services.account.fetch(event.aggregateId)
    if not account:
        raise LookupError(f"could not find account {event.aggregateId}")
    account.withdrawRejectionCount = account.withdrawRejectionCount + 1
    services.account.store(account)


def close_account(event: events.AccountClosed, services: Services):
    account = services.account.fetch(event.aggregateId)
    if not account:
        raise LookupError(f"could not find account {event.aggregateId}")
    account.closed = True
    services.account.store(account)


EVENT_HANDLERS = {
    events.AccountOpened: [open_account],
    events.DepositOrderAccepted: [deposit_order],
    events.WithdrawOrderAccepted: [withdraw_order],
    events.WithdrawOrderRejected: [reject_withdraw_order],
    events.AccountClosed: [close_account],
}  # type: Dict[Type[events.Event], List[Callable]]
