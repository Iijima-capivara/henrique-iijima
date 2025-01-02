from datetime              import datetime
from src.model.url         import url
from src.model.type        import type
from src.model.main        import main

class Site: 
   
        self._id: int
        self._url: str
        self._type: str 
        self._createdAt: datetime
        self._updatedAt: datetime

    def __init__(self):
        self._id: int = None
        self._url: str = None
        self._type: str = None
        self._createdAt = datetime.now()
        self._updatedAt = datetime.now()

    def get_id(self):
        return self._id

    def set_id(self, value: int):
        self._id = value

    def get_url(self):
        return self._url

    def set_url(self, value: str):
        self._url = value

    def get_type(self):
        return self._type

    def set_type(self, value: str):
        self._type = value

    def get_createdAt(self):
        return self._createdAt

    def set_createdAt(self, value: datetime):
        self._createdAt = value

    def get_updatedAt(self):
        return self._updatedAt

    def set_updatedAt(self, value: datetime):
        self._updatedAt = value

    def __hash__(self):
        return hash((self._id, self._url, self._type))

    def __eq__(self, other):
        if not isinstance(other, Site):
            return False
        return self._id == other._id and self._url == other._url and self._type == other._type

    def __str__(self):
        return (f"Phone(id={self._id}, url={self._url}, type={self._type}, "
                f"is_main={self._main}, created_at={self._created_at}, updated_at={self._updated_at})")

    @classmethod
    def builder(cls):
        return cls.SiteBuilder()

    class SiteBuilder:
        def __init__(self):
            self._site = site()

        def id(self, value: int):
            self._site.set_id(value)
            return self
    
        def build(self):
            return self._site