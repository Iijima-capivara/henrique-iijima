from datetime              import datetime
from src.model.email       import Email
from src.model.type        import type
from src.model.main        import main

class Email: 
    def __init__(self):
        self._id: int
        self._email: str
        self._type: str
        self._main: bool  
        self._createdAt: datetime
        self._updatedAt: datetime

    def __init__(self):
        self._id: int = None
        self._email: str = None
        self._type: str = None
        self._main: bool = None
        self._createdAt = datetime.now()
        self._updatedAt = datetime.now()

    def get_id(self):
        return self._id

    def set_id(self, value: int):
        self._id = value

    def get_email(self):
        return self._email

    def set_email(self, value: str):
        self._email = value

    def get_type(self):
        return self._type

    def set_type(self, value: str):
        self._type = value

    def get_main(self):
        return self._main

    def set_main(self, value: bool):
        self._main = value

    def get_createdAt(self):
        return self._createdAt

    def set_createdAt(self, value: datetime):
        self._createdAt = value

    def get_updatedAt(self):
        return self._updatedAt

    def set_updatedAt(self, value: datetime):
        self._updatedAt = value

    def __hash__(self):
        return hash((self._id, self._email, self._type, self._main))

    def __eq__(self, other):
        if not isinstance(other, Phone):
            return False
        return self._id == other._id and self._email == other._email and self._type == other._type and self._main == other._main

    def __str__(self):
        return (f"Phone(id={self._id}, number={self._email}, type={self._type}, "
                f"is_main={self._main}, created_at={self._created_at}, updated_at={self._updated_at})")

    @classmethod
    def builder(cls):
        return cls.emailBuilder()

    class PhoneBuilder:
        def __init__(self):
            self._email = Email()

        def id(self, value: int):
            self._email.set_id(value)
            return self
    
        def build(self):
            return self._email