from dataclasses import dataclass
from event_processing.service.account import AccountService
from event_processing.service.user import UserService


@dataclass
class Services:
    account: AccountService
    user: UserService

