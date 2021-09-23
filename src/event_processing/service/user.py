from typing import Optional
from event_processing.domain.model import User


class UserService:
    def fetch(self, accountUID: str) -> Optional[User]:
        pass


user_service = UserService()
