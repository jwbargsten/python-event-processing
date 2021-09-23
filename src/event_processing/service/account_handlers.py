from typing import List, Dict, Callable, Type
import event_processing.domain.account_events as events
from event_processing.service import Services


def open_account(event: events.AccountOpened, services: Services):
    pass



EVENT_HANDLERS = {
    events.AccountOpened: [open_account],
    events.AccountClosed: [],
}  # type: Dict[Type[events.Event], List[Callable]]
