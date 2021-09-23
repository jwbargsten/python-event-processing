from typing import List, Dict, Callable, Type
from event_processing.service import Services
import event_processing.domain.account_events as events
import event_processing.service.account_handlers as handlers
from event_processing.service.account import AccountService
from event_processing.service.user import UserService
import logging

__version__ = "0.1.0"

log_dfmt = "%Y-%m-%d %H:%M:%S"
log_fmt = "[%(asctime)s] [%(levelname)s] %(name)s.%(funcName)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_fmt, datefmt=log_dfmt)

logger = logging.getLogger(__name__)


class EventHandler:
    def __init__(self, handlers: Dict[Type[events.Event], List[Callable]]) -> None:
        self.handlers = handlers

    def handle(self, event: events.Event) -> None:
        for handler in self.handlers[type(event)]:
            try:
                logger.debug("handling event %s with handler %s", event, handler)
                handler(event)
            except Exception:
                logger.exception("Exception handling event %s", event)
                continue


def inject_dependencies(
    handlers: Dict[Type[events.Event], List[Callable]], services: Services
):
    injected_event_handlers = {
        event_type: [
            lambda event: handler(event, services) for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.items()
    }
    return EventHandler(injected_event_handlers)


def init():
    # this is a very simple version of dependency "injection".
    # To see something more sophisticated and probably more clean,
    # check
    # https://github.com/cosmicpython/code/blob/69a88f8e05d549cc4cf01a91cd33b0fc4d87014d/src/allocation/bootstrap.py#L44
    account_service = AccountService()
    user_service = UserService()
    services = Services(account_service, user_service)
    inject_dependencies(handlers.EVENT_HANDLERS, services)
